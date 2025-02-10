from machine import Pin, ADC, PWM
from utime import sleep_us, sleep

# Buttons
button1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(1, Pin.IN, Pin.PULL_DOWN)

# LED
led_red = PWM(Pin(2))
led_green = PWM(Pin(3))
led_blue = PWM(Pin(4))

# Limit Switches
limit_switch1 = Pin(5, Pin.IN, Pin.PULL_UP)
limit_switch2 = Pin(6, Pin.IN, Pin.PULL_UP)

# Stepper Motor
motor_pul = Pin(7, Pin.OUT)
motor_dir = Pin(8, Pin.OUT)
motor_ena = Pin(9, Pin.OUT)

# Potentiometer
potentiometer = ADC(28)

# PWM Frequency Setup
led_red.freq(1000)
led_green.freq(1000)
led_blue.freq(1000)
motor_pul.freq(500)

# LED Control Function
def set_led_color(r, g, b):
    led_red.duty_u16(r * 65535 // 255)
    led_green.duty_u16(g * 65535 // 255)
    led_blue.duty_u16(b * 65535 // 255)

# Motor Control
def motor_control(direction, speed):
    motor_dir.value(direction)
    motor_ena.value(0)  # Enable motor
    while True:
        if limit_switch1.value() == 0 or limit_switch2.value() == 0:
            break  # Stop if limit switch is hit
        motor_pul.value(1)
        sleep_us(speed)
        motor_pul.value(0)
        sleep_us(speed)
    motor_ena.value(1)  # Disable motor

# Button 1 LED Cycling
led_state = 0  # 0 = OFF, 1 = RED, 2 = GREEN, 3 = BLUE

def cycle_led():
    global led_state
    led_state = (led_state + 1) % 4  # Cycle through 0, 1, 2, 3
    if led_state == 0:
        set_led_color(0, 0, 0)  # OFF
    elif led_state == 1:
        set_led_color(255, 0, 0)  # RED
    elif led_state == 2:
        set_led_color(0, 255, 0)  # GREEN
    elif led_state == 3:
        set_led_color(0, 0, 255)  # BLUE

# Toggle for Button 2 (Motor Start/Stop)
motor_running = False

def toggle_motor():
    global motor_running
    motor_running = not motor_running  # Toggle state

# Main Loop
while True:
    # Check Limit Switches for LED Control
    if limit_switch1.value() == 0:
        set_led_color(255, 0, 0)  # RED for limit switch 1
    elif limit_switch2.value() == 0:
        set_led_color(0, 255, 0)  # GREEN for limit switch 2
    
    # Button 1 Controls LED Cycling
    if button1.value() == 1:
        cycle_led()
        sleep(0.3)  # Debounce
    
    # Button 2 Controls Motor Toggle
    if button2.value() == 1:
        toggle_motor()
        sleep(0.3)  # Debounce
    
    # Potentiometer Adjusts Motor Speed
    pot_value = potentiometer.read_u16()
    motor_speed = int(1000 - (pot_value / 65535) * 800)  # Map to speed range
    
    # Move the motor if running
    if motor_running:
        motor_control(1, motor_speed)  # Move forward at speed
