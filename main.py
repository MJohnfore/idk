num = 9
start = False

def on_button_pressed_a():
    global start
    start = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global start
    start = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if start:
        global num
        basic.show_number(num)
        basic.pause(500)
        num -= 1
        if num = 0:
            basic.show_string("DONE")
basic.forever(on_forever)


