init python:
    import os

    def _find_test_save_path(slot_name):
        return TimeEngine.find_slot_path(slot_name)

    def _corrupt_test_save(slot_name):
        save_path = _find_test_save_path(slot_name)

        if save_path is None:
            return False

        try:
            with open(save_path, "wb") as save_file:
                save_file.write(
                    b"CORRUPTED_CORRUPTED_GARBAGE_00000000"
                )

            return True

        except Exception as exc:
            print(
                f"[TEST ERROR] Ошибка повреждения слота {slot_name}: {exc}"
            )
            return False

    def run_ironman_test():
        """
        Стресс-тест
        Симулирует внезапный краш питания и повреждение активного слота сейва.
        """
        print("\n==========================================")
        print(">>> запуск теста A-B <<<")
        print("==========================================")

        p = 1
        TimeEngine.set_profile(p)

        slot_a = f"prof{p}_a"
        slot_b = f"prof{p}_b"

        #1: Записываем заведомо рабочий слот A
        print("[TEST 1] Запись стабильного слота A")
        renpy.save(slot_a, "Stable Checkpoint A")

        assert TimeEngine.is_slot_valid(slot_a), \
            "ОШИБКА: Слот A должен быть физически валидным!"

        print("[TEST 1] Слот A успешно записан и проверен")

        print("[TEST 2] Запись свежего слота B")
        renpy.save(slot_b, "Latest Checkpoint B")

        assert TimeEngine.is_slot_valid(slot_b), \
            "ОШИБКА: Слот B должен быть физически валидным!"

        print("[TEST 2] Слот B успешно записан и проверен")

        #Проверяем, что сейчас новейший - B
        latest_before = TimeEngine.get_latest_save(p)
        print(f"[TEST 3] Актуальный слот до сбоя: {latest_before}")

        assert latest_before == slot_b, \
            f"ОШИБКА: Новейшим должен быть {slot_b}!"

        #3 Ломаем слот B
        print("\n Искусственно повреждаем файл слота B...")

        corrupted_b = _corrupt_test_save(slot_b)

        assert corrupted_b, \
            "ОШИБКА: Не удалось найти физический файл слота B для инъекции сбоя!"

        print("[CHAOS INJECTION] Файл слота B успешно скоррапчен!")

        #4 Проверяем реакцию движка на битый файл
        print("\n[TEST 4] Проверка реакции TimeEngine на повреждение")

        valid_b = TimeEngine.is_slot_valid(slot_b)
        print(f"[TEST 4] is_slot_valid(slot_b) после порчи: {valid_b}")

        assert not valid_b, \
            "ОШИБКА: Повреждённый слот B должен считаться невалидным!"

        # ШАГ 5 Проверяем Самовосстановление
        recovered_slot = TimeEngine.get_latest_save(p)
        print(f"[TEST 5] Восстановленный слот: {recovered_slot}")

        assert recovered_slot == slot_a, \
            f"ОШИБКА: Система должна была восстановить {slot_a}, но вернула {recovered_slot}!"

        assert TimeEngine.has_save(p), \
            "ОШИБКА: После повреждения B рабочий слот A должен оставаться доступным!"

        print("\n>>> ТЕСТ УСПЕШНО ПРОЙДЕН: Резервный слот A спас прогресс игрока! <<<")
        print("==========================================\n")

        renpy.notify(
            _("ТЕСТ ОТКАЗОУСТОЙЧИВОСТИ: УСПЕХ! Слот A спасен.")
        )

    def run_ironman_double_corruption_test():
        """
        Стресс-тест
        Симулирует повреждение обоих слотов активного дела.
        """
        print("\n==========================================")
        print(">>> запуск теста двойного повреждения <<<")
        print("==========================================")

        p = 1
        TimeEngine.set_profile(p)

        slot_a = f"prof{p}_a"
        slot_b = f"prof{p}_b"

        #1: Создаём два рабочих слота
        print("[TEST 1] Создание рабочих слотов A/B")

        renpy.save(slot_a, "Stable Checkpoint A")
        renpy.save(slot_b, "Latest Checkpoint B")

        assert TimeEngine.is_slot_valid(slot_a), \
            "ОШИБКА: Слот A должен быть валидным!"

        assert TimeEngine.is_slot_valid(slot_b), \
            "ОШИБКА: Слот B должен быть валидным!"

        #2 Повреждаем оба слота
        print("[TEST 2] Повреждение слота A")
        assert _corrupt_test_save(slot_a), \
            "ОШИБКА: Не удалось повредить слот A!"

        print("[TEST 2] Повреждение слота B")
        assert _corrupt_test_save(slot_b), \
            "ОШИБКА: Не удалось повредить слот B!"

        #3 Проверяем физическую целостность
        print("[TEST 3] Проверка повреждения обоих слотов")

        assert not TimeEngine.is_slot_valid(slot_a), \
            "ОШИБКА: Повреждённый слот A не должен быть валидным!"

        assert not TimeEngine.is_slot_valid(slot_b), \
            "ОШИБКА: Повреждённый слот B не должен быть валидным!"

        # ШАГ 4: Проверяем отсутствие рабочего сейва
        print("[TEST 4] Проверка отсутствия рабочего сейва")

        latest_after_corruption = TimeEngine.get_latest_save(p)
        print(
            f"[TEST 4] Последний рабочий слот: {latest_after_corruption}"
        )

        assert latest_after_corruption is None, \
            "ОШИБКА: После повреждения обоих слотов рабочий сейв не должен находиться!"

        assert not TimeEngine.has_save(p), \
            "ОШИБКА: has_save() не должен находить повреждённые слоты!"

        print("\n>>> ТЕСТ УСПЕШНО ПРОЙДЕН: Оба повреждённых слота корректно отброшены! <<<")
        print("==========================================\n")

        renpy.notify(
            _("ТЕСТ ОТКАЗОУСТОЙЧИВОСТИ: Оба слота повреждены.")
        )

    def test_all():
        run_ironman_test()
        run_ironman_double_corruption_test()