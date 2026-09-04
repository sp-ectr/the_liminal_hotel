# ВХОДНАЯ ТОЧКА И БАЗОВЫЙ СТЕЙТ (The Liminal Hotel)

# 1. Глобальный мета-стейт (Переживает загрузки и откаты)
default persistent.loop_count = 1            # Счётчик циклов/перемоток
default persistent.unlocked_clues = set()    # ID найденных улик за все циклы
default persistent.npc_suspicion = {}        # Подозрительность NPC

# 2. Локальный стейт текущего таймлайна (Откатывается при перемотке)
default current_timeline_node = "prologue_start"   # Текущий сюжетный узел
default current_room = "reception"                 # Текущая комната
default inventory = []                             # Предметы в текущем цикле
default drawer_searched = False                    # Обыскан ли ящик стола
default ashtray_searched = False                   # Осмотрена ли пепельница

# 3. Персонажи (ПОКА загулшки)
define d = Character(_("Детектив"), color="#c29b38")
define n = Character(None, color="#ffffff")  # ---------- Рассказчик / мысли

# 4. Стартовый лейбл игры
label start:
    scene expression "images/bg/menu.png" with dissolve

    # Фиксируем Якорь #1 при входе
    $ TimeEngine.create_anchor("hotel_entrance")

    $ current_loop = TimeEngine.get_loop_count()
    n "Петля времени: [current_loop]"

    if current_loop == 1:
        d "Я впервые переступаю порог отеля 'The Liminal Hotel'. Воздух застыл."
    else:
        d "Опять этот чертов холл... Ощущение дежавю давит на виски."

label hotel_lobby:
    $ current_room = "reception"

    # Сюжетные реплики на основе найденных улик
    if TimeEngine.has_clue("master_key") and TimeEngine.has_clue("torn_receipt"):
        n "В вашей памяти чётко сошлись две детали: латунный ключ и обгоревшая квитанция ведут к номеру 203."
    elif TimeEngine.has_clue("master_key"):
        n "В вашей памяти отпечаталось: ключ лежит в нижнем ящике стойки."
    else:
        n "Стойка регистрации заброшена. Вокруг разбросаны бумаги и тлеет огарок сигареты."

    menu lobby_choice:
        # Улика #1
        "Обыскать стойку регистрации" if not drawer_searched:
            $ drawer_searched = True
            $ inventory.append("master_key")
            $ TimeEngine.unlock_clue("master_key")

            n "Вы выдвигаете ящик и достаете латунный ключ с биркой '203'."
            d "Ключ теперь в кармане. Нажмите (Tab), чтобы посмотреть доску расследования."
            jump hotel_lobby

        # Улика #2 (Связана с ключом)
        "Осмотреть тяжёлую пепельницу на столике" if not ashtray_searched:
            $ ashtray_searched = True
            $ inventory.append("torn_receipt")
            $ TimeEngine.unlock_clue("torn_receipt")

            n "Среди пепла вы находите обгоревший край квитанции за номер 203."
            d "Интересно... Кажется, эта квитанция как-то связана с ключом от того же номера."
            jump hotel_lobby

        "Проверить карманы (Инвентарь)":
            n "В карманах сейчас: [inventory]"
            jump hotel_lobby

        "Перемотать время (Time Rewind)":
            n "Вы активируете временной скачок назад..."
            $ TimeEngine.rewind_to("hotel_entrance")

        "Выйти в главное меню":
            $ MainMenu(confirm=False)()