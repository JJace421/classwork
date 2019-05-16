import random
import arcade


WIDTH = 640
HEIGHT = 480

# rain_x_positions = [100, 150 ,223, 300, 376, 478, 534, 597, 606]
# rain_y_positions = [464, 480, 472, 447, 483, 468, 473, 490, 500]

rain_x_positions = []
rain_y_positions = []

for i in range(30):
    x = random.randrange(0, WIDTH)
    y = random.randrange(475, 675)
    rain_x_positions.append(x)
    rain_y_positions.append(y)

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
    for index in range(len(rain_y_positions)):
        rain_y_positions[index] -= 3
        if rain_y_positions[index] < 0:
            rain_y_positions[index] = random.randrange(475, 675)
            rain_x_positions[index] = random.randrange(0, WIDTH)



def on_draw():
    arcade.start_render()
    # Draw in here...
    radius = 10

    for x, y in zip(rain_x_positions, rain_y_positions):
        arcade.draw_circle_filled(x, y, radius, arcade.color.BABY_BLUE_EYES)
        arcade.draw_triangle_filled(x-radius,y,x+radius,y,x,y+20, arcade.color.BABY_BLUE_EYES)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
