# ЭКРАН ВЫБОРА 3 ДЕЛ
screen case_select():
    tag menu
    add "images/bg/menu.png"
    add "#000000B0"

    vbox:
        xalign 0.5
        yalign 0.12
        spacing 10

        text _("ДЕЛА РАССЛЕДОВАНИЯ"):
            font "fonts/AlumniSansPinstripe.ttf"
            size 70
            color "#c29b38"
            xalign 0.5
            outlines [(2, "#000000", 0, 0)]

        text _("Выберите активное дело для продолжения или начните новое"):
            size 22
            color "#888888"
            xalign 0.5

    # 3 Карточки дел
    hbox:
        xalign 0.5
        yalign 0.55
        spacing 40

        for p_id in (1, 2, 3):
            use case_card(p_id)

    # Кнопка возврата в главное меню
    textbutton _("НАЗАД В МЕНЮ"):
        xalign 0.5
        yalign 0.92
        text_font "fonts/AlumniSansPinstripe.ttf"
        text_size 45
        text_color "#aaaaaa"
        text_hover_color "#ffffff"
        action Return()

# КАРТОЧКА ДЕЛА
screen case_card(p_id):
    $ has_save = TimeEngine.has_save(p_id)
    $ latest_slot = TimeEngine.get_latest_save(p_id)
    $ meta = TimeEngine.get_meta(p_id)
    $ loop_count = meta.get("loop_count", 1)

    frame:
        xsize 420
        ysize 480
        background "#1a1616cc"
        padding (20, 20)

        vbox:
            spacing 15
            xfill True

            # Заголовок карточки
            hbox:
                xfill True
                text _("ДЕЛО #{0}").format(p_id):
                    font "fonts/AlumniSansPinstripe.ttf"
                    size 42
                    color ("#c29b38" if has_save else "#666666")

                if has_save:
                    text _("Петля {0}").format(loop_count):
                        size 20
                        color "#ff4444"
                        yalign 0.5

            # Превью скриншота
            frame:
                xsize 380
                ysize 214
                xalign 0.5
                background "#00000088"

                if has_save and latest_slot:
                    add FileScreenshot(latest_slot, page=""):
                        xalign 0.5
                        yalign 0.5
                else:
                    text _("АРХИВ ПУСТ"):
                        align (0.5, 0.5)
                        color "#444444"
                        size 24

            # Кнопки управления
            if has_save and latest_slot:
                text FileTime(latest_slot, page="", format=_("{#file_time}%d.%m.%Y • %H:%M")):
                    size 18
                    color "#888888"
                    xalign 0.5

                null height 5

                # 1. Загрузка
                button:
                    xfill True
                    ysize 45
                    background "#c29b38"
                    hover_background "#dfb448"
                    action [
                        Function(TimeEngine.set_profile, p_id),
                        Function(renpy.load, latest_slot)
                    ]

                    text _("ПРОДОЛЖИТЬ"):
                        align (0.5, 0.5)
                        color "#000000"
                        size 20
                        bold True

                # 2. Стереть дело
                textbutton _("Стереть дело"):
                    xalign 0.5
                    text_size 16
                    text_color "#ff444488"
                    text_hover_color "#ff4444"
                    action Confirm(
                        _("Вы уверены, что хотите стереть Дело #{0}? Весь прогресс будет уничтожен!").format(p_id),
                        Function(TimeEngine.delete_profile, p_id)
                    )

            else:
                text _("Дело свободно для нового расследования"):
                    size 18
                    color "#555555"
                    xalign 0.5
                    text_align 0.5

                null height 20

                # 3. Начать новое дело
                button:
                    xfill True
                    ysize 50
                    background "#333333"
                    hover_background "#c29b38"
                    action [
                        Function(TimeEngine.set_profile, p_id),
                        Start()
                    ]

                    text _("НАЧАТЬ РАССЛЕДОВАНИЕ"):
                        align (0.5, 0.5)
                        color "#ffffff"
                        hover_color "#000000"
                        size 18