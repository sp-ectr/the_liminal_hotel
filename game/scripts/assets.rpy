#РЕГИСТРАЦИЯ АУДИОКАНАЛОВ
init python:
    #Зацикленный фоновый эмбиент
    renpy.music.register_channel("ambient", mixer="music", loop=True)
    renpy.music.register_channel("ambient_layer", mixer="music", loop=True)

    #Отдельный независимый канал под случайные скрипы/звуки
    renpy.music.register_channel("room_sfx", mixer="sfx", loop=False)



# РЕГИСТРАЦИЯ АУДИО: ЭМБИЕНТЫ
define audio.amb_atrium = "audio/amb/amb_atrium.ogg"
define audio.amb_dead_body = "audio/amb/amb_dead_body.ogg"
define audio.amb_elevator = "audio/amb/amb_elevator.ogg"
define audio.amb_forest_night = "audio/amb/amb_forest_night.ogg"
define audio.amb_forest_night_silent = "audio/amb/amb_forest_night_silent.ogg"
define audio.amb_hotel_room = "audio/amb/amb_hotel_room.ogg"
define audio.amb_restaurant = "audio/amb/amb_restaurant.ogg"
define audio.amb_writing = "audio/amb/amb_writing.ogg"
define audio.amb_chase = "audio/amb/amb_chase.ogg"



# РЕГИСТРАЦИЯ АУДИО: МУЗЫКА
define audio.mus_atrium = "audio/music/mus_atrium.ogg"
define audio.mus_dead_body = "audio/music/mus_dead_body.ogg"
define audio.mus_elevator = "audio/music/mus_elevator.ogg"
define audio.mus_hotel_room = "audio/music/mus_hotel_room.ogg"
define audio.mus_main_menu = "audio/music/mus_main_menu.ogg"
define audio.mus_restaurant = "audio/music/mus_restaurant.ogg"



# РЕГИСТРАЦИЯ АУДИО: ГОТОВЫЕ ЭФФЕКТЫ
define audio.sfx_car_crash = "audio/sfx/sfx_car_crash.ogg"
define audio.sfx_cloth = "audio/sfx/sfx_cloth.ogg"
define audio.sfx_deer = "audio/sfx/sfx_deer.ogg"
define audio.sfx_door_handle = "audio/sfx/sfx_door_handle.ogg"
define audio.sfx_elevator = "audio/sfx/sfx_elevator.ogg"
define audio.sfx_fast_pulse = "audio/sfx/sfx_fast_pulse.ogg"
define audio.sfx_slow_pulse = "audio/sfx/sfx_slow_pulse.ogg"
define audio.sfx_lamps = "audio/sfx/sfx_lamps.ogg"
define audio.sfx_pen_click = "audio/sfx/sfx_pen_click.ogg"
define audio.sfx_radio_interference = "audio/sfx/sfx_radio_interference.ogg"
define audio.sfx_radio = "audio/sfx/sfx_radio.ogg"
define audio.sfx_writing = "audio/sfx/sfx_writing.ogg"
define audio.sfx_before_screamer = "audio/sfx/sfx_before_screamer.ogg"
define audio.sfx_radio_interference_no_voices = "audio/sfx/sfx_radio_interference_no_voices.ogg"
define audio.sfx_monster_punch = "audio/sfx/sfx_monster_punch.ogg"
define audio.sfx_chase = "audio/sfx/sfx_chase.ogg"
define audio.sfx_time_scratch = "audio/sfx/sfx_time_scratch.ogg"
define audio.sfx_impact = "audio/sfx/sfx_impact.ogg"
define audio.sfx_monster_scream_far = "audio/sfx/sfx_monster_scream_far.ogg"
define audio.sfx_monster_scream_close = "audio/sfx/sfx_monster_scream_close.ogg"
define audio.sfx_cloth_2 = "audio/sfx/sfx_cloth_2.ogg"
define audio.sfx_steps = "audio/sfx/sfx_steps.ogg"
define audio.sfx_steps_2 = "audio/sfx/sfx_steps_2.ogg"
define audio.sfx_steps_3 = "audio/sfx/sfx_steps_3.ogg"

