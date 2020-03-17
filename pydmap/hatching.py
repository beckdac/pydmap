import math
import random

import numpy as np

from .natural_lines import line


def hatch_cell(ctx, xcell, ycell, lines_per_cell=5, squiggle_strength=5, seed=None, print_points=False):
    ctx.save()

    hatch_dir_x = xcell % 2
    hatch_dir_y = ycell % 2
    mid_x = xcell * 100 + 50
    mid_y = ycell * 100 + 50

    for x in np.linspace(0., 100., lines_per_cell + 2)[1:-1]:
        xi = xcell * 100. + x
        yi = ycell * 100.
        xi1 = xi + random.random() * 10. + 5.
        yi1 = yi + random.random() * 10. + 10.
        xi2 = xi + random.random() * 10. - 5.
        yi2 = yi + 100 - random.random() * 10. - 10.
        line(ctx, xi1, yi1, xi2, yi2, squiggle_strength=squiggle_strength, print_points=print_points, seed=seed)

    ctx.translate(-mid_x, -mid_y)
    ctx.rotate(-math.pi/4)
    ctx.translate(mid_x, mid_y)

    ctx.stroke()
    ctx.restore()


def demo(ctx, height, width):
    print_points = False
    ctx.set_source_rgba(0, 0, 0, 1)
    ctx.move_to(0, 100)
    ctx.line_to(200, 100)
    ctx.move_to(100, 0)
    ctx.line_to(100, 200)
    ctx.stroke()
    hatch_cell(ctx, 0, 0)
    #hatch_cell(ctx, 1, 1)
    #hatch_cell(ctx, 1, 2)
    #hatch_cell(ctx, 2, 1)
    #hatch_cell(ctx, 2, 2)
