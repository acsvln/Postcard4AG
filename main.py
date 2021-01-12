#!/usr/bin/env python3

from random import randint, choice

from asciimatics.effects import Print, Sprite, Snow
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework,\
    PalmFirework
from asciimatics.renderers import FigletText, Box, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import ManagedScreen
from asciimatics.paths import Path
from art import art, decor
from ascii_train import train
from xorCryptPy import xorCrypt

from stuff import *

recipient = xorCrypt("Ghgurguog&Aitdshipg")
sender = "backend guy"


def scene_start(screen, duration):
    start_text = "start the show"
    snow_text = "start the snow"
    decoration = decor("snow", both=True)
    caption1 = decoration[0] + start_text + decoration[1]
    caption2 = decoration[0] + snow_text + decoration[1]
    offset = len(caption1) // 2

    bears = art("cat smile")

    effects = [
        Print(screen, StaticRenderer([bears]), y=screen.height//2 - 2, x=screen.width // 2 - len(bears)//2),
        Print(screen, StaticRenderer([caption1, caption2]), y=screen.height//2, x=screen.width // 2 - offset, speed=15),
        Print(screen, StaticRenderer([teddy]), y=screen.height//2 + 1, x=screen.width // 2 - 21//2 - 2),
        Snow(screen)
    ]

    return Scene(effects, duration)


def scene_train(screen, duration):
    train_choo_choo = train("Choo Choo!!!")
    train_mail = train("Mails for everybody!")

    path = Path()
    path.jump_to(screen.width, screen.height//2)
    path.move_straight_to(0, screen.height//2, 100)

    sprite = Sprite(
      screen,
      renderer_dict={
          "default": StaticRenderer([
            train_choo_choo,
            train_choo_choo,
            train_choo_choo,
            train_choo_choo,
            train_choo_choo,
            train_choo_choo,
            train_choo_choo,
            train_mail,
            train_mail,
            train_mail,
            train_mail,
            train_mail])
      },
      path=path,
      clear=True)
    return Scene([sprite], duration)


def scene_girl(screen, duration):
    effects = [
      Print(screen, StaticRenderer([house]), y=screen.height//2 - 2, x=0),
      Print(screen, StaticRenderer([postbox]), y=screen.height//2 - 2, x=screen.width // 2),
      Print(screen, StaticRenderer([girl]), y=screen.height//2 - 2, x=20)
    ]
    return Scene(effects, duration)


def scene_postcard(screen, duration):
    effects = [
      Print(screen, Box(22*4, 25), y=0, x=0),
      Print(screen, StaticRenderer(["From"]), y=1, x=1),
      Print(screen, StaticRenderer([sender + " " + art("smile")]), y=1, x=10),
      Print(screen, StaticRenderer(["To"]), y=3, x=1),
      Print(screen, StaticRenderer([recipient + " " + art("confused3")]), y=3, x=10),
      Print(screen, StaticRenderer(["Topic"]), y=5, x=1),
      Print(screen, StaticRenderer(["Best wishes!!!"]), y=5, x=10),
      Print(screen, StaticRenderer(["Message"]), y=7, x=1),
      Print(screen, FigletText("Happy Birthday!", font=u'big'), y=9, x=1)
    ]
    return Scene(effects, duration)


def scene_end(screen, duration):
    effects = [
      Print(screen, FigletText("The End", font=u'doh'), y=screen.height//2 - 2, x=0),
    ]

    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(screen,
                      randint(0, screen.width),
                      randint(screen.height // 8, screen.height * 3 // 4),
                      randint(start, stop),
                      start_frame=randint(0, 250)))
    return Scene(effects, duration)


@ManagedScreen
def run_the_show(screen=None):
    screen.play([
      scene_start(screen, 100),
      scene_train(screen, 200),
      scene_girl(screen, 400),
      scene_postcard(screen, 300),
      scene_end(screen, 400)
    ], stop_on_resize=True)


if __name__ == "__main__":
    run_the_show()
