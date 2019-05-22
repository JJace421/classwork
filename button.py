import arcade


WIDTH = 640
HEIGHT = 480

#           x   y   w   h   color                           click color
button1 = [185,240,250,50,arcade.color.ORIOLES_ORANGE,arcade.color.ATOMIC_TANGERINE,False]
button2 = [185,140,250,50,arcade.color.PEARL_AQUA,arcade.color.NAVY_BLUE,False]
button3 = [185,340,250,50,arcade.color.VIOLET,arcade.color.LAVENDER,False]
button4 = [185,40,250,50,arcade.color.PALE_PINK,arcade.color.PARADISE_PINK,False]



btn_x = 0
btn_y = 1
btn_w = 2
btn_h = 3
btn_c = 4
btn_cc = 5
clicks = 6


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
    draw_button(button1)
    draw_button(button2)
    draw_button(button3)
    draw_button(button4)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global clicks

    print(f"Clicked at ({x}, {y}).")

    if is_clicked(x,y,button1):
        button1[clicks] = True

    if is_clicked(x,y,button2):
        button2[clicks] = True

    if is_clicked(x,y,button3):
        button3[clicks] = True

    if is_clicked(x,y,button4):
        button4[clicks] = True



def on_mouse_release(x, y, button, modifiers):
    global clicks

    button1[clicks] = False
    button2[clicks] = False
    button3[clicks] = False
    button4[clicks] = False


def draw_button(button):
    global clicks

    if button[clicks] == True:
        color = button[btn_c]
    else:
        color = button[btn_cc]

    #Draw button
    arcade.draw_xywh_rectangle_filled(
        button[btn_x],
        button[btn_y],
        button[btn_w],
        button[btn_h],
        color)

def is_clicked(x,y,button):

    if (x > button[btn_x] and x < button[btn_x] + button[btn_w] and
        y > button[btn_y] and y < button[btn_y] + button[btn_h]):
        print("Button clicked")
        return True
    else:
        return False

if __name__ == '__main__':
    setup()


