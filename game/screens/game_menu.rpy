# -------------------------------------------------------------------
# 1. ЛЕВОЕ МЕНЮ НАВИГАЦИИ (Внутри паузы)
# -------------------------------------------------------------------
screen navigation():
    vbox:
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Дела") action ShowMenu("case_select")
        else:
            textbutton _("История") action ShowMenu("history")

        textbutton _("Настройки") action ShowMenu("preferences")

        if not main_menu:
            textbutton _("Главное меню") action MainMenu()

        textbutton _("Об игре") action ShowMenu("about")

        if renpy.variant("pc"):
            textbutton _("Выход") action Quit(confirm=not main_menu)


# -------------------------------------------------------------------
# ТРАНСФОРМАЦИИ НАКЛОНА СТРАНИЦ БЛОКНОТА (ПОД МАКЕТ ФИГМЫ)
# -------------------------------------------------------------------
transform dossier_left_tilt:
    rotate_pad False
    rotate -1.5

transform dossier_right_tilt:
    rotate_pad False
    rotate 1.0


# -------------------------------------------------------------------
# 2. ЭКРАН НАСТРОЕК (ДОСЬЕ: две страницы поверх options_dossier.png)
# -------------------------------------------------------------------
screen preferences():
    tag menu

    # Фон — раскрытая папка с блокнотом и зип-пакетом
    add "gui/options/options_dossier.png"

    # Заголовок OPTIONS над пакетом слева
    text "OPTIONS":
        font "fonts/Jost/Jost-Regular.ttf"
        size 42
        color "#ffffff"
        xpos 160
        ypos 120

    # НАВИГАЦИЯ ВНУТРИ ЗИП-ПАКЕТА СЛЕВА
    vbox:
        xpos 160
        ypos 410
        spacing 16

        textbutton _("Дела"):
            style "dossier_nav_btn"
            action ShowMenu("case_select")

        textbutton _("Настройки"):
            style "dossier_nav_btn"
            text_color "#c20000"
            text_hover_color "#ff3333"
            action ShowMenu("preferences")

        textbutton _("Об игре"):
            style "dossier_nav_btn"
            action ShowMenu("about")

        textbutton _("Выход"):
            style "dossier_nav_btn"
            action Quit(confirm=True)

    # ---------------------------------------------------------------
    # ЛЕВАЯ СТРАНИЦА БЛОКНОТА (Экран, Скорость, Язык)
    # Наклон: -1.5 градуса
    # ---------------------------------------------------------------
    vbox:
        at dossier_left_tilt
        xpos 700
        ypos 185
        xsize 420
        spacing 8

        # Display
        text _("Display"):
            font "fonts/Jost/Jost-Regular.ttf"
            size 30
            color "#1a1a1a"
            bold True

        vbox:
            xpos 35
            spacing 4

            # Window
            button:
                action Preference("display", "window")
                has hbox:
                    spacing 10
                    yalign 0.5
                if not _preferences.fullscreen:
                    add "gui/options/crossout.png":
                        yalign 0.5
                        zoom 0.7
                else:
                    null width 24 height 24
                text _("window"):
                    font "fonts/Jost/Jost-Regular.ttf"
                    size 22
                    color ("#c20000" if not _preferences.fullscreen else "#666666")
                    hover_color "#1a1a1a"

            # Fullscreen
            button:
                action Preference("display", "fullscreen")
                has hbox:
                    spacing 10
                    yalign 0.5
                if _preferences.fullscreen:
                    add "gui/options/crossout.png":
                        yalign 0.5
                        zoom 0.7
                else:
                    null width 24 height 24
                text _("fullscreen"):
                    font "fonts/Jost/Jost-Regular.ttf"
                    size 22
                    color ("#c20000" if _preferences.fullscreen else "#666666")
                    hover_color "#1a1a1a"

        null height 15

        # Text Speed
        text _("Text speed"):
            font "fonts/Jost/Jost-Regular.ttf"
            size 26
            color "#1a1a1a"
            bold True

        bar value Preference("text speed"):
            style "pref_slider"
            xsize 380

        null height 15

        # Auto-forward Speed
        text _("Auto-forward speed"):
            font "fonts/Jost/Jost-Regular.ttf"
            size 26
            color "#1a1a1a"
            bold True

        bar value Preference("auto-forward time"):
            style "pref_slider"
            xsize 380

        # Отступ: опускаем Language к оленю
        null height 80

        # Language
        vbox:
            xpos 215
            spacing 4

            text _("Language"):
                font "fonts/Jost/Jost-Regular.ttf"
                size 24
                color "#1a1a1a"
                bold True

            textbutton "english":
                style "dossier_lang_btn"
                text_color ("#c20000" if _preferences.language == "english" else "#666666")
                action Function(pick_language, "english")

            textbutton "russian":
                style "dossier_lang_btn"
                text_color ("#c20000" if _preferences.language is None else "#666666")
                action Function(pick_language, "russian")

    # ---------------------------------------------------------------
    # ПРАВАЯ СТРАНИЦА БЛОКНОТА (Пропуск, Громкость, Mute)
    # Наклон: +1.0 градус
    # ---------------------------------------------------------------
    vbox:
        at dossier_right_tilt
        xpos 1290
        ypos 190
        xsize 420
        spacing 10

        # Skip
        text _("Skip"):
            font "fonts/Jost/Jost-Regular.ttf"
            size 30
            color "#1a1a1a"
            bold True

        vbox:
            xpos 45
            spacing 4

            textbutton _("unseen text"):
                style "dossier_skip_btn"
                text_color ("#c20000" if _preferences.skip_unseen else "#666666")
                action Preference("skip", "toggle")

            textbutton _("after choices"):
                style "dossier_skip_btn"
                text_color ("#c20000" if _preferences.skip_after_choices else "#666666")
                action Preference("after choices", "toggle")

            textbutton _("transitions"):
                style "dossier_skip_btn"
                text_color ("#c20000" if _preferences.transitions == 2 else "#666666")
                action Preference("transitions", "toggle")

        null height 20

        # Music volume
        if config.has_music:
            text _("Music volume"):
                font "fonts/Jost/Jost-Regular.ttf"
                size 26
                color "#1a1a1a"
                bold True

            bar value Preference("music volume"):
                style "pref_slider"
                xsize 380

        null height 15

        # Sound volume
        if config.has_sound:
            text _("Sound volume"):
                font "fonts/Jost/Jost-Regular.ttf"
                size 26
                color "#1a1a1a"
                bold True

            bar value Preference("sound volume"):
                style "pref_slider"
                xsize 380

        # Отступ: опускаем Mute к ёлкам
        null height 75

        # Mute all — БЕЗ ВЫЛЕТОВ через selected_color стиля
        button:
            action Preference("all mute", "toggle")
            style "dossier_mute_btn"
            xoffset -20
            has hbox:
                spacing 10
                yalign 0.5
            text _("Mute all") style "dossier_mute_btn_text"
            add "gui/options/mute.png":
                yalign 0.5
                zoom 0.85

    # Кнопка Back в левом нижнем углу
    textbutton _("back"):
        xpos 115
        ypos 930
        text_font "fonts/Jost/Jost-Regular.ttf"
        text_size 36
        text_color "#777777"
        text_hover_color "#ffffff"
        action Return()

    key "game_menu" action Return()


