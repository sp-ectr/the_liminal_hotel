# ВХОДНАЯ ТОЧКА И БАЗОВЫЙ СТЕЙТ (The Liminal Hotel)

# 1. Глобальный мета-стейт (Переживает загрузки и откаты)
default persistent.loop_count = 1            # Счётчик циклов/перемоток
default persistent.unlocked_clues = set()    # ID найденных улик за все циклы
default persistent.npc_suspicion = {}        # Подозрительность NPC

# 2. Локальный стейт текущего таймлайна (Откатывается при перемотке)
default current_timeline_node = "prologue_start"   # Текущий сюжетный узел
default current_room = "reception"                 # Текущая комната
default inventory = []                             # Предметы в текущем цикле
default drawer_searched = False

# 3. Персонажи (ПОКА загулшки)
define d = Character(_("Детектив"), color="#c29b38")
define n = Character(None, color="#ffffff")  # ---------- Рассказчик / мысли

# 4. Стартовый лейбл игры
label start:
    scene black with dissolve

    # Фиксируем Якорь #1 при входе
    $ TimeEngine.create_anchor("hotel_entrance")

    $ current_loop = TimeEngine.get_loop_count()
    n "Петля времени: [current_loop]"

    if current_loop == 1:
        d "Я впервые переступаю порог отеля 'The Liminal Hotel'. Воздух застыл."
    else:
        d "Опять этот чертов холл... бла бла бла."

label hotel_lobby:
    $ current_room = "reception"

    if TimeEngine.has_clue("master_key"):
        n "В вашей памяти чётко отпечаталось ключ лежит в нижнем ящике стойки."
    else:
        n "Стойка регистрации заброшена. Вокруг разбросаны бумаги. Ужас"

    menu lobby_choice:
        "Обыскать стойку регистрации" if not drawer_searched:
            $ drawer_searched = True
            $ inventory.append("master_key")
            $ TimeEngine.unlock_clue("master_key")

            n "Вы достаете латунный ключ с биркой 203."
            d "Ключ теперь в кармане."
            jump hotel_lobby

        "Проверить инвентарь":
            n "В карманах: [inventory]"
            jump hotel_lobby

        "Перемотать время (Time Rewind)":
            n "Вы активируете временной скачок..."
            $ TimeEngine.rewind_to("hotel_entrance")

        "Выйти в меню":
            return