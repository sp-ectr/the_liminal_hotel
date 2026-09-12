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

label start:
    # Запуск сюжетной экспозиции
    jump exposition