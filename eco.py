import curses
from __future__ import division
import time
import RPi.GPIO as GPIO
import sys
import Adafruit_PCA9685

#Ultrasonic pins
Tr = 11
Ec = 8

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_B_EN    = 4
Motor_A_EN    = 17

Motor_B_Pin1  = 14
Motor_B_Pin2  = 15
Motor_A_Pin1  = 27
Motor_A_Pin2  = 18

Dir_forward   = 0
Dir_backward  = 1

left_forward  = 0
left_backward = 1

right_forward = 0
right_backward= 1

pwn_A = 0
pwm_B = 0

speed_set = 70

line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

def startServo(stdscr):
    # Initialiser la position des servomoteurs
    positions = {
        11: 240,
        12: 400,
        13: 280,
        14: 300,
        15: 285
    }

    try:
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Appuyez sur Q pour quitter")

            # Afficher les positions actuelles des servomoteurs
            for num, pos in positions.items():
                stdscr.addstr(num, 0, f"Servo {num}: {pos}")

            key = stdscr.getch()

            if key == ord('q'):
                break  # Quitter la boucle si la touche 'q' est pressée

            # Mettre à jour les positions des servomoteurs en fonction de la touche pressée
            if ord('1') <= key <= ord('5'):
                servo_num = int(chr(key))
                new_position = positions[servo_num] + 10  # Ajustez la valeur de déplacement selon vos besoins
                positions[servo_num] = new_position
                pwm.set_pwm(servo_num, 0, new_position)
            else:
                stdscr.addstr(7, 0, "Touche non reconnue. Appuyez sur 1-5 pour changer la position des servomoteurs.")

    except KeyboardInterrupt:
        pass  # Gérer l'interruption clavier (Ctrl+C) pour quitter proprement

    # Réinitialiser les servomoteurs à la position initiale avant de quitter
    for num, pos in positions.items():
        pwm.set_pwm(num, 0, pos)

if __name__ == "__main__":
    curses.wrapper(startServo)
