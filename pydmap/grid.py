import math
import random

import numpy as np

from .natural_lines import line, arc, rect, cubic_bezier
from .constants import CELL_SIZE, EPSILON

def grid_cell(ctx, xcell, ycell, squiggle_strength=5, rgba=(.7, .7, .7, .2), seed=None):
    min_x = xcell * CELL_SIZE
    min_y = ycell * CELL_SIZE
    mid_x = min_x + CELL_SIZE / 2.
    mid_y = min_y + CELL_SIZE / 2.
    max_x = xcell * CELL_SIZE + CELL_SIZE
    max_y = ycell * CELL_SIZE + CELL_SIZE

    ctx.set_source_rgba(rgba[0], rgba[1], rgba[2], rgba[3])

    # draw a bottom left dot on a random chance
    if random.random() < .2:
        arc(ctx, max_x, max_y, 1, 0, 2 * math.pi - EPSILON)

    # draw cell divider lines on +1, +1
    grid_cell_line(ctx, max_x, max_y, min_x, max_y)
    grid_cell_line(ctx, max_x, max_y, max_x, min_y)

def grid_cell_line(ctx, x1, y1, x2, y2):
    rand = random.random()

    # need a function that trims down a line segment fromm the ends out
    if rand < .25:
        # split in half
    elif rand < .5:
        # spit in thirds
    elif rand < .75:
        # single line
        line(ctx, x1, y1, x2, y2)
    else:
    ctx.stroke()

def demo(ctx, width, height):
    random.seed()
    for i in range(int(width / CELL_SIZE)):
        for j in range(int(height / CELL_SIZE)):
            grid_cell(ctx, i, j, squiggle_strength=5)
