init -2 python:
    import os
    import re
    import zipfile

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
            # 1. Защита от рекурсии
            if cls._is_saving:
                return

            # 2. Не сохраняем в главном меню
            if getattr(renpy.store, "main_menu", True):
                return

            # 3. СОХРАНЯЕМ ТОЛЬКО ВНУТРИ ИГРЫ и СЮЖЕТА
            current_mode = renpy.get_mode()
            if current_mode not in ("say", "menu", "pause"):
                return

            # 4. Если открыт системный экран — выходим
            for blocked_screen in ("main_menu", "case_select", "preferences", "about", "game_menu", "history"):
                if renpy.get_screen(blocked_screen):
                    return

            p = cls.get_profile()

            cls._is_saving = True
            try:
                slot_a = f"prof{p}_a"
                slot_b = f"prof{p}_b"

                latest = cls.get_latest_save(p)

                target_slot = slot_b if latest == slot_a else slot_a

                #Захватываем актуальный кадр игры
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
        def find_slot_path(cls, slot_name):
            """Находит физический файл указанного слота"""
            save_dir = renpy.config.savedir

            if not os.path.isdir(save_dir):
                return None

            # Строгий шаблон: имя слота + любой суффикс после дефиса (-LT1, -auto, -1725...) + .save
            pattern = re.compile(
                rf"^{re.escape(slot_name)}(?:-.*)?\.save$"
            )

            try:
                for fname in os.listdir(save_dir):
                    if pattern.match(fname):
                        return os.path.join(save_dir, fname)

            except Exception as exc:
                renpy.log(
                    f"[TimeEngine ERROR] Ошибка поиска файла слота {slot_name}: {exc}"
                )

            return None

        @classmethod
        def is_slot_valid(cls, slot_name):
            """Проверяет физическую целостность файла сохранения"""
            save_path = cls.find_slot_path(slot_name)

            if save_path is None:
                return False

            try:
                if not os.path.isfile(save_path):
                    return False

                if os.path.getsize(save_path) <= 0:
                    return False

                with zipfile.ZipFile(save_path, "r") as save_file:
                    if save_file.testzip() is not None:
                        return False

                    file_names = save_file.namelist()

                    if not file_names:
                        return False

                    return True

            except Exception as exc:
                renpy.log(
                    f"[TimeEngine ERROR] Повреждённый слот {slot_name}: {exc}"
                )
                return False

        @classmethod
        def get_latest_save(cls, profile_id):
            """Возвращает самый свежий рабочий сейв для указанного дела"""
            if profile_id not in (1, 2, 3):
                return None

            slots = [
                f"prof{profile_id}_a",
                f"prof{profile_id}_b"
            ]

            valid_slots = []

            for slot_name in slots:
                if cls.is_slot_valid(slot_name):
                    save_path = cls.find_slot_path(slot_name)

                    if save_path is not None:
                        valid_slots.append(
                            (
                                os.path.getmtime(save_path),
                                slot_name
                            )
                        )

            if not valid_slots:
                return None

            valid_slots.sort(
                key=lambda item: item[0],
                reverse=True
            )

            return valid_slots[0][1]

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

            if not cls.is_slot_valid(slot_name):
                renpy.notify(
                    _("Временной якорь повреждён или недоступен!")
                )
                return

             # Инкрементируем общий счётчик петель
            meta = cls.get_meta(p)
            meta["loop_count"] = meta.get("loop_count", 1) + 1

            # Отдельно считаем перемотки конкретного якоря
            anchor_rewinds = meta.setdefault("anchor_rewinds", {})
            anchor_rewinds[anchor_id] = anchor_rewinds.get(anchor_id, 0) + 1

            renpy.save_persistent()
            renpy.load(slot_name)

        @classmethod
        def get_anchor_rewind_count(cls, anchor_id):
            """Сколько раз игрок уже перематывался к конкретному якорю"""
            meta = cls.get_meta()
            return meta.get("anchor_rewinds", {}).get(anchor_id, 0)

        @classmethod
        def reset_anchor_rewind_count(cls, anchor_id):
            """Сбрасывает счётчик конкретного временного якоря"""
            meta = cls.get_meta()
            anchor_rewinds = meta.setdefault("anchor_rewinds", {})
            anchor_rewinds[anchor_id] = 0
            renpy.save_persistent()
            
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