



import arcade


WIDTH = 640
HEIGHT = 480

#           x   y   w   h   color                           click color
button1 = [185,240,250,50,arcade.color.ATOMIC_TANGERINE, arcade.color.ORIOLES_ORANGE]
btn_x = 0
btn_y = 1
btn_w = 2
btn_h = 3
btn_c = 4
btn_cc = 5

clicks = 0

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
    window.on_mouse_release = on_mouse_release

    arcade.run()


def update(delta_time):
    pass

def on_draw():
    arcade.start_render()
    # Draw in here...

    if clicks % 2 == 0:
        color = button1[btn_c]
    else:
        color = button1[btn_cc]

    arcade.draw_xywh_rectangle_filled(
        button1[btn_x],
        button1[btn_y],
        button1[btn_w],
        button1[btn_h],
        color)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global clicks

    print(f"Clicked at ({x}, {y}).")
    if (x > button1[btn_x] and x < button1[btn_x] + button1[btn_w] and
        y > button1[btn_y] and y < button1[btn_y] + button1[btn_h]):
        print("Button clicked")
        clicks += 1

def on_mouse_release(x, y, button, modifiers):
    global clicks

    clicks -= 1


if __name__ == '__main__':
    setup()