# Стили кнопок навигации внутри пакета
style dossier_nav_btn is default:
    xalign 0.0

style dossier_nav_btn_text:
    font "fonts/Jost/Jost-Regular.ttf"
    size 30
    color "#d6d6d6"
    hover_color "#c20000"

# Стили текстовых кнопок на страницах
style dossier_skip_btn is default
style dossier_skip_btn_text:
    font "fonts/Jost/Jost-Regular.ttf"
    size 22
    hover_color "#1a1a1a"

style dossier_lang_btn is default
style dossier_lang_btn_text:
    font "fonts/Jost/Jost-Regular.ttf"
    size 22
    hover_color "#1a1a1a"

style dossier_mute_btn is default
style dossier_mute_btn_text:
    font "fonts/Jost/Jost-Regular.ttf"
    size 24
    color "#666666"
    hover_color "#1a1a1a"
    selected_color "#c20000"

# Ползунок-стрелка с красным крестиком (ysize 34 — чтобы остриё и крылья
# стрелки не срезались рендером бара)
style pref_slider is slider:
    ysize 34
    base_bar "gui/options/hover_arrow.png"
    thumb "gui/options/crossout.png"
    thumb_align 0.5
    thumb_offset 12


# -------------------------------------------------------------------
# 3. ЭКРАН ИСТОРИИ ДИАЛОГОВ (КИНОПЛЁНКА)
# -------------------------------------------------------------------
init python:
    # Сцена за историей размывается (слой master) и затемняется —
    # плёнка history_film.png имеет собственную прозрачность
    def blur_scene():
        renpy.show_layer_at([Transform(blur=8)], layer="master")

    def unblur_scene():
        renpy.show_layer_at([], layer="master")


