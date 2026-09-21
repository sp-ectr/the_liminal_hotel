#ВЫБОР ЯЗЫКА ПЕРЕД ГЛАВНЫМ МЕНЮ
init python:
    def pick_language(lang):
        """Пишем во встроенные настройки языка движка — он сам их сохраняет и применяет.
        Русский = None, английский = "english".
        True обязателен: action Function закрывает call screen только если функция
        вернула не-None, иначе экран висит и кнопки кажутся мёртвыми."""
        target = "english" if lang == "english" else None
        if _preferences.language != target or persistent.lang_choice != lang:
            _preferences.language = target
            persistent.lang_choice = lang
            persistent.lang_just_chosen = True
            renpy.save_persistent()   # фиксируем ДО перезапуска
            renpy.utter_restart()
        return True


screen language_select():
    modal True

    add "#000000"

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 70

        text "LANGUAGE / ЯЗЫК":
            size 76
            color "#c29b38"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 90

            style_prefix "language"

            textbutton "English":
                action Function(pick_language, "english")

            textbutton "Русский":
                action Function(pick_language, "russian")

        textbutton "ВЫХОД / QUIT":
            style_prefix "language"
            text_size 28
            action Quit(confirm=False)

    # ESC тоже закрывает игру с этого экрана
    key "K_ESCAPE" action Quit(confirm=False)


style language_button is default:
    xalign 0.5

style language_button_text:
    size 52
    color "#d6d6d6"
    hover_color "#ffffff"
    selected_color "#ffffff"
    outlines [(1, "#00000080", 0, 0)]
    xalign 0.5


#Хук перед главным меню: язык спрашиваем при каждом запуске
label splashscreen:
    if persistent.lang_just_chosen:
        $ persistent.lang_just_chosen = False
        $ renpy.save_persistent()
    else:
        call screen language_select
    return