#Звуки отеля (001 - 009)
#1 звук удалила
#2 звук удалила
define audio.sfx_hotel_room_003 = "audio/sfx/sfx_hotel_room-003.ogg"
#4 звук удалила
define audio.sfx_hotel_room_005 = "audio/sfx/sfx_hotel_room-005.ogg"
define audio.sfx_hotel_room_006 = "audio/sfx/sfx_hotel_room-006.ogg"
define audio.sfx_hotel_room_008 = "audio/sfx/sfx_hotel_room-008.ogg"
define audio.sfx_hotel_room_009 = "audio/sfx/sfx_hotel_room-009.ogg"

#Пул случайных фоновых скрипов номера отеля
define hotel_room_creaks = [
    audio.sfx_hotel_room_003,
    audio.sfx_hotel_room_006,
    audio.sfx_hotel_room_008,
    audio.sfx_hotel_room_009,
]

#ВРЕМЕННЫЕ ЗАГЛУШКИ ДЛЯ ЕЩЁ НЕ СДАННЫХ ЗВУКОВ
define audio.sfx_monster_walk = "<silence 0.0>"



#РЕГИСТРАЦИЯ АУДИО: ЗВУКИ ИНТЕРФЕЙСА (UI)
define audio.ui_click_1 = "audio/ui/ui_click-001.wav"
define audio.ui_click_2 = "audio/ui/ui_click-002.wav"
define audio.ui_hover_1 = "audio/ui/ui_hover-001.wav"
define audio.ui_hover_2 = "audio/ui/ui_hover-002.wav"
define audio.ui_start = "audio/ui/ui_start.wav"


#РЕГИСТРАЦИЯ ФОНОВ (BACKGROUNDS)
image bg forest_night = "images/bg/forest_night_back.png"
image bg room_day = "images/bg/main_room_day.png"
image bg room_day_rain = "images/bg/main_room_day_rain.png"
image bg room_night = "images/bg/main_room_night.png"
image bg room_night_rain = "images/bg/main_room_night_rain.png"
image bg office_nolight = "images/bg/office_nolight.png"
image bg office_projector = "images/bg/office_projector.png"
image bg menu = "gui/main_menu/menu.png"

# Белая вспышка (scene white / show white в скриптах)
image white = Solid("#ffffff")


#РЕГИСТРАЦИЯ UI-СПРАЙТОВ
image ui choice_idle = "gui/button/choice_idle_background.png"
image ui choice_hover = "gui/button/choice_hover_background.png"
image ui choice_rewind_idle = "gui/button/choice_rewind_idle.png"
image ui choice_rewind_hover = "gui/button/choice_rewind_hover.png"


#РЕГИСТРАЦИЯ ФОНОВ: НОВЫЕ ЛОКАЦИИ (PNG)
image bg atrium = "images/bg/atrium_back.png"
image bg desi_room = "images/bg/desi_room_back.png"
image bg elevator = "images/bg/elevator_back.png"
image bg elevator_inside = "images/bg/scary_elevator_inside_back.png"
image bg restaurant = "images/bg/restaurant_back.png"
image bg scary_elevator = "images/bg/scary_elevator_back.png"
image bg scary_elevator_inside = "images/bg/scary_elevator_inside_back.png"
image bg window_deer = "images/bg/window_deer_back.png"


#РЕГИСТРАЦИЯ ВИДЕО-ФОНОВ (Movie, зациклены по умолчанию)
image bg endless_stairs = Movie(play="images/bg/endless_stairs.webm")
image bg forest_day = Movie(play="images/bg/forest_day.webm")
# Группа "forest": при переключении олень/без оленя последний кадр предыдущего
# ролика держится на экране, пока новый не отдаст первый кадр (без квадратов в стыке)
image bg forest_deer = Movie(play="images/bg/forest_deer.webm", group="forest")
image bg forest_no_deer = Movie(play="images/bg/forest_no_deer.webm", group="forest")
image bg parking = Movie(play="images/bg/parking_back.webm", group="parking")
image bg parking_no_birds = Movie(play="images/bg/parking_no_birds.webm", group="parking")
image bg scary_hall = Movie(play="images/bg/scary_hall_back.webm")
image bg scary_stairs = Movie(play="images/bg/scary_stairs_back.webm")


