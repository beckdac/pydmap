import cairo

def render_png(filename='pydmap.png', width=512, height=512, pixel_coordinates=True, draw_func=None):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    
    context = cairo.Context(surface)
    
    if pixel_coordinates:
        pass
    else:
        context.scale(width, height)
    
    # background is transparent black
    context.set_source_rgba(0., 0., 0., 0.)
    # background is white
    context.set_source_rgba(1., 1., 1., 1.)
    context.rectangle(0, 0, width, height)
    context.fill()
    context.stroke()

    if draw_func is not None:
        draw_func(context, width, height)
    
    surface.write_to_png(filename)
