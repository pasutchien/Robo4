# Robo4

## Project Overview

Robo4 is a project centered around developing a linear stage system controlled by a Raspberry Pi Pico. This system utilizes various components such as stepper motors, RGB LEDs, buttons, and limit switches to provide precise mechanical movement and visual feedback.

## Features

- **Stepper Motor Control**: Moves a platform along a linear stage with precise control.
- **RGB LED Feedback**: Changes colors based on operational status.
- **Button Inputs**: Two buttons for manual control of the motor's direction.
- **Limit Switches**: Ensures the motor stops at the ends of the stage to prevent overtravel.

## Hardware Components

- Raspberry Pi Pico
- DM452 Motor Driver
- Stepper Motor
- RGB LED
- Buttons
- Limit Switches
- Potentiometer

## Setup

Details on how to set up the hardware and configure the software will be added here.

## Connection with RPi Pico

- Button 1 => GP0
- Button 2 => GP1
- LED Red  => GP2
- LED Green=> GP3
- LED Blue => GP4
- Limit switch 1 => GP5
- Limit switch 2 => GP6
- Motor Driver
 - PUL => GP7
 - DIR => GP8
 - ENA => GP9
- Potentiometer => GP28 (ADC2)

## Contributing

Feel free to fork this project and contribute by submitting a pull request. We appreciate your input!

## License

This project is released under the MIT License.
