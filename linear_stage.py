from machine import Pin, ADC, PWM
from utime import sleep_us, sleep

# Buttons
button1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(1, Pin.IN, Pin.PULL_DOWN)

# LED
led_red = PWM(Pin(2))
led_green = PWM(Pin(3))
led_blue = PWM(Pin(4))

# Switches
limit_switch1 = Pin(5, Pin.IN, Pin.PULL_UP)
limit_switch2 = Pin(6, Pin.IN, Pin.PULL_UP)

# Stepper Motor
motor_pul = Pin(7, Pin.OUT)
motor_dir = Pin(8, Pin.OUT)
motor_ena = Pin(9, Pin.OUT)

# ADC for Potentiometer
potentiometer = ADC(28)

# Frequency for PWM (LED and stepper pulse)
led_red.freq(1000)
led_green.freq(1000)
led_blue.freq(1000)
motor_pul.freq(500)  # for stepper motor

def set_led_color(r, g, b):
    led_red.duty_u16(r * 65535 // 255)
    led_green.duty_u16(g * 65535 // 255)
    led_blue.duty_u16(b * 65535 // 255)

def check_limit_switches():
    return limit_switch1.value() == 0 or limit_switch2.value() == 0

def motor_control(direction, steps, speed):
    motor_dir.value(direction)
    motor_ena.value(0)  # Enable motor
    for _ in range(steps):
        if check_limit_switches():
            break
        motor_pul.value(1)
        sleep_us(speed)
        motor_pul.value(0)
        sleep_us(speed)
    motor_ena.value(1)  # Disable motor

while True:
    if button1.value() == 1:
        motor_control(1, 200, 500)  # Move forward 200 steps
    if button2.value() == 1:
        motor_control(0, 200, 500)  # Move backward 200 steps
    # Read potentiometer value and set LED color based on the value
    pot_value = potentiometer.read_u16()
    set_led_color(pot_value % 256, (pot_value // 2) % 256, (pot_value // 3) % 256)
    sleep(0.1)


# Button 1 moves the stepper motor forward
# Button 2 moves it backward
# limit switches stops the motor at each end of the stage. 
# The RGB LED color changes
# based on the potentiometer's position.