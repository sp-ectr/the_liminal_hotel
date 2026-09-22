#РЕГИСТРАЦИЯ ПЕРСОНАЖЕЙ И ДИНАМИЧЕСКИХ ИМЕН
init python:
    # Функция динамического имени гг
    def get_player_name():
        if player_first_name or player_last_name:
            return f"{player_first_name} {player_last_name}".strip()
        return _("Я")

#1 Главная героиня
default player_first_name = ""
default player_last_name = ""
default player_display_name = _("Я")

#Прямая речь ГГ: пока имя пустое - пишет "Я", после ввода - "Имя Фамилия"
define me = Character("[player_display_name]")

#Рассказчик / внутренний монолог
define n = Character(None)

#2. Доктор (Эверетт Димаано)
#До раскрытия личности на плашке ??? после раскрытия - "Доктор Димаано"
default doc_display_name = _("???")
define doc = Character("[doc_display_name]", image="doctor")

#3 Беглец
define fug = Character(_("Беглец"), image="fugitive")

#4 Наблюдатель
define obs = Character(_("Наблюдатель"), image="observer")

#5 Писатель
define wri = Character(_("Писатель"), image="writer")

#6 Служебные голоса
define radio = Character(_("Радио"))
define unk = Character(_("???"))


# БАЗОВЫЕ ПОЗИЦИИ И ТРАНСФОРМАЦИИ

# Плавное появление
transform sprite_appear:
    alpha 0.0
    yoffset 15
    easein 0.35 alpha 1.0 yoffset 0

# Плавное исчезновение
transform sprite_disappear:
    easeout 0.25 alpha 0.0 yoffset 15


# Крупный план Доктора
transform close_up_doctor:
    zoom 0.75
    xalign 0.5
    yalign 0.15

# Крупный план Доктора с затемнением
transform close_up_darkened:
    zoom 0.75
    xalign 0.5
    yalign 0.15
    matrixcolor TintMatrix("#333333")

# Возврат Доктора к обычному состоянию
transform restore_doctor_normal:
    easein 0.8 zoom 0.5 xalign 0.5 yalign 1.0 matrixcolor TintMatrix("#ffffff")