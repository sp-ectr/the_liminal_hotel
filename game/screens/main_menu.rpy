#АНИМАЦИИ ГЛАВНОГО МЕНЮ
transform menu_logo_intro:
    alpha 0.0 zoom 1.08
    easein 1.4 alpha 1.0 zoom 1.0

transform menu_buttons_intro:
    alpha 0.0 yoffset 20
    pause 0.5
    easein 0.8 alpha 1.0 yoffset 0


#ЭКРАН ГЛАВНОГО МЕНЮ
screen main_menu():
    tag menu

    add "bg menu"

    add "images/gui/logo.png":
        xalign 0.5
        yalign 0.46
        at menu_logo_intro

    hbox:
        xalign 0.5
        yalign 0.94
        spacing 70
        at menu_buttons_intro

        use main_menu_nav_button(_("Start"), ShowMenu("case_select"), click_sound=audio.ui_start)
        use main_menu_nav_button(_("Options"), ShowMenu("preferences"))
        use main_menu_nav_button(_("About"), ShowMenu("about"))
        use main_menu_nav_button(_("Exit"), Quit(confirm=False))

# КОМПОНЕНТ КНОПКИ ГЛАВНОГО МЕНЮ
screen main_menu_nav_button(label_text, button_action, click_sound=None):
    button:
        action button_action
        xanchor 0.5
        yanchor 0.5

        # Рандомизация наведения (ui_hover_1 или ui_hover_2)
        hover_sound renpy.random.choice([audio.ui_hover_1, audio.ui_hover_2])

        # Если задан специальный звук (ui_start) — играет он, иначе рандомный клик (1 или 2)
        activate_sound (click_sound if click_sound else renpy.random.choice([audio.ui_click_1, audio.ui_click_2]))

        hover_background Transform("images/gui/pickMenu.png", align=(0.5, 0.5))

        text label_text:
            font "fonts/AlumniSansPinstripe.ttf"
            size 62
            color "#d6d6d6"
            hover_color "#ffffff"
            outlines [(1, "#00000080", 0, 0)]
            xalign 0.5
            yalign 0.5