import random

from .draw import rect, cubic_bezier

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

    cubic_bezier(ctx, 116,10, 10,40, 30,160, 150,110)
    ctx.stroke()
