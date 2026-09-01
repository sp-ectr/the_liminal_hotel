init -2 python:
    class TimeEngine:
        """
        Ядро автоматического таймлайна с поддержкой 3 независимых профилей
        -Изолированный Ironman A/B пинг-понг сохранение для каждого профиля
        -Изолированные Timeline Anchors
        -Изолированная мета-память улик и петель для каждого профиля
        """
        _is_saving = False


        #управление активным профилем
        @classmethod
        def get_profile(cls):
            """Возвращает ID текущего профиля"""
            profile_id = getattr(persistent, "active_profile", 1)

            if profile_id not in (1, 2, 3):
                profile_id = 1
                persistent.active_profile = profile_id

            return profile_id

        @classmethod
        def set_profile(cls, profile_id):
            """Устанавливает активный профиль и инициализирует его мета-хранилище"""
            if profile_id not in (1, 2, 3):
                return

            persistent.active_profile = profile_id

            if getattr(persistent, "profiles_meta", None) is None:
                persistent.profiles_meta = {}

            if profile_id not in persistent.profiles_meta:
                persistent.profiles_meta[profile_id] = {
                    "loop_count": 1,
                    "unlocked_clues": set(),
                    "npc_suspicion": {}
                }

            renpy.save_persistent()

        @classmethod
        def get_meta(cls, profile_id=None):
            """Возвращает мета-словарь указанного или текущего профиля"""
            p = profile_id if profile_id is not None else cls.get_profile()

            if p not in (1, 2, 3):
                p = 1

            if getattr(persistent, "profiles_meta", None) is None:
                persistent.profiles_meta = {}

            if p not in persistent.profiles_meta:
                persistent.profiles_meta[p] = {
                    "loop_count": 1,
                    "unlocked_clues": set(),
                    "npc_suspicion": {}
                }
                renpy.save_persistent()

            return persistent.profiles_meta[p]

        # 1. IRONMAN PING-PONG ДЛЯ ТЕКУЩЕГО ПРОФИЛЯ
        @classmethod
        def auto_step_save(cls):
            """Автосейв в A/B слот активного дела"""
            if getattr(renpy.store, "main_menu", True) or cls._is_saving:
                return

            p = cls.get_profile()

            cls._is_saving = True
            try:
                slot_a = f"prof{p}_a"
                slot_b = f"prof{p}_b"

                latest = renpy.newest_slot(
                    regexp=rf"^prof{p}_[ab]$"
                )

                target_slot = slot_b if latest == slot_a else slot_a

                # Захватываем актуальный кадр для карточки дела
                renpy.take_screenshot()
                renpy.save(
                    target_slot,
                    f"Case #{p} Autosave"
                )

            except Exception as exc:
                renpy.log(
                    f"[TimeEngine ERROR] Ошибка автосейва профиля {p}: {exc}"
                )
            finally:
                cls._is_saving = False

        @classmethod
        def get_latest_save(cls, profile_id):
            """Возвращает самый свежий рабочий сейв для указанного дела"""
            if profile_id not in (1, 2, 3):
                return None

            return renpy.newest_slot(
                regexp=rf"^prof{profile_id}_[ab]$"
            )

        @classmethod
        def has_save(cls, profile_id):
            """Проверяет, начато ли дело"""
            return cls.get_latest_save(profile_id) is not None

        # 2. МЕХАНИКА ПЕРЕМОТКИ
        @classmethod
        def create_anchor(cls, anchor_id):
            """Фиксирует локальный якорь для активного профиля"""
            p = cls.get_profile()
            slot_name = f"prof{p}_anchor_{anchor_id}"

            renpy.save(
                slot_name,
                f"Case {p} Anchor: {anchor_id}"
            )

        @classmethod
        def rewind_to(cls, anchor_id):
            """Перемотка времени внутри активного дела"""
            p = cls.get_profile()
            slot_name = f"prof{p}_anchor_{anchor_id}"

            if not renpy.can_load(slot_name):
                renpy.notify(
                    _("Временной якорь повреждён или недоступен!")
                )
                return

            #инкрементируем счетчик петель
            meta = cls.get_meta(p)
            meta["loop_count"] = meta.get("loop_count", 1) + 1

            renpy.save_persistent()
            renpy.load(slot_name)

        # 3. МЕТА-УЛИКИ
        @classmethod
        def unlock_clue(cls, clue_id):
            meta = cls.get_meta()

            if "unlocked_clues" not in meta:
                meta["unlocked_clues"] = set()

            meta["unlocked_clues"].add(clue_id)

            renpy.save_persistent()
            renpy.notify(_("Улика зафиксирована в деле."))

        @classmethod
        def has_clue(cls, clue_id):
            meta = cls.get_meta()
            return clue_id in meta.get("unlocked_clues", set())

        @classmethod
        def get_loop_count(cls):
            meta = cls.get_meta()
            return meta.get("loop_count", 1)

        # 4. УДАЛЕНИЕ / ПЕРЕЗАПУСК ДЕЛА
        @classmethod
        def delete_profile(cls, profile_id):
            """Полностью стирает дело: сейвы A/B, якоря и мета-данные."""
            if profile_id not in (1, 2, 3):
                return

            #удаляем A/B
            for suffix in ("a", "b"):
                slot = f"prof{profile_id}_{suffix}"

                if renpy.can_load(slot):
                    renpy.unlink_save(slot)

            #удаляем все якоря этого профиля
            try:
                anchors = renpy.list_slots(
                    regexp=rf"^prof{profile_id}_anchor_"
                )

                for slot in anchors:
                    renpy.unlink_save(slot)

            except Exception as exc:
                renpy.log(
                    f"[TimeEngine ERROR] Ошибка очистки якорей дела {profile_id}: {exc}"
                )

            #сбрасываем мета-память профиля
            if (
                getattr(persistent, "profiles_meta", None)
                and profile_id in persistent.profiles_meta
            ):
                persistent.profiles_meta[profile_id] = {
                    "loop_count": 1,
                    "unlocked_clues": set(),
                    "npc_suspicion": {}
                }

            #если удаляем активное дело, переключаемся на Дело 1
            if cls.get_profile() == profile_id:
                persistent.active_profile = 1

            renpy.save_persistent()


    # Хук к системному циклу interaction
    def _ironman_interact_hook():
        TimeEngine.auto_step_save()

    config.interact_callbacks.append(_ironman_interact_hook)