screen history():
    tag menu
    predict False

    on "show" action Function(blur_scene)
    on "hide" action Function(unblur_scene)
    on "replaced" action Function(unblur_scene)

    add "#00000066"
    add "gui/history_film.png"
    use navigation

    text _("История"):
        xpos 480
        ypos 60
        size 45
        color "#cc0000"
        outlines [(2, "#000000", 0, 0)]

    viewport:
        xpos 480
        ypos 150
        xsize 1380
        ysize 840
        scrollbars "vertical"
        mousewheel True
        draggable True
        yinitial 0.0

        vbox:
            spacing 20
            for h in _history_list:
                window:
                    background None
                    has vbox
                    if h.who:
                        label h.who:
                            text_color "#c29b38"
                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        color "#e0dacf"
                        size 22

            if not _history_list:
                label _("История диалогов пуста.")

    textbutton _("Назад"):
        xpos gui.navigation_xpos
        yalign 0.95
        action Return()

    key "game_menu" action Return()


# -------------------------------------------------------------------
# 4. ЭКРАН "О ПРОЕКТЕ" (ABOUT)
# -------------------------------------------------------------------
screen about():
    tag menu
    add "bg menu"
    add "#000000C8"

    vbox:
        xalign 0.5
        yalign 0.3
        spacing 20

        text _("О ПРОЕКТЕ"):
            size 60
            color "#c29b38"
            xalign 0.5

        text "[config.name!t] — [config.version!t]":
            size 24
            color "#aaaaaa"
            xalign 0.5

    textbutton _("НАЗАД В МЕНЮ (Esc)"):
        xalign 0.5
        yalign 0.9
        action Return()

    key "game_menu" action Return()


# -------------------------------------------------------------------
# 5. ЭКРАН ПОДТВЕРЖДЕНИЯ (CONFIRM - ОБРЫВОК ИЗ ФИГМЫ)
# -------------------------------------------------------------------
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add "#00000088"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1573
        ysize 463
        background Image("gui/confirm_box.png", xalign=0.5, yalign=0.5)
        padding (80, 60, 80, 40)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            # Текст вопроса (тёмный, читается на белой бумаге)
            text _(message):
                color "#1a1a1a"
                size 24
                xalign 0.5
                text_align 0.5

            # Кнопки: Да — красная, Нет — черная
            hbox:
                xalign 0.5
                spacing 160

                textbutton _("Да"):
                    text_color "#c20000"
                    text_hover_color "#ff3333"
                    text_size 28
                    action yes_action

                textbutton _("Нет"):
                    text_color "#1a1a1a"
                    text_hover_color "#666666"
                    text_size 28
                    action no_action

    key "K_ESCAPE" action no_action
    key "game_menu" action no_action


# -------------------------------------------------------------------
# 6. ЭКРАН УВЕДОМЛЕНИЙ (NOTIFY)
# -------------------------------------------------------------------
screen notify(message):
    zorder 100
    frame:
        background "#1a1616ee"
        xalign 0.98
        ypos 30
        padding (20, 10)
        text "[message!tq]":
            size 20
            color "#c29b38"

    timer 3.25 action Hide('notify')