def updateScoreboard():
    OLED.clear()
    OLED.write_string_new_line("P1: " + str(P1))
    OLED.new_line()
    OLED.write_string_new_line("P2: " + str(P2))
    OLED.new_line()
    OLED.write_string_new_line("Ties: " + str(Ties))
    OLED.new_line()
    OLED.write_string_new_line("Rounds: " + str(Rounds))

def on_gesture_shake():
    reset()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def reset():
    global Rounds, P2, P1, Ties
    OLED.init(128, 64)
    Rounds = 0
    P2 = 0
    P1 = 0
    Ties = 0
    OLED.write_string_new_line("shall we play a game?")
    basic.pause(2000)
    updateScoreboard()
Rounds = 0
Ties = 0
P2 = 0
P1 = 0
reset()