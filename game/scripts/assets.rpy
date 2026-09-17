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

#Звуки отеля (001 - 009)
define audio.sfx_hotel_room_001 = "audio/sfx/sfx_hotel_room-001.ogg"
define audio.sfx_hotel_room_002 = "audio/sfx/sfx_hotel_room-002.ogg"
define audio.sfx_hotel_room_003 = "audio/sfx/sfx_hotel_room-003.ogg"
define audio.sfx_hotel_room_004 = "audio/sfx/sfx_hotel_room-004.ogg"
define audio.sfx_hotel_room_005 = "audio/sfx/sfx_hotel_room-005.ogg"
define audio.sfx_hotel_room_006 = "audio/sfx/sfx_hotel_room-006.ogg"
define audio.sfx_hotel_room_007 = "audio/sfx/sfx_hotel_room-007.ogg"
define audio.sfx_hotel_room_008 = "audio/sfx/sfx_hotel_room-008.ogg"
define audio.sfx_hotel_room_009 = "audio/sfx/sfx_hotel_room-009.ogg"

#Пул случайных фоновых скрипов номера отеля
define hotel_room_creaks = [
    audio.sfx_hotel_room_001,
    audio.sfx_hotel_room_002,
    audio.sfx_hotel_room_003,
    audio.sfx_hotel_room_004,
    audio.sfx_hotel_room_005,
    audio.sfx_hotel_room_006,
    audio.sfx_hotel_room_007,
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
image bg menu = "images/bg/menu.png"


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