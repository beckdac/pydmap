#!/usr/bin/env python

import pydmap
from pydmap import hatching

def main():
    width = 200
    height = 200
    pydmap.render_png(filename='demo.png', width=width, height=height, draw_func=hatching.demo)

if __name__== "__main__":
  main()
