import arcade


WIDTH = 640
HEIGHT = 480


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    for x in range(0, WIDTH, 75):
        draw_face(x, 300)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass

def draw_face(x,y):

    #Face
    arcade.draw_ellipse_filled(x, y, 125, 150, arcade.color.YELLOW_ROSE)
    arcade.draw_ellipse_outline(x, y, 125, 150, arcade.color.BRONZE_YELLOW, 2)
    #Eye
    arcade.draw_circle_filled(x - 50, y + 40,25,arcade.color.WHITE)
    arcade.draw_ellipse_filled(x- 50, y + 30,15,15,arcade.color.PEARL_AQUA)

    arcade.draw_circle_filled(x + 50, y + 40,25,arcade.color.WHITE)
    arcade.draw_ellipse_filled(x + 50, y + 30,15,15,arcade.color.PEARL_AQUA)

    #Mouth
    arcade.draw_ellipse_filled(x, y - 50,25,30, arcade.color.BLACK_BEAN)


if __name__ == '__main__':
    setup()
