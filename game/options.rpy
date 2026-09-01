# База
define config.name = _("The Liminal Hotel")
define gui.show_name = True
define config.version = "0.1.0-demo"
define config.save_directory = "TheLiminalHotel-Demo-2026"
define build.name = "The_Liminal_Hotel"

# Звуки и музыка
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

# Переходы
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

# Управление окном
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# Настройки текста
default preferences.text_cps = 0
default preferences.afm_time = 15

# Иконка игры
define config.window_icon = "gui/window_icon.png"

#Ironman
# Игра использует собственную систему автоматических A/B-сохранений
# Штатное сохранение, quicksave, rollback и стандартный autosave отключены
define config.rollback_enabled = False
define config.has_quicksave = False
define config.has_autosave = False

#Язык по умолчанию
define config.default_language = "english"

#Настройка сборки
init python:
    #Игнорируем системный мусор и исходники в билде
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)          # Игнорируем тяжелые исходники Photoshop
    build.classify('**.clip', None)         # Игнорируем Clip Studio
    build.classify('**.kra', None)          # Игнорируем Krita
    build.classify('log.txt', None)
    build.classify('traceback.txt', None)

    ## Документация в корне архива
    build.documentation('*.html')
    build.documentation('*.txt')