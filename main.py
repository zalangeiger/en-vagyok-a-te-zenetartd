def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_button_pressed_ab():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_left():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

basic.show_string("en vagyok a te zenetartod")