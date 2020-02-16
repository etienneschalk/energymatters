"""
//==============================================================================
|| Orientation Enum
|| ----------------------------
|| Each cardinal direction is associted to a number of degrees,
|| relative to the Up direction.
|| Blocks have an orientation, used for the logic and the drawing.
//==============================================================================
"""

from enum import Enum


class Orientation(Enum):  # values are degrees with TOP by default
    Up = 0
    Left = 90
    Down = 180
    Right = 270

    @staticmethod
    def from_str(label):
        if label in ('Up', 'UP', 'up'):
            return Orientation.Up
        elif label in ('Left', 'LEFT', 'left'):
            return Orientation.Left
        elif label in ('Down', 'DOWN', 'down'):
            return Orientation.Down
        elif label in ('Right', 'RIGHT', 'right'):
            return Orientation.Right
        else:
            raise NotImplementedError
