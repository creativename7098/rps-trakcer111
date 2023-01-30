input.onGesture(Gesture.Shake, function () {
    reset()
})
function reset () {
    OLED.init(128, 64)
    Rounds = 0
    P2 = 0
    P1 = 0
    Ties = 0
    OLED.writeStringNewLine("shall we play a game?")
    basic.pause(2000)
    OLED.clear()
    OLED.writeStringNewLine("P1: " + P1)
    OLED.newLine()
    OLED.writeStringNewLine("P2: " + P2)
    OLED.newLine()
    OLED.writeStringNewLine("Ties: " + Ties)
    OLED.newLine()
    OLED.writeStringNewLine("Rounds: " + Rounds)
}
let Ties = 0
let P1 = 0
let P2 = 0
let Rounds = 0
reset()
basic.forever(function () {
	
})
