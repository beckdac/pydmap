import math
import random

import numpy as np

from .natural_lines import line, arc, rect, cubic_bezier

EPSILON = .0001
CELL_SIZE = 100

def grid_cell(ctx, xcell, ycell, squiggle_strength=5, rgba=(.7, .7, .7, .2), seed=None):
    min_x = xcell * CELL_SIZE
    min_y = ycell * CELL_SIZE
    mid_x = min_x + CELL_SIZE / 2.
    mid_y = min_y + CELL_SIZE / 2.
    max_x = xcell * CELL_SIZE + CELL_SIZE
    max_y = ycell * CELL_SIZE + CELL_SIZE

    ctx.set_source_rgba(rgba[0], rgba[1], rbga[2], rbga[3])
    if random.random() < .1:
        arc(ctx, mid_x, mid_y, 5, 0, 2 * math.pi - EPSILON)
    line(ctx, xi1, yi1, xi2, yi2, squiggle_strength=squiggle_strength, print_points=print_points, seed=seed)
    ctx.stroke()

def demo(ctx, height, width):
    a = 10
    w = 100
    ws = w * .9
    print_points = False
    random.seed()
    ctx.set_source_rgba(0, 0, 0, 1)
    rect(ctx, a, a, ws, ws, squiggle_strength=1, print_points=print_points)
    rect(ctx, a + w, a, ws, ws, squiggle_strength=2, print_points=print_points)
    rect(ctx, a + 2*w, a, ws, ws, squiggle_strength=5, print_points=print_points)
    rect(ctx, a + 3*w, a, ws, ws, squiggle_strength=7, print_points=print_points)
    rect(ctx, a + 4*w, a, ws, ws, squiggle_strength=10, print_points=print_points)
    ctx.stroke()

    arc(ctx, a + 2*w + w/2, 150, 30, 30 * math.pi/180., 240 * math.pi/180., squiggle_strength=1, n=20)
    arc(ctx, a + 3*w + w/2, 150, 30, 280 * math.pi/180., 300 * math.pi/180., squiggle_strength=1, n=20)
    arc(ctx, a + 4*w + w/2, 150, 40, 0 * math.pi/180., 359.99 * math.pi/180., squiggle_strength=10, n=80)

    cubic_bezier(ctx, 10,170, 40,60, 120,180, 200,140, squiggle_strength=1, n=50)
