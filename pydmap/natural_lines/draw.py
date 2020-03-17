import math
import random

import numpy as np
def quad_to(ctx, x1, y1, x2, y2):
    x0, y0 = ctx.get_current_point()

    c1x = (x0 + 2.*x1) / 3.
    c1y = (y0 + 2.*y1) / 3.
    c2x = (x2 + 2.*x1) / 3.
    c2y = (y2 + 2.*y1) / 3.

    ctx.curve_to(c1x, c1y, c2x, c2y, x2, y2)

def time_to_point(sx, sy, fx, fy, t):
    # scale the time value, which should be between 0 and 2, to 0 and 1
    tau = t / 2.0
    poly_term = 15. * math.pow(tau, 4.) \
              - 6. * math.pow(tau, 5.) \
              - 10. * math.pow(tau, 3.)

    return {"x": sx + (sx - fx) * poly_term,
            "y": sy + (sy - fy) * poly_term }

def get_squiggle(prev, current, strength=5., seed=None):
    # find the midpoint
    midpoint = {"x": (prev["x"] + current["x"]) / 2., \
                      "y": (prev["y"] + current["y"]) / 2.};

    # displace by a random value between -5 and 5
    # the paper calls to do this w.r.t. the normal of the line
    # but we'll just do it on the circle.
    if seed is not None:
        random.seed(seed)
    def rng():
        return random.random()

    range_adjust = strength / 2.
    displacementX = rng() * strength - range_adjust;
    displacementY = rng() * strength - range_adjust;

    midpoint["x"] += displacementX;
    midpoint["y"] += displacementY;

    #print(f"{midpoint['x']}, {midpoint['y']}")

    return midpoint;

def line(ctx, sx, sy, fx, fy, squiggle_strength=10., seed=None, print_points=False):

    dist = math.sqrt(math.pow(sx - fx, 2) + math.pow(sy - fy, 2));
    if dist < 200:
        dt = 0.5
    elif dist < 400:
        dt = 0.3
    else:
        dt = 0.2

    last_point = {"x": sx, "y": sy}
    ctx.new_path()
    ctx.move_to(last_point["x"], last_point["y"])

    #print(f"last.x = {last_point['x']}, last.y = {last_point['y']}")
    for t in np.linspace(0, 2., int(2. / dt) + 1):
        current_point = time_to_point(sx, sy, fx, fy, t)
        squiggle_control_point = get_squiggle(last_point, current_point, strength=squiggle_strength, seed=seed)
        quad_to(ctx, squiggle_control_point["x"], squiggle_control_point["y"], current_point["x"], current_point["y"])

        if print_points:
            print(f"current.x = {current_point['x']}, current.y = {current_point['y']}")
            print(f"squiggle.x = {squiggle_control_point['x']}, squiggle.y = {squiggle_control_point['y']}")

        last_point = current_point;

    ctx.stroke()

def rect(ctx, x, y, w, h, squiggle_strength=5., seed=None, print_points=False):
    line(ctx, x,     y    , x + w, y    , squiggle_strength=squiggle_strength, seed=seed, print_points=print_points)
    line(ctx, x + w, y    , x + w, y + h, squiggle_strength=squiggle_strength, seed=seed, print_points=print_points)
    line(ctx, x + w, y + h, x    , y + h, squiggle_strength=squiggle_strength, seed=seed, print_points=print_points)
    line(ctx, x    , y + h, x    , y    , squiggle_strength=squiggle_strength, seed=seed, print_points=print_points)

def arc(ctx, xc, yc, radius, angle1, angle2):
    while angle2 < angle1:
        angle2 += 2. * math.pi

def cubic_bezier(ctx, x0, y0, x1, y1, x2, y2, x3, y3, n=10):
    for i in range(n+1):
        t = i / n
        a = (1. - t)**3
        b = 3. * t * (1. - t)**2
        c = 3.0 * t**2 * (1.0 - t)
        d = t**3

        x = int(a * x0 + b * x1 + c * x2 + d * x3)
        y = int(a * y0 + b * y1 + c * y2 + d * y3)

        line(ctx, x0, y0, x1, y1)
