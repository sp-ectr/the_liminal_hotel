# ВНУТРИИГРОВОЙ HUD
screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Доска улик (Tab)") action ShowMenu("investigation_board")
            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Опции") action ShowMenu('preferences')

            #Tab для быстрого вызова Доски
            key "K_TAB" action ShowMenu("investigation_board")

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True
style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xpos 1660
    ypos 1044
    xanchor 1.0
    yanchor 1.0
    spacing 24

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
    size 19
    color "#e0dacf"
    hover_color "#ffffff"