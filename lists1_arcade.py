import arcade


WIDTH = 640
HEIGHT = 480

tree_x_location = [100, 125, 300, 350, 600]
tree_y_location = [200, 250, 130, 287, 379]

def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...



    # for x in tree_x_location:
    #     arcade.draw_circle_filled(x,350,50, arcade.color.ATOMIC_TANGERINE)


    # while loop with i
    # i = 0
    # while i < len(tree_x_location):
    #     x = tree_x_location[i]
    #     y = tree_y_location[i]
    #     arcade.draw_circle_filled(x, y, 50, arcade.color.ATOMIC_TANGERINE)
    #     i += 1

    #zip
    

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():


    print("SETUP")
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


if __name__ == '__main__':
    setup()
