#ВРЕМЕННЫЕ ПЛЕЙСХОЛДЕРЫ CG
image cg dead_body_half = Composite(
    (1920, 1080),
    (0, 0), "#000000CC",
    (740, 500), Text(
        "CG: ТРУП В НОМЕРЕ (БЕЗ ЛИЦА)",
        size=32,
        color="#ff4444"
    )
)

image cg dead_body_full = Composite(
    (1920, 1080),
    (0, 0), "#220000DD",
    (700, 500), Text(
        "CG: ТРУП (ЛИЦО КРУПНЫМ ПЛАНОМ)",
        size=36,
        color="#ff2222",
        bold=True
    )
)


#СЦЕНА 1: ЭКСПОЗИЦИЯ
label exposition:

    $ use_black_textbox = False
    $ hide_namebox = False

    # 1. ТЕМНЫЙ ЭКРАН
    stop music fadeout 1.0
    $ quick_menu = False
    window hide

    scene black with dissolve
    $ renpy.music.set_volume(1.0, delay=0.0, channel="ambient")
    $ renpy.music.set_volume(1.0, delay=0.0, channel="ambient_layer")
    play ambient audio.amb_writing fadein 1.5
    play sound audio.sfx_writing

    #2 КИНЕМАТОГРАФИЧНЫЙ ТИТР ПО ЦЕНТРУ
    show text "{color=#b51a1a}{size=90}{font=fonts/AlumniSansPinstripe.ttf}Самые громкие истории начинаются с убийства.{/font}{/size}{/color}" at truecenter with Dissolve(1.2)
    pause
    hide text with Dissolve(0.8)

    #3. ВСТУПИТЕЛЬНЫЙ МОНОЛОГ
    $ quick_menu = True
    window show
    with dissolve

    n "Право, я уже вижу ваши открытые рты, готовые до синеющего горла оспаривать такое пустословное заявление."

    n "Вы вот-вот скажете, что ваш любимый роман начинается далеко не с этого. И что чья-либо преждевременная смерть от чьей бы то ни было руки не является решающим фактором успеха."

    n "Да-да, всё так. Но давайте начистоту."

    n "Вы уже здесь. Я тоже."

    n "И совсем недавно я и мои друзья лицезрели зверскую картину, которая не оставит вас равнодушными."

    #4. ПЕРЕХОД К СЦЕНЕ УБИЙСТВА
    $ renpy.music.set_volume(0.15, delay=1.0, channel="ambient")
    play ambient_layer audio.amb_dead_body fadein 1.5
    play music audio.mus_dead_body fadein 2.0
    #Чёрный textbox включается на блоке с телом и зловещей музыкой.
    $ use_black_textbox = True

    scene cg dead_body_half
    with dissolve

    n "Труп распластался посреди роскошного отельного номера, а его кровь щедро напитала дорогущий паркет. Залитая в щели между вощёными досками, она при каждом шаге издавала мерзкое хлюпанье и била в нос удушливым железом."

    n "Вся эта лирика, впрочем, меркла на фоне слона в комнате."

    n "Вернее, его отсутствия."

    #5. КРУПНЫЙ ПЛАН ТРУПА
    scene cg dead_body_full with Dissolve(0.15)
    with hpunch

    n "Ведь у трупа не было лица."

    n "Плотскую маску срезали неумелым движением. Не оставили ничего: ни кожи, ни губ, ни век. Лишь оголенные бледные фасции, обрывки сосудов и огромные глазные яблоки, которые теперь смотрели в лепной потолок с застывшим вопросом."

    n "Перед нами лежало тело, напрочь лишённое идентичности, словно кто-то решил стереть человека, превратив его в безликий кусок мяса."

    n "Все присутствующие, конечно, знали, {b}кто это{/b}."

    n "А вот {b}кто{/b} из нас в одночасье {b}стал хладнокровным убийцей{/b} — загадка, которая грубыми голыми руками сдавила сердца первобытным страхом."

    n "Потому что каждый здесь мог стать следующим."

    #6. ВОЗВРАТ ИЗ СЦЕНЫ УБИЙСТВА
    stop music fadeout 1.5
    stop ambient_layer fadeout 1.5
    $ renpy.music.set_volume(1.0, delay=1.5, channel="ambient")
    #Возвращаем обычный блокнот для финального обращения к читателю.
    $ use_black_textbox = False
    $ hide_namebox = False

    scene black with dissolve

    n "Теперь-то вам интересно?"

    n "Вот и я о том же."

    n "Но, дорогой читатель, не буду лишать свою Героиню голоса, как когда-то лишили меня. Проживите нашу историю вместе с ней, её глазами."

    n "В конце концов, вы здесь ради разгадок."

    #7. ФИНАЛ ЭКСПОЗИЦИИ
    stop ambient fadeout 1.5
    stop ambient_layer fadeout 1.5
    window hide
    $ quick_menu = False

    jump prologue