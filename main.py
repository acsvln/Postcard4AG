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

from stuff import teddy, girl, postbox, house
from utils import textBlockWidth, textBlockHeight, centerOfScreen, ScreenPoint


recipient = xorCrypt("Ghgurguog&Aitdshipg")
sender = "backend guy"


def getGirlSceneOffsets(screen):
    center = centerOfScreen(screen)

    house_width = textBlockWidth(house)
    house_height = textBlockHeight(house)

    scene_width = house_width + 3 + textBlockWidth(postbox)
    scene_height = house_height + textBlockHeight(postbox)

    offset_x = center.x - scene_width // 2
    offset_y = center.y - scene_height // 2

    return ScreenPoint(offset_x, offset_y)


def scene_start(screen, duration):
    show_text = "Start The Show"
    snow_text = "Start The Snow"
    decoration = decor("snow", both=True)
    start_caption = decoration[0] + show_text + decoration[1]
    snow_caption = decoration[0] + snow_text + decoration[1]
    smile = art("cat smile")

    center = centerOfScreen(screen)

    teddy_width = textBlockWidth(teddy)
    teddy_height = textBlockHeight(teddy)

    teddy_y_offset = teddy_height // 3

    effects = [
        Print(
          screen,
          StaticRenderer([smile]),
          y=center.y - 2 - teddy_y_offset,
          x=center.x - len(smile) // 2
        ),
        Print(
          screen,
          StaticRenderer([start_caption, snow_caption]),
          y=center.y - teddy_y_offset,
          x=center.x - len(start_caption) // 2,
          speed=15
        ),
        Print(
          screen,
          StaticRenderer([teddy]),
          y=center.y + 1 - teddy_y_offset,
          x=center.x - teddy_width // 2
        ),
        Snow(screen)
    ]

    return Scene(effects, duration)


def scene_train(screen, duration):
    choo_choo_message = train("Choo!!! Choo!!!")
    mails_message = train("Mails for everybody!")

    path = Path()
    path.jump_to(screen.width, screen.height//2)
    path.move_straight_to(0, screen.height//2, 100)

    sprite = Sprite(
      screen,
      renderer_dict={
          "default": StaticRenderer(
            [choo_choo_message] * 7 + [mails_message] * 5
          )
      },
      path=path,
      clear=True
    )

    return Scene([sprite], duration)


def scene_girl_walk(screen, duration):
    house_width = textBlockWidth(house)
    house_height = textBlockHeight(house)

    offset = getGirlSceneOffsets(screen)

    path = Path()
    path.jump_to(17 + offset.x, house_height + offset.y)
    path.move_round_to([
        (17 + offset.x, house_height+2 + offset.y),
        (18 + offset.x, house_height+3 + offset.y),
        (19 + offset.x, house_height+5 + offset.y),
        (house_width + offset.x, house_height+7 + offset.y),
        (house_width + offset.x, house_height+7 + offset.y)
      ],
      35
    )

    sprite = Sprite(
      screen,
      renderer_dict={"default": StaticRenderer([girl])},
      path=path,
      clear=True, start_frame=20, stop_frame=86
    )

    effects = [
      Print(
        screen,
        StaticRenderer([house]),
        y=offset.y,
        x=offset.x,
        transparent=True
      ),
      Print(
        screen,
        StaticRenderer([postbox]),
        y=house_height + offset.y,
        x=house_width + 3 + offset.x,
      ),
      sprite
    ]
    return Scene(effects, duration)


def scene_girl_talk(screen, duration):
    house_width = textBlockWidth(house)
    house_height = textBlockHeight(house)

    offset = getGirlSceneOffsets(screen)

    effects = [
      Print(
        screen,
        StaticRenderer(["WOW! I got a mail!!!"]),
        y=house_height + offset.y,
        x=house_width - 9 + offset.x
      )
    ]
    return Scene(effects, duration, clear=False)


def scene_postcard(screen, duration):
    border_width = 88
    border_height = 25

    sender_text = sender + " " + art("smile")
    recipient_text = recipient + " " + art("confused3")
    topic_text = "Best wishes!!!"
    message_text = "Happy Birthday!"

    field_label_x_offset = 2
    field_value_x_offset = 12

    line_offsets = range(2, 10, 2)

    text_x = 5
    text_y = 12

    center = centerOfScreen(screen)

    offset_x = center.x - border_width // 2
    offset_y = center.y - border_height // 2

    effects = [
      Print(
        screen,
        Box(border_width, border_height),
        y=offset_y,
        x=offset_x
      ),
      Print(
        screen,
        StaticRenderer(["From"]),
        y=offset_y + line_offsets[0],
        x=offset_x + field_label_x_offset
      ),
      Print(
        screen,
        StaticRenderer([sender_text]),
        y=offset_y + line_offsets[0],
        x=offset_x + field_value_x_offset
      ),
      Print(
        screen,
        StaticRenderer(["To"]),
        y=offset_y + line_offsets[1],
        x=offset_x + field_label_x_offset
      ),
      Print(
        screen,
        StaticRenderer([recipient_text]),
        y=offset_y + line_offsets[1],
        x=offset_x + field_value_x_offset
      ),
      Print(
        screen,
        StaticRenderer(["Topic"]),
        y=offset_y + line_offsets[2],
        x=offset_x + field_label_x_offset
      ),
      Print(
        screen,
        StaticRenderer([topic_text]),
        y=offset_y + line_offsets[2],
        x=offset_x + field_value_x_offset
      ),
      Print(
        screen,
        StaticRenderer(["Message"]),
        y=offset_y + line_offsets[3],
        x=offset_x + field_label_x_offset
      ),
      Print(
        screen,
        FigletText(message_text, font=u'big'),
        y=offset_y + text_y,
        x=offset_x + text_x
      )
    ]
    return Scene(effects, duration)


def scene_end(screen, duration):
    text_width = 130

    center = centerOfScreen(screen)

    effects = [
      Print(
        screen,
        FigletText("The End", font=u'doh', width=text_width),
        y=center.y,
        x=center.x - text_width // 2
      )
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
            firework(
              screen,
              randint(0, screen.width),
              randint(screen.height // 8, screen.height * 3 // 4),
              randint(start, stop),
              start_frame=randint(0, 250)
            )
        )

    return Scene(effects, duration)


@ManagedScreen
def run_the_show(screen=None):
    screen.play([
      scene_start(screen, 150),
      scene_train(screen, 200),
      scene_girl_walk(screen, 120),
      scene_girl_talk(screen, 50),
      scene_postcard(screen, 85),
      scene_end(screen, -1)
    ], stop_on_resize=True)


if __name__ == "__main__":
    run_the_show()