#РЕГИСТРАЦИЯ CG
image cg ilay = "images/cg/ilay.png"

# Джампскейр-олень: mp4 без альфы — фон кадра чёрный (на тёмной сцене ок).
# Захотим прозрачный оверлей — тогда конвертируем transparent.mov
# в пару webm (play+mask) и меняем регистрацию
image cg deer_jumpscare = Movie(play="images/bg/deer_jumpscare_sprite.webm", loop=False)


#РЕГИСТРАЦИЯ СПРАЙТОВ ПЕРСОНАЖЕЙ (эмоции)
# Доктор: без очков — «doctor <эмоция>», в очках — «doctor glasses <эмоция>»
image doctor frown = "images/characters/doctor/without_glasses/frown.png"
image doctor grumpy = "images/characters/doctor/without_glasses/grumpy.png"
image doctor neutral = "images/characters/doctor/without_glasses/neutral.png"
image doctor skepticism = "images/characters/doctor/without_glasses/skepticism.png"
image doctor smile = "images/characters/doctor/without_glasses/smile.png"
image doctor surprise = "images/characters/doctor/without_glasses/surprise.png"
image doctor glasses frown = "images/characters/doctor/glasses/frown.png"
image doctor glasses grumpy = "images/characters/doctor/glasses/grumpy.png"
image doctor glasses neutral = "images/characters/doctor/glasses/neutral.png"
image doctor glasses skepticism = "images/characters/doctor/glasses/skepticism.png"
image doctor glasses smile = "images/characters/doctor/glasses/smile.png"
image doctor glasses surprise = "images/characters/doctor/glasses/surprise.png"

# Беглец
image fugitive big_smile = "images/characters/fugitive/big_smile.png"
image fugitive embarrassed = "images/characters/fugitive/embarrassed.png"
image fugitive nervous = "images/characters/fugitive/nervous.png"
image fugitive neutral = "images/characters/fugitive/neutral.png"
image fugitive scared = "images/characters/fugitive/scared.png"
image fugitive smile = "images/characters/fugitive/smile.png"

# Наблюдатель
image observer neutral = "images/characters/observer/neutral.png"
image observer smile = "images/characters/observer/smile.png"

# Писатель
image writer angry = "images/characters/writer/angry.png"
image writer neutral = "images/characters/writer/neutral.png"
image writer sad = "images/characters/writer/sad.png"
image writer smile = "images/characters/writer/smile.png"
image writer smile2 = "images/characters/writer/smile2.png"
image writer soft_smile = "images/characters/writer/soft_smile.png"

transform writer_normal:
    zoom 0.47
    xalign 0.5
    yalign 1.0

transform writer_left:
    zoom 0.47
    xalign 0.25
    yalign 1.0


#РЕГИСТРАЦИЯ NPC (статичные)
image bandit = "images/nps/bandit.png"
image maid = "images/nps/maid.png"


#СПЕЦЭФФЕКТЫ И АНИМАЦИИ (ATL)
define camera_shake = hpunch

transform camera_shake:
    linear 0.05 xoffset -12 yoffset 8
    linear 0.05 xoffset 14 yoffset -10
    linear 0.05 xoffset -8 yoffset 12
    linear 0.05 xoffset 10 yoffset -6
    linear 0.05 xoffset 0 yoffset 0

transform flashlight_flash:
    alpha 0.0
    linear 0.1 alpha 0.85
    linear 0.4 alpha 0.0

transform time_rewind_glitch:
    parallel:
        linear 0.04 xoffset -10
        linear 0.04 xoffset 10
        linear 0.04 xoffset -5
        linear 0.04 xoffset 0
    parallel:
        matrixcolor InvertMatrix(1.0)
        pause 0.06
        matrixcolor InvertMatrix(0.0)
        pause 0.06
        matrixcolor InvertMatrix(0.8)
        pause 0.06
        matrixcolor InvertMatrix(0.0)
