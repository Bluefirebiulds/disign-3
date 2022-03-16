def on_button_pressed_a():
    basic.show_string("hi cambell the groner")
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_string("Hello!")
basic.show_string("i'm gardian scout mark 9193")
soundExpression.hello.play_until_done()
basic.show_icon(IconNames.HAPPY)
basic.pause(100)
basic.show_leds("""
    . . . . .
        . # # # .
        . # # # .
        . . # . .
        . . # . .
""")