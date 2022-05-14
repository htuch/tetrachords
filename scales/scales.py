from tetrachords import *


class Scale:

    def __init__(self, name: str, lower_tetrachord: LowerTetrachord,
                 upper_tetrachord: UpperTetrachord, lower_optimal_shape: Shape,
                 upper_optimal_shape: Shape):
        self.name = name
        self.lower_tetrachord = lower_tetrachord
        self.upper_tetrachord = upper_tetrachord
        self.lower_optimal_shape = lower_optimal_shape
        self.upper_optimal_shape = upper_optimal_shape

    def single_string_markers(self, location: Location) -> list[Marker]:
        lower_markers = self.lower_tetrachord.markers(location, Shape.I)
        upper_markers = self.upper_tetrachord.markers(
            location + SINGLE_STRING_P5_OFFSET, Shape.I)
        return lower_markers + upper_markers

    def two_string_markers(self, location: Location, lower_shape: Shape,
                           upper_shape: Shape) -> list[Marker]:
        lower_markers = self.lower_tetrachord.markers(location, lower_shape)
        upper_markers = self.upper_tetrachord.markers(location + P5_OFFSET,
                                                      upper_shape)
        return lower_markers + upper_markers

    def two_string_optimal_markers(self, location: Location) -> list[Marker]:
        return self.two_string_markers(location, self.lower_optimal_shape,
                                       self.upper_optimal_shape)

    @property
    def simple_name(self):
        return self.name.lower().replace(' ', '-')


MAJOR_SCALE = Scale('Major', LOWER_MAJOR_TETRACHORD, UPPER_MAJOR_TETRACHORD,
                    Shape.Z, Shape.J)
MIXOLYDIAN_SCALE = Scale('Mixolydian', LOWER_MAJOR_TETRACHORD,
                         UPPER_MINOR_TETRACHORD, Shape.Z, Shape.J)
NATURAL_MINOR_SCALE = Scale('Natural minor', LOWER_MINOR_TETRACHORD,
                            UPPER_PHRYGIAN_TETRACHORD, Shape.R, Shape.Z)
HARMONIC_MINOR_SCALE = Scale('Harmonic minor', LOWER_MINOR_TETRACHORD,
                             UPPER_HARMONIC_TETRACHORD, Shape.R, Shape.Z)
MELODIC_MINOR_SCALE = Scale('Melodic minor', LOWER_MINOR_TETRACHORD,
                            UPPER_MAJOR_TETRACHORD, Shape.R, Shape.Z)
DORIAN_SCALE = Scale('Dorian', LOWER_MINOR_TETRACHORD, UPPER_MINOR_TETRACHORD,
                     Shape.R, Shape.R)
PHRYGIAN_SCALE = Scale('Phrygian', LOWER_PHRYGIAN_TETRACHORD,
                       UPPER_PHRYGIAN_TETRACHORD, Shape.R, Shape.Z)
PHRYGIAN_DOMINANT_SCALE = Scale('Phrygian dominant', LOWER_HARMONIC_TETRACHORD,
                                UPPER_PHRYGIAN_TETRACHORD, Shape.Z, Shape.Z)
NEAPOLITAN_MINOR_SCALE = Scale('Neapolitan minor', LOWER_PHRYGIAN_TETRACHORD,
                               UPPER_HARMONIC_TETRACHORD, Shape.R, Shape.Z)
DOUBLE_HARMONIC_SCALE = Scale('Double harmonic', LOWER_HARMONIC_TETRACHORD,
                              UPPER_HARMONIC_TETRACHORD, Shape.Z, Shape.Z)

SCALES = [
    MAJOR_SCALE,
    MIXOLYDIAN_SCALE,
    NATURAL_MINOR_SCALE,
    HARMONIC_MINOR_SCALE,
    MELODIC_MINOR_SCALE,
    DORIAN_SCALE,
    PHRYGIAN_SCALE,
    PHRYGIAN_DOMINANT_SCALE,
    NEAPOLITAN_MINOR_SCALE,
    DOUBLE_HARMONIC_SCALE,
]
