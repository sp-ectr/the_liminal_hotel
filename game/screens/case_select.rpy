init python:
    import time

    # Action для загрузки дела
    class LoadCase(Action):
        def __init__(self, profile_id, slot_name):
            self.profile_id = profile_id
            self.slot_name = slot_name

        def __call__(self):
            TimeEngine.set_profile(self.profile_id)
            renpy.load(self.slot_name)

        def get_sensitive(self):
            return self.slot_name is not None and TimeEngine.is_slot_valid(self.slot_name)


define CASE_FONT = "fonts/Roboto_Condensed/RobotoCondensed-Medium.ttf"

# Штамп «продолжить»: из арта 366x275 вырезаем только саму печать
# (видимая зона ~(26,86)-(340,184) + поля). im.Scale всего арта в 330x90
# сплющивал печать в полоску — текст торчал над ней
define CONTINUE_STAMP_IDLE = LiveCrop((16, 76, 334, 118), "gui/case_select/button_continue.png")
define CONTINUE_STAMP_HOVER = im.Scale("gui/case_select/button_continue_hover.png", 334, 118)


# Карточки делаем больше, чтобы все элементы точно помещались внутри бумаги
define CASE_CARD_SIZE = {
    1: (610, 760),
    2: (560, 735),
    3: (660, 760)
}


# ЭКРАН ВЫБОРА 3 ДЕЛ
screen case_select():
    tag menu

    add "gui/case_select/bg_case_select.png"

    # Заголовок
    vbox:
        xalign 0.5
        yalign 0.135
        spacing 5

        text _("АРХИВ РАССЛЕДОВАНИЙ"):
            font CASE_FONT
            size 48
            color "#ffffff"
            xalign 0.5

        text _("Выберите активное дело для продолжения или начните новое"):
            font CASE_FONT
            size 24
            color "#cc0000"
            xalign 0.5


    # 3 конверта дел
    hbox:
        xalign 0.5
        yalign 0.62
        spacing 18

        for p_id in (1, 2, 3):
            use case_card(p_id)


    # Возврат в игру
    textbutton _("НАЗАД"):
        xalign 0.5
        yalign 0.93
        text_size 30
        text_color "#888888"
        text_hover_color "#ffffff"
        action Return()

# КАРТОЧКА ДЕЛА
screen case_card(p_id):

    $ has_save = TimeEngine.has_save(p_id)
    $ latest_slot = TimeEngine.get_latest_save(p_id)
    $ meta = TimeEngine.get_meta(p_id)
    $ loop_count = meta.get("loop_count", 1)

    # Битое дело:
    $ is_broken = meta.get("corrupted", False) or (has_save and not TimeEngine.is_slot_valid(latest_slot))

    $ card_w, card_h = CASE_CARD_SIZE[p_id]

    $ art = (
        ("gui/case_broken_%d.png" % p_id)
        if is_broken
        else ("gui/case_select/case%d.png" % p_id)
    )


    fixed:
        xsize card_w
        ysize card_h


        # Сам конверт
        add art:
            xalign 0.5
            yalign 0.0
            xsize card_w
            ysize card_h
            fit "contain"


        # -------------------------
        # ШАПКА ДЕЛА
        # -------------------------

        hbox:
            xalign 0.5
            ypos 118
            spacing 10

            text _("ДЕЛО #[p_id]"):
                font CASE_FONT
                size 31
                color "#1a1a1a"

            if has_save:
                text _("Петля [loop_count]"):
                    font CASE_FONT
                    size 16
                    color "#cc0000"
                    yalign 0.6



        # -------------------------
        # ПОВРЕЖДЁННОЕ ДЕЛО
        # -------------------------

        if is_broken:

            text _("[ ДЕЛО ПОВРЕЖДЕНО ]"):
                xalign 0.5
                ypos 455
                font CASE_FONT
                size 24
                color "#cc0000"



        # -------------------------
        # ДЕЛО С СОХРАНЕНИЕМ
        # -------------------------

        elif has_save and latest_slot:

            # Скриншот
            frame:
                xalign 0.5
                ypos 205
                padding (6, 6)
                background "#000000"

                fixed:
                    xsize 315
                    ysize 177

                    $ thumb_img = renpy.slot_screenshot(latest_slot)

                    if thumb_img:
                        add thumb_img:
                            xalign 0.5
                            yalign 0.5
                            fit "contain"
                            xsize 315
                            ysize 177

                    else:
                        text _("НЕТ СКРИНШОТА"):
                            xalign 0.5
                            yalign 0.5
                            font CASE_FONT
                            size 16
                            color "#444444"


            # Дата последнего захода
            $ mtime = renpy.slot_mtime(latest_slot)

            if mtime:
                $ time_str = time.strftime(
                    "%d.%m.%Y | %H:%M",
                    time.localtime(mtime)
                )

                text "[time_str]":
                    xalign 0.5
                    ypos 395
                    font CASE_FONT
                    size 14
                    color "#1a1a1a"


            # Продолжить
            button:
                xalign 0.5
                ypos 435
                xsize 334
                ysize 118

                background CONTINUE_STAMP_IDLE
                hover_background CONTINUE_STAMP_HOVER

                action LoadCase(p_id, latest_slot)

                text _("ПРОДОЛЖИТЬ"):
                    xalign 0.5
                    yalign 0.5
                    font CASE_FONT
                    size 27
                    color "#cc0033"
                    hover_color "#ffffff"



        # -------------------------
        # ПУСТОЕ ДЕЛО
        # -------------------------

        else:

            # Чёрное пустое окно
            frame:
                xalign 0.5
                ypos 205
                padding (6, 6)
                background "#000000"

                fixed:
                    xsize 315
                    ysize 177


            # Начать расследование
            button:
                xalign 0.5
                ypos 435
                xsize 334
                ysize 118

                background CONTINUE_STAMP_IDLE
                hover_background CONTINUE_STAMP_HOVER

                action [
                    Function(TimeEngine.set_profile, p_id),
                    Start()
                ]

                text _("НАЧАТЬ РАССЛЕДОВАНИЕ"):
                    xalign 0.5
                    yalign 0.5
                    font CASE_FONT
                    size 22
                    color "#1a1a1a"
                    hover_color "#cc0000"



        # -------------------------
        # СТЕРЕТЬ ДЕЛО
        # -------------------------

        if has_save:

            textbutton _("Стереть дело"):
                xalign 0.5
                ypos 560
                text_font CASE_FONT
                text_size 13
                text_color "#cc0000aa"
                text_hover_color "#cc0000"

                action Confirm(
                    renpy.translate_string(
                        _("Вы уверены, что хотите стереть Дело #{0}? Весь прогресс будет уничтожен!")
                    ).format(p_id),

                    Function(
                        TimeEngine.delete_profile,
                        p_id
                    )
                )