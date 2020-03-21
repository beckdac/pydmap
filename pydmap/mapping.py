import math
import random

import cairo
import numpy as np

from .natural_lines import line, arc
from .hatching import hatch_cell
from .grid import grid_cell
from . import natural_lines
from . import hatching
from . import grid
from .constants import CELL_SIZE


def demo(ctx, width, height):
    circ_radius = CELL_SIZE * 3
    xc = width / 2
    yc = height / 2
    hatch_cells = 2.3 * CELL_SIZE

    # draw the hatching to a surface
    hatch_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    hatch_ctx = cairo.Context(hatch_surface)
    hatch_ctx.set_source_rgba(0., 0., 0., 1.)
    for xcell in range(int(width / CELL_SIZE)):
        for ycell in range(int(height / CELL_SIZE)):
            hatch_cell(hatch_ctx, xcell, ycell)
    hatch_surface.write_to_png('hatching.png')

    ctx.save()
    ctx.set_source_surface(hatch_surface, 0, 0)
    fade = cairo.RadialGradient(xc, yc, 0, xc, yc, circ_radius + hatch_cells)
    fade.add_color_stop_rgba(0, 0, 0, 0, 0);
    fade.add_color_stop_rgba(circ_radius / (circ_radius + hatch_cells), 0, 0, 0, 0);
    fade.add_color_stop_rgba(circ_radius / (circ_radius + hatch_cells), 0, 0, 0, 1);
    fade.add_color_stop_rgba(1, 0, 0, 0, 0);
    ctx.mask(fade)
    ctx.restore()

    # draw the grid to a surface
    grid_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    grid_ctx = cairo.Context(grid_surface)
    grid_ctx.set_source_rgba(0., 0., 0., 1.)
    for xcell in range(int(width / CELL_SIZE)):
        for ycell in range(int(height / CELL_SIZE)):
            grid_cell(grid_ctx, xcell, ycell)
    grid_surface.write_to_png('grid.png')

    ctx.save()
    ctx.set_source_surface(grid_surface, 0, 0)
    ctx.arc(xc, yc, circ_radius, 0, 2.*math.pi)
    ctx.clip()
    ctx.paint()
    ctx.restore()

    ctx.save()
    ctx.set_line_width(3)
    natural_lines.demo(ctx, width, height)
    ctx.restore()

    ctx.save()
    ctx.set_line_width(5)
    ctx.set_source_rgba(0, 0, 0, 1)
    arc(ctx, xc, yc, circ_radius, 0, 2.*math.pi, segments=72, n=3)
    ctx.restore()

    hallway_mask_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    hallway_mask_ctx = cairo.Context(hallway_mask_surface)
    hallway_mask_ctx.set_source_rgba(0, 0, 0, 1)
    hallway_mask_ctx.set_line_width(100)
    # unfinished
