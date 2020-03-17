import math
import random

import numpy as np

from .natural_lines import line


CELL_SIZE = 100

def hatch_cell(ctx, xcell, ycell, lines_per_cell=5, squiggle_strength=5, seed=None, print_points=False):
    ctx.save()

    hatch_dir_x = xcell % 2
    hatch_dir_y = ycell % 2
    mid_x = xcell * CELL_SIZE + CELL_SIZE / 2
    mid_y = ycell * CELL_SIZE + CELL_SIZE / 2

    #ctx.translate(-mid_x, -mid_y)
    #ctx.rotate(45. * math.pi/180.)

    #line(ctx, mid_x, mid_y, 100, 100)

    for x in np.linspace(0., CELL_SIZE, lines_per_cell + 2)[1:-1]:
        xi = xcell * CELL_SIZE + x
        yi = ycell * CELL_SIZE
        xi1 = xi + random.random() * 10. + CELL_SIZE / 2 / 10.
        yi1 = yi + random.random() * 10. + CELL_SIZE / 10.
        xi2 = xi + random.random() * 10. - CELL_SIZE / 2/ 10.
        yi2 = yi + CELL_SIZE - random.random() * 10. - CELL_SIZE / 10.
        line(ctx, xi1, yi1, xi2, yi2, squiggle_strength=squiggle_strength, print_points=print_points, seed=seed)

    #ctx.translate(mid_x, mid_y)

    ctx.stroke()
    ctx.restore()


def demo(ctx, height, width):
    print_points = False
    ctx.set_source_rgba(0, 0, 0, 1)
    ctx.move_to(0, CELL_SIZE)
    ctx.line_to(200, CELL_SIZE)
    ctx.move_to(CELL_SIZE, 0)
    ctx.line_to(CELL_SIZE, 200)
    ctx.stroke()
    hatch_cell(ctx, 0, 0)
    #hatch_cell(ctx, 1, 1)
    #hatch_cell(ctx, 1, 2)
    #hatch_cell(ctx, 2, 1)
    #hatch_cell(ctx, 2, 2)
