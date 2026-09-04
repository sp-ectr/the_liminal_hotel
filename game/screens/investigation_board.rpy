init -1 python:
    class BoardConnectionsDisplayable(renpy.Displayable):
        """
        Красные нити между уликами
        """
        def __init__(self, connections, **kwargs):
            super(BoardConnectionsDisplayable, self).__init__(**kwargs)
            self.connections = connections

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            canvas = rv.canvas()

            line_color = (194, 34, 34, 210)
            shadow_color = (0, 0, 0, 100)

            for _, pos1, pos2 in self.connections:
                canvas.line(shadow_color, (pos1[0] + 2, pos1[1] + 2), (pos2[0] + 2, pos2[1] + 2), 4)
                canvas.line(line_color, pos1, pos2, 3)

            return rv


#ЭКРАН ДОСКИ РАССЛЕДОВАНИЯ
screen investigation_board():
    tag menu

    default selected_clue = None

    #Фон
    add "images/bg/menu.png"
    add "#000000A0"

    $ meta = TimeEngine.get_meta()
    $ unlocked_ids = meta.get("unlocked_clues", set())
    $ unlocked_clues = ClueDatabase.get_by_ids(unlocked_ids)
    $ connections = ClueDatabase.get_unique_connections(unlocked_ids)
    $ total_clues_count = len(ClueDatabase.get_all())

    add BoardConnectionsDisplayable(connections)

    #Шапка
    hbox:
        xalign 0.05
        yalign 0.04
        spacing 25

        text _("ДОСКА РАССЛЕДОВАНИЯ"):
            font "fonts/AlumniSansPinstripe.ttf"
            size 55
            color "#c29b38"
            outlines [(2, "#000000", 0, 0)]

        text _("Улик обнаружено: {0} / {1}").format(len(unlocked_clues), total_clues_count):
            size 22
            color "#aaaaaa"
            yalign 0.6

    #Карточки и улики
    for clue in unlocked_clues:
        use clue_pin_card(clue)

    #Кнопки закрытия
    textbutton _("ЗАКРЫТЬ ДОСКУ (Tab / Esc)"):
        xalign 0.95
        yalign 0.04
        text_font "fonts/AlumniSansPinstripe.ttf"
        text_size 40
        text_color "#d6d6d6"
        text_hover_color "#ffffff"
        action Return()

    #Окно осмотра
    if selected_clue:
        use clue_inspect_modal(selected_clue)

    #Горячие клавиши закрытия
    key "game_menu" action (SetScreenVariable("selected_clue", None) if selected_clue else Return())
    key "K_TAB" action (SetScreenVariable("selected_clue", None) if selected_clue else Return())


#ВИДЖЕТ КАРТОЧКИ УЛИКИ
screen clue_pin_card(clue):
    button:
        pos clue.pos
        anchor (0.5, 0.5)
        xsize 170
        ysize 210
        background "#e6decb"
        hover_background "#fff8e7"
        padding (10, 10, 10, 10)
        action SetScreenVariable("selected_clue", clue)

        vbox:
            spacing 6
            xfill True

            frame:
                xsize 150
                ysize 130
                background "#00000033"
                add clue.thumb:
                    xalign 0.5
                    yalign 0.5
                    ysize 120
                    fit "contain"

            text clue.title:
                size 14
                color "#1a1a1a"
                bold True
                xalign 0.5
                text_align 0.5

        #Красная булавка
        add "#c22222":
            xsize 14
            ysize 14
            xalign 0.5
            yoffset -15



#ОКНО ДЕТАЛЬНОГО ОСМОТРА
screen clue_inspect_modal(clue):
    button:
        xfill True
        yfill True
        background "#000000C0"
        action SetScreenVariable("selected_clue", None)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 850
        ysize 520
        background "#1a1616f0"
        padding (30, 30)

        hbox:
            spacing 30
            xfill True

            frame:
                xsize 340
                ysize 460
                background "#00000088"
                add clue.full_image:
                    align (0.5, 0.5)
                    fit "contain"

            vbox:
                spacing 15
                xfill True

                text _("({0})").format(clue.category.upper()):
                    size 16
                    color "#c29b38"
                    bold True

                text clue.title:
                    font "fonts/AlumniSansPinstripe.ttf"
                    size 48
                    color "#ffffff"

                add "#c29b38":
                    xsize 400
                    ysize 2

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    ysize 250

                    text clue.description:
                        size 20
                        color "#cccccc"
                        line_spacing 4

                textbutton _("Закрыть осмотр (Esc)"):
                    xalign 1.0
                    text_size 18
                    text_color "#c29b38"
                    text_hover_color "#ffffff"
                    action SetScreenVariable("selected_clue", None)