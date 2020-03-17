import math
import random

from .draw import rect, cubic_bezier, arc

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
