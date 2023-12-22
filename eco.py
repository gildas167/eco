import curses
import pwm  # Assurez-vous d'importer correctement votre bibliothèque PWM

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
