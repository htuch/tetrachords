# We assume an all-fourths tuning except during final rendering where
# a fixup is performed with adjust_p4_to_standard() to deal with the B-string
# irregularity.

from typing import Iterable, NamedTuple


class Offset:
    """Offset on the fretboard."""

    def __init__(self, string: int = 0, fret: int = 0):
        self.string = string
        self.fret = fret

    def __add__(self, other: 'Offset') -> 'Offset':
        return Offset(self.string + other.string, self.fret + other.fret)


NEXT_STRING_OFFSET = Offset(string=1, fret=-5)
P4_OFFSET = Offset(string=1, fret=0)
P5_OFFSET = Offset(string=1, fret=2)
SINGLE_STRING_P5_OFFSET = Offset(fret=7)
OCTAVE_OFFSET = P4_OFFSET + P5_OFFSET


class Location(Offset):
    """A fretboard location.

    Strings are numbered 0-5, with 0 representing low E. Fret numbering starts
    at 0, with 0 representing an open string and 1 the first fretted note.
    """

    def __add__(self, other: 'Offset') -> 'Location':
        return Location(self.string + other.string, self.fret + other.fret)


class Marker(NamedTuple):
    """Fretboard marker."""

    location: Location
    label: str
    color: str


## fixup for standard tuning and top string linearization of the tetrachord
def adjust_p4_to_standard(markers: Iterable[Marker]) -> Iterable[Marker]:

    def fix_marker(m):
        # Linearize the final tetrachord as we've run out of additional strings
        if m.location.string > 5:
            return Marker(m.location + Offset(-1, 6), m.label, m.color)
        # B-string hiccup
        if m.location.string >= 4:
            return Marker(m.location + Offset(0, 1), m.label, m.color)
        return m

    return map(fix_marker, markers)


# Markers representing P1, P4 and P5 intervals immediately below a given location.
def perfect_interval_markers(location: Location):
    return [
        Marker(location, '1', 'black'),
        Marker(location + P4_OFFSET, '4', 'black'),
        Marker(location + P5_OFFSET, '5', 'black'),
    ]
