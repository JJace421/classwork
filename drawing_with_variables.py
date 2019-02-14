import arcade


WIDTH = 640
HEIGHT = 480

x = int(input('x = '))
y = int(input('y = '))
radius = int(input('radius = '))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.PASTEL_PINK)

# End drawing
arcade.finish_render()
arcade.run()