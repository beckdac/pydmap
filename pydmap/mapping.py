import math
import random

import cairo
import numpy as np

from .natural_lines import line, arc
from .hatching import hatch_cell
from .grid import grid_cell
from .constants import CELL_SIZE


def demo(ctx, height, width):

    # draw the hatching to a surface
    hatch_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    hatch_ctx = cairo.Context(hatch_surface)
    hatch_ctx.set_source_rgba(0., 0., 0., 1.)
    for xcell in range(int(width / CELL_SIZE)):
        for ycell in range(int(height / CELL_SIZE)):
            hatch_cell(hatch_ctx, xcell, ycell)
    hatch_surface.write_to_png('hatching.png')

    #ctx.set_source_surface(hatch_surface, 0, 0)
    #ctx.arc(width/4., height/4., height/8., 0, 2.*math.pi)
    #ctx.clip()
    #ctx.paint()

    # draw the hatching to a surface
    grid_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    grid_ctx = cairo.Context(grid_surface)
    grid_ctx.set_source_rgba(0., 0., 0., 1.)
    for xcell in range(int(width / CELL_SIZE)):
        for ycell in range(int(height / CELL_SIZE)):
            grid_cell(grid_ctx, xcell, ycell)
    grid_surface.write_to_png('grid.png')

    ctx.set_source_surface(grid_surface, 0, 0)
    ctx.arc(width/4., height/2. + height/4., height/8., 0, 2.*math.pi)
    ctx.clip()
    ctx.paint()

    ctx.set_source_rgba(0, 0, 0, 1)
    arc(ctx, width/2., height/2., height/8., 9, 360.)
