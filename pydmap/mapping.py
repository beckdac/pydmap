import math
import random

import cairo
import numpy as np
from sympy.geometry import Point2D

from .natural_lines import line, arc
from .hatching import hatch_cell
from .grid import grid_cell
from . import natural_lines
from . import hatching
from . import grid
from .constants import CELL_SIZE


class Room:

    def __init__(self, name, loc, flags=[]):
        self.name = name
        self.loc = loc
        assert isinstance(self.loc, Point2D)
        self.flags = flags

    def __repr__(self):
        return f"<Room name:{self.name}, loc:({self.loc.x}, {self.loc.y}), flags:{self.flags}>"


class Path:

    def __init__(self, room_name_1, room_name_2, flags=[]):
        self.room_name_1 = room_name_1
        self.room_name_2 = room_name_2
        self.flags = flags

    def __repr__(self):
        return f"<Path room_1:{self.room_name_1} room_2:{self.room_name_2} flags:{self.flags}>"

        
class Map:

    def __init__(self, name, width, height, cell_size=CELL_SIZE):
        self.name = name
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.rooms = {}
        self.pathes = []

    def __repr__(self):
        return f"<Map name:{self.name} width:{self.width} height:{self.height} has {len(self.rooms)} rooms and {len(self.pathes)} pathes>"
    
    def has_room(self, room_name):
        if room_name in self.rooms:
            return True
        else:
            return False
   
    def add_room(self, room):
        self.rooms[room.name] = room

    def remove_room(self, room_name):
        self.rooms.pop(room_name)

    def has_path(self, room_name_1, room_name_2):
        assert self.has_room(room_name_1)
        assert self.has_room(room_name_2)
        for path in self.pathes:
            if ((path.room_name_1 == room_name_1 and path.room_name_2 == room_name_2) or \
                (path.room_name_2 == room_name_2 and path.room_name_1 == room_name_1)):
                        return True
            else:
                pass
        return False

    def add_path(self, room_name_1, room_name_2, flags=[]):
        assert not self.has_path(room_name_1, room_name_2)
        self.pathes.append(Path(room_name_1, room_name_2, flags))

    def draw(self, context):
        for room in self.rooms:
            print(self.rooms[room])
        for path in self.pathes:
            print(path)


def demo(ctx, width, height):
    map = Map('demo', width, height, cell_size=CELL_SIZE)
    map.add_room(Room('start', Point2D(width/4, height/4)))
    map.add_room(Room('mid1', Point2D(width/2 + width/4, height/2)))
    map.add_room(Room('mid2', Point2D(width/2, height/2 + height /4)))
    map.add_room(Room('end', Point2D(width/2 + width/4, height/2 + height/4)))
    map.add_path('start', 'mid1', flags=['arc'])
    map.add_path('start', 'mid2', flags=['door', 'trapped'])
    map.add_path('mid1', 'end', flags=['door'])
    print(map)
    map.draw(ctx)

def old_demo(ctx, width, height):
    circ_radius = CELL_SIZE * 3
    xc = width / 2
    yc = height / 2
    hatch_cells = 2.3 * CELL_SIZE
    hallway_extension = 2 * CELL_SIZE

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

    room_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    room_ctx = cairo.Context(room_surface)
    room_ctx.set_source_rgba(0, 0, 0, 1)
    room_ctx.set_line_width(CELL_SIZE)
    room_ctx.move_to(width/2, height/2 + circ_radius + hallway_extension)
    room_ctx.line_to(width/2, height/2 - circ_radius - hallway_extension)
    room_ctx.move_to(width/2 + circ_radius + hallway_extension, height/2)
    room_ctx.line_to(width/2 - circ_radius - hallway_extension, height/2)
    room_ctx.stroke()
    room_ctx.arc(width/2, height/2, circ_radius, 0, 2*math.pi)
    room_ctx.fill()
    room_surface.write_to_png('room.png')
    # apply mask
    ctx.set_operator(cairo.OPERATOR_DEST_OUT)
    ctx.set_source_surface(room_surface, 0, 0)
    ctx.paint()

    #ctx.identity_matrix()
    #ctx.set_source_surface(room_surface, 0, 0)
    #ctx.paint()
