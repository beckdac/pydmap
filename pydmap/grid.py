import math
import random

import numpy as np

from .natural_lines import line, arc, rect, cubic_bezier
from .constants import CELL_SIZE, EPSILON, MAX_DELTA, CENTER_DOT_FRAC

def grid_cell(ctx, xcell, ycell, squiggle_strength=5, rgba=(.7, .7, .7, .15), seed=None):
    min_x = xcell * CELL_SIZE
    min_y = ycell * CELL_SIZE
    mid_x = min_x + CELL_SIZE / 2.
    mid_y = min_y + CELL_SIZE / 2.
    max_x = xcell * CELL_SIZE + CELL_SIZE
    max_y = ycell * CELL_SIZE + CELL_SIZE

    ctx.set_source_rgba(rgba[0], rgba[1], rgba[2], rgba[3])

    # draw a bottom left dot on a random chance
    if random.random() < CENTER_DOT_FRAC:
        arc(ctx, max_x, max_y, 1, 0, 2 * math.pi - EPSILON)

    # draw cell divider lines on +1, +1
    grid_cell_line(ctx, max_x, max_y, min_x, max_y)
    grid_cell_line(ctx, max_x, max_y, max_x, min_y)

def split_line(ctx, x1, y1, x2, y2, fraction):
    start_x_delta = random.random() * MAX_DELTA
    start_y_delta = random.random() * MAX_DELTA
    start_x = x1 + start_x_delta * (x2 - x1)
    start_y = y1 + start_y_delta * (y2 - y1)
    break_x_delta = random.random() * MAX_DELTA
    break_y_delta = random.random() * MAX_DELTA
    break_xm = x2 - break_x_delta * (x2 - x1)
    break_ym = y2 - break_y_delta * (y2 - y1)
    break_xp = x1 + break_x_delta * (x2 - x1)
    break_yp = y1 + break_y_delta * (y2 - y1)
    end_x_delta = random.random() * MAX_DELTA
    end_y_delta = random.random() * MAX_DELTA
    end_x = x2 - end_x_delta * (x2 - x1)
    end_y = y2 - end_y_delta * (y2 - y1)
    line(ctx, start_x, start_y, break_xm, break_ym)
    line(ctx, break_xp, break_yp, end_x, end_y)

def grid_cell_line(ctx, x1, y1, x2, y2):
    split_line(ctx, x1, y1, x2, y2, fraction = random.random())
    ctx.stroke()

def demo(ctx, width, height):
    random.seed()
    for i in range(int(width / CELL_SIZE)):
        for j in range(int(height / CELL_SIZE)):
            grid_cell(ctx, i, j, squiggle_strength=5)
