################################################################################
## Инициализация и Базовые Стили
################################################################################

init offset = -1

default use_black_textbox = False
default hide_namebox = False

init -500 python:
    # Арт-фонов кнопок в gui/button/ нет (кнопки текстовые; арт задаётся явно
    # на choice-экране и в главном меню). Штатный gui.button_properties движка
    # всегда подставляет gui/button/[prefix_]background.png и роняет игру,
    # если файла нет — вырезаем фон из свойств кнопок.
    _gui_button_properties_orig = gui.button_properties

    def _text_only_button_properties(*args, **kwargs):
        rv = _gui_button_properties_orig(*args, **kwargs)
        rv.pop("background", None)
        return rv

    gui.button_properties = _text_only_button_properties

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

# gui/bar/*.png в поставке нет — фоновые картинки бара не задаём
style bar:
    ysize gui.bar_size

style vbar:
    xsize gui.bar_size

# Горизонтального скроллбара арт нет — временная заливка
style scrollbar:
    ysize gui.scrollbar_size
    base_bar "#ffffff33"
    thumb "#c29b38cc"

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

# Вертикального слайдера арт нет — временная заливка
style vslider:
    xsize gui.slider_size
    base_bar "#ffffff33"
    thumb "#c29b38cc"

# gui/frame.png в поставке нет — все фреймы задают фон явно
style frame:
    padding gui.frame_borders.padding
    background None


################################################################################
## Диалоговые Экраны (Точная верстка под блокнот text_box.png)
################################################################################

screen say(who, what):
    window:
        id "window"

        if who is not None and not hide_namebox:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

init python:
    config.character_id_prefixes.append('namebox')


# Окно блокнота
style window:
    xalign 0.5
    yalign 0.98
    xsize 1480
    ysize 260
    padding (0, 0, 0, 0)
    background ConditionSwitch("use_black_textbox", Image("gui/text_box_black.png", xalign=0.5, yalign=1.0), "True", Image("gui/text_box.png", xalign=0.5, yalign=1.0))

style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label

# Плашка имени: ровно на верхней закладке блокнота
style namebox:
    xpos 95
    ypos -42
    xanchor 0.0
    yanchor 1.0
    background None
    padding (0, 0, 0, 0)

# Текст имени персонажа
style say_label:
    properties gui.text_properties("name", accent=True)
    size 22
    color "#1a1a1a"
    bold True

# Текст диалога: строго под закладкой с ограничением по ширине
style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 230
    ypos 68
    xsize 1180
    size 24
    color "#e0dacf"
    line_spacing 4
    adjust_spacing False


################################################################################
## Экраны Выбора и Ввода
################################################################################

screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            # перемотка времени — отдельная крупная кнопка
            $ cap = i.caption.lower()
            $ is_rewind = ("перемот" in cap) or ("отмот" in cap) or ("скачок" in cap) or ("воскрешение" in cap) or ("rewind" in cap)
            if is_rewind:
                $ rewind_caption = i.caption.strip()
                $ rewind_caption = rewind_caption[1:].strip() if rewind_caption.startswith(">") else rewind_caption
                $ rewind_caption = rewind_caption.upper()

                button:
                    style "choice_rewind_button"
                    action i.action
                    idle_background "ui choice_rewind_idle"
                    hover_background "ui choice_rewind_hover"

                    fixed:
                        xysize (1155, 297)

                        text rewind_caption:
                            style "choice_rewind_button_text"
                            xpos 0
                            ypos 133
                            xsize 980
                            yanchor 0.5
                            text_align 0.5
            else:
                textbutton i.caption action i.action:
                    idle_background "ui choice_idle"
                    hover_background "ui choice_hover"

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_rewind_button is choice_button:
    xsize 1155
    ysize 297
    padding (0, 0, 0, 0)

style choice_button_text is default:
    properties gui.text_properties("choice_button")

style choice_rewind_button_text is choice_button_text:
    size 46
    color "#161212"
    bold True

screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos
            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
