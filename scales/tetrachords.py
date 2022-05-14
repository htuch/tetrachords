from enum import Enum
import itertools

from base import *

from matplotlib.colors import LinearSegmentedColormap
import svgwrite


# Tetromino-like shapes for tetrachords across two strings.
class Shape(Enum):
    J = 1
    Z = 2
    R = 3
    I = 4


class Tetrachord:

    def __init__(self, name: str, halfsteps: tuple[int, int, int], color: str):
        self.name = name
        self.halfsteps = halfsteps
        self.start_color = color
        # The remaining 3 notes in the tetrachord have a lighter color on
        # diagrams.
        rest_color = LinearSegmentedColormap.from_list('my_cmap',
                                                       [color, 'white'])(0.35)
        self.rest_color = svgwrite.rgb(r=255 * rest_color[0],
                                       g=255 * rest_color[1],
                                       b=255 * rest_color[2])
        offsets = [0] + list(itertools.accumulate(halfsteps))
        self._offsets = [Offset(fret=offset) for offset in offsets]

    def shape_offsets(self, shape: Shape) -> list[Offset]:
        return self._offsets[:shape.value] + [
            offset + NEXT_STRING_OFFSET
            for offset in self._offsets[shape.value:]
        ]

    def markers(self, location: Location, shape: Shape) -> list[Marker]:
        return [
            Marker(location + offset, interval, color)
            for offset, interval, color in zip(self.shape_offsets(
                shape), self.intervals, [self.start_color] +
                                               3 * [self.rest_color])
        ]

    @property
    def intervals(self):
        pass


class LowerTetrachord(Tetrachord):

    @property
    def intervals(self):
        lower_intervals = ['1', '♭2', '2', '♭3', '3', '4']
        return [lower_intervals[offset.fret] for offset in self._offsets]


class UpperTetrachord(Tetrachord):

    @property
    def intervals(self):
        upper_intervals = ['5', '♭6', '6', '♭7', '7', '8']
        return [upper_intervals[offset.fret] for offset in self._offsets]


# Colors from https://www.w3.org/TR/SVG11/types.html#ColorKeywords
LOWER_MAJOR_TETRACHORD = LowerTetrachord('Major', (2, 2, 1), 'dodgerblue')
LOWER_MINOR_TETRACHORD = LowerTetrachord('Minor', (2, 1, 2), 'darkseagreen')
LOWER_HARMONIC_TETRACHORD = LowerTetrachord('Harmonic', (1, 3, 1),
                                            'lightslategrey')
LOWER_PHRYGIAN_TETRACHORD = LowerTetrachord('Phrygian', (1, 2, 2), 'chocolate')

UPPER_MAJOR_TETRACHORD = UpperTetrachord('Major', (2, 2, 1), 'dodgerblue')
UPPER_MINOR_TETRACHORD = UpperTetrachord('Minor', (2, 1, 2), 'darkseagreen')
UPPER_HARMONIC_TETRACHORD = UpperTetrachord('Harmonic', (1, 3, 1),
                                            'lightslategrey')
UPPER_PHRYGIAN_TETRACHORD = UpperTetrachord('Phrygian', (1, 2, 2), 'chocolate')

LOWER_TETRACHORDS = [
    LOWER_MAJOR_TETRACHORD,
    LOWER_MINOR_TETRACHORD,
    LOWER_HARMONIC_TETRACHORD,
    LOWER_PHRYGIAN_TETRACHORD,
]

UPPER_TETRACHORDS = [
    UPPER_MAJOR_TETRACHORD,
    UPPER_MINOR_TETRACHORD,
    UPPER_HARMONIC_TETRACHORD,
    UPPER_PHRYGIAN_TETRACHORD,
]
