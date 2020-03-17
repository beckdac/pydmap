#!/usr/bin/env python

import pydmap
from pydmap import hatching, natural_lines


def main():
    width = 600
    height = 200
    pydmap.render_png(filename='demo.png', width=width, height=height, draw_func=hatching.demo)
    pydmap.render_png(filename='demo.png', width=width, height=height, draw_func=natural_lines.demo)

if __name__== "__main__":
  main()
