"""Render guitar fretboard scale diagrams derived from tetrachords."""
from scales import *

import fretboard

# python-fretboard style for 3-octave scales.
SCALE_STYLE = {
    'drawing': {
        'orientation': 'landscape',
        'width': 1200,
    },
    'marker': {
        'radius': 15
    },
}

# python-fretboard style for tetrachord shape diagrams.
TETRACHORD_STYLE = {
    'drawing': {
        'orientation': 'portrait',
        'width': 200,
        'height': 400
    },
    'marker': {
        'radius': 12
    },
}


def render_tetrachord_with_markers(filename, markers):
    fb = fretboard.Fretboard(frets=(1, 10), strings=6, style=TETRACHORD_STYLE)
    for marker in markers:
        fb.add_marker(string=marker.location.string,
                      fret=marker.location.fret,
                      label=marker.label,
                      color=marker.color)
    fb.save(f'svg/{filename}.svg')


def render_scale_with_markers(filename, markers):
    fb = fretboard.Fretboard(frets=(1, 15), style=SCALE_STYLE)
    for marker in adjust_p4_to_standard(markers):
        fb.add_marker(string=marker.location.string,
                      fret=marker.location.fret,
                      label=marker.label,
                      color=marker.color)
    fb.save(f'svg/{filename}.svg')


def render_tetrachord(tetrachord):
    location = Location(0, 5)
    for shape in Shape:
        markers = tetrachord.markers(location, shape)
        render_tetrachord_with_markers(
            f'tetrachord-{shape.name}-{tetrachord.name.lower()}', markers)


# TODO: make this less verbose
def render_perfect_intervals():
    location = Location(0, 3)
    markers = perfect_interval_markers(location)
    render_scale_with_markers('perfect-intervals-two', markers)
    location += OCTAVE_OFFSET
    markers.extend(perfect_interval_markers(location))
    render_scale_with_markers('perfect-intervals-four', markers)
    location += OCTAVE_OFFSET
    markers.extend(perfect_interval_markers(location))
    location += OCTAVE_OFFSET
    markers.extend(perfect_interval_markers(location))
    render_scale_with_markers('perfect-intervals-six', markers)


def render_single_string(scale):
    location = Location(0, 3)
    markers = scale.single_string_markers(location)
    render_scale_with_markers('singlestring-' + scale.simple_name, markers)


def render_three_two_r_major():
    location = Location(0, 3)
    markers = MAJOR_SCALE.lower_tetrachord.markers(location, Shape.R)
    render_scale_with_markers('threetwo-R-major-one', markers)
    location += P5_OFFSET
    markers.extend(MAJOR_SCALE.upper_tetrachord.markers(location, Shape.R))
    render_scale_with_markers('threetwo-R-major-two', markers)
    location += P4_OFFSET
    markers.extend(MAJOR_SCALE.two_string_markers(location, Shape.R, Shape.R))
    location += OCTAVE_OFFSET
    markers.extend(MAJOR_SCALE.two_string_markers(location, Shape.R, Shape.R))
    render_scale_with_markers('threetwo-R-major-six', markers)


def render_three_two_r(scale):
    location = Location(0, 3)
    markers = []
    for n in range(3):
        markers.extend(scale.two_string_markers(location, Shape.R, Shape.R))
        location += OCTAVE_OFFSET
    render_scale_with_markers('threetwo-R-' + scale.simple_name, markers)


def render_three_two_optimized(scale):
    location = Location(0, 3)
    markers = []
    for n in range(3):
        markers.extend(scale.two_string_optimal_markers(location))
        location += OCTAVE_OFFSET
    render_scale_with_markers(
        'threetwo-opt-' + scale.name.lower().replace(' ', '-'), markers)


# Generate all SVG diagrams.
if __name__ == '__main__':
    for tetrachord in LOWER_TETRACHORDS:
        render_tetrachord(tetrachord)

    for scale in SCALES:
        render_single_string(scale)
        render_three_two_r(scale)
        render_three_two_optimized(scale)

    render_perfect_intervals()
    render_three_two_r_major()
