let num = 9
let start = false
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    start = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    start = false
})
basic.forever(function on_forever() {
    if (start) {
        
        basic.showNumber(num)
        basic.pause(500)
        num -= 1
    }
    
})
