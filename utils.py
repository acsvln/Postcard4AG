from collections import namedtuple

ScreenPoint = namedtuple('ScreenPoint', ['x', 'y'])


def textBlockWidth(block):
    return len(max(block.split('\n'), key=lambda x: len(x)))


def textBlockHeight(block):
    return block.count('\n') + 1


def centerOfScreen(screen):
    return ScreenPoint(screen.width // 2, screen.height//2)
