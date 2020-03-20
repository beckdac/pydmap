import math
import random

import numpy as np

from .natural_lines import line
from .constants import CELL_SIZE


def stone(ctx, squiggle_strength=5, seed=None, print_points=False):
    ctx.save()

    ctx.stroke()
    ctx.restore()


def demo(ctx, height, width):
    print_points = False
    ctx.set_source_rgba(0, 0, 0, 1)
    ctx.line_to(CELL_SIZE / 2, CELL_SIZE / 2)
    stone(ctx)
