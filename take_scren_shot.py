#!/usr/bin/env python3

import time

import vlc

media_player = vlc.MediaPlayer()
media = vlc.Media("/home/devloper-pratthamesh/python_program/HUM_ROYENGE_ITNA__Full_Screen_Whatsapp_Status_Without_Watermark360p.mp4 ")
media_player.set_media(media)
media_player.vedio_set_scale(0.6)
media_player.play()
time.sleep(5)
media_player.vedio_take_snapshot(0,"F:/home/devloper-pratthamesh/python_program/image",400,300)

