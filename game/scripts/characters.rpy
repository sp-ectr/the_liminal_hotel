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



#СПРАЙТЫ: ДОКТОР
#Без очков - вариант по умолчанию
image doctor neutral = "images/characters/doctor/without_glasses/neutral.png"
image doctor smile = "images/characters/doctor/without_glasses/smile.png"
image doctor frown = "images/characters/doctor/without_glasses/frown.png"
image doctor grumpy = "images/characters/doctor/without_glasses/grumpy.png"
image doctor skepticism = "images/characters/doctor/without_glasses/skepticism.png"
image doctor surprise = "images/characters/doctor/without_glasses/surprise.png"

#В очках - атрибут glasses
image doctor glasses neutral = "images/characters/doctor/glasses/neutral.png"
image doctor glasses smile = "images/characters/doctor/glasses/smile.png"
image doctor glasses frown = "images/characters/doctor/glasses/frown.png"
image doctor glasses grumpy = "images/characters/doctor/glasses/grumpy.png"
image doctor glasses skepticism = "images/characters/doctor/glasses/skepticism.png"
image doctor glasses surprise = "images/characters/doctor/glasses/surprise.png"


#СПРАЙТЫ: БЕГЛЕЦ
image fugitive neutral = "images/characters/fugitive/neutral.png"
image fugitive smile = "images/characters/fugitive/smile.png"
image fugitive big_smile = "images/characters/fugitive/big_smile.png"
image fugitive nervous = "images/characters/fugitive/nervous.png"
image fugitive scared = "images/characters/fugitive/scared.png"
image fugitive embarrassed = "images/characters/fugitive/embarrassed.png"



#СПРАЙТЫ: НАБЛЮДАТЕЛЬ
image observer neutral = "images/characters/observer/neutral.png"
image observer smile = "images/characters/observer/smile.png"



#СПРАЙТЫ: ПИСАТЕЛЬ
image writer neutral = "images/characters/writer/neutral.png"
image writer smile = "images/characters/writer/smile.png"
image writer smile2 = "images/characters/writer/smile2.png"
image writer soft_smile = "images/characters/writer/soft_smile.png"
image writer sad = "images/characters/writer/sad.png"
image writer angry = "images/characters/writer/angry.png"


# БАЗОВЫЕ ПОЗИЦИИ И ТРАНСФОРМАЦИИ
# Плавное появление
transform sprite_appear:
    alpha 0.0
    yoffset 15
    easein 0.35 alpha 1.0 yoffset 0

# Плавное исчезновение
transform sprite_disappear:
    easeout 0.25 alpha 0.0 yoffset 15

# Стандартная позиция Доктора
transform doctor_normal:
    zoom 0.5
    xalign 0.5
    yalign 1.0

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