from machine import Pin, Timer

led = Pin(25, Pin.OUT)  # built-in LED

def toggle_led(timer):
    led.toggle()

# Create a timer that toggles the LED every 500 milliseconds (0.5 seconds)
timer = Timer()
timer.init(freq=2, mode=Timer.PERIODIC, callback=toggle_led)

while True:
    pass 
