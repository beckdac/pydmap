import random

from .draw import rect

def demo(ctx):
    a = 10
    w = 100
    ws = w * .9
    ctx.translate(520, 0);
    ctx.scale(-1, 1)
    print_points = False
    random.seed()
    rect(ctx, a, a, ws, ws, squiggle_strength=10, print_points=print_points);
    rect(ctx, a + w, a, ws, ws, squiggle_strength=7, print_points=print_points);
    rect(ctx, a + 2*w, a, ws, ws, squiggle_strength=5, print_points=print_points);
    rect(ctx, a + 3*w, a, ws, ws, squiggle_strength=2, print_points=print_points);
    rect(ctx, a + 4*w, a, ws, ws, squiggle_strength=1, print_points=print_points);
