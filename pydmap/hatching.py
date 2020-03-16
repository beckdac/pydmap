import random

import numpy as np

from .natural_lines import line


def hatch_cell(ctx, xcell, ycell, strength=5, seed=None, print_points=False):
    hatch_dir_x = xcell % 2
    hatch_dir_y = ycell % 2

    #ctx.translate(xcell * 100., ycell * 100.)
    #ctx.new_path()
    i = 0
    for x in np.linspace(0., 100., 6):
        if i == 0 or i == 5:
            i = i + 1
            continue
        else:
            pass
        xi = xcell * 100. + x
        yi = ycell * 100.
        xi1 = xi + random.random() * 10. - 5.
        yi1 = yi + random.random() * 10. - 10.
        xi2 = xi + random.random() * 10. - 5.
        yi2 = yi + 100 - random.random() * 10. - 10.
        #print(f"{xi1}, {yi1} -> {xi2}, {yi2}")
        if i % 2 == 0:
            line(ctx, xi1, yi1, xi2, yi2, squiggle_strength=strength, print_points=print_points, seed=seed)
        else:
            line(ctx, xi2, yi2, xi1, yi1, squiggle_strength=strength, print_points=print_points, seed=seed)

    #ctx.rotate(xcell * 180. + ycell * 90.)
    ctx.stroke()

def demo(ctx, height, width):
    print_points = False
    ctx.set_source_rgba(0, 0, 0, 1)
    hatch_cell(ctx, 0, 0)
    #hatch_cell(ctx, 1, 1)
    #hatch_cell(ctx, 1, 2)
    #hatch_cell(ctx, 2, 1)
    #hatch_cell(ctx, 2, 2)
