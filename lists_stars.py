import random
import arcade


WIDTH = 640
HEIGHT = 480

stars_x_locations = []
stars_y_locations = []


for i in range(100):
    x = random.randrange(-40, WIDTH + 40, 15)
    y = random.randrange(0,HEIGHT, 15)
    stars_x_locations.append(x)
    stars_y_locations.append(y)


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.NAVY_BLUE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    for index in range(len(stars_x_locations)):
        stars_x_locations[index] += 2
        if stars_x_locations[index] == (WIDTH + 40):
            stars_x_locations[index] = random.randrange(-40,0,15)
            stars_y_locations[index] = random.randrange(5,HEIGHT,15)



def on_draw():
    arcade.start_render()

    radius = 3
    tip = 7

    for x, y in zip(stars_x_locations,stars_y_locations):
        arcade.draw_circle_filled(x, y, radius, arcade.color.PASTEL_YELLOW)
        arcade.draw_triangle_filled(x - radius, y, x + radius, y, x, y + tip, arcade.color.PASTEL_YELLOW)  # top of star
        arcade.draw_triangle_filled(x - radius, y, x + radius, y, x, y - tip, arcade.color.PASTEL_YELLOW)  # bottom of star
        arcade.draw_triangle_filled(x, y - radius, x, y + radius, x - tip, y, arcade.color.PASTEL_YELLOW)  # left of star
        arcade.draw_triangle_filled(x, y - radius, x, y + radius, x + tip, y, arcade.color.PASTEL_YELLOW)  # right of star


def on_key_press(key, modifiers):
    pass

def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
