from tkinter import *
from gpiozero import LED
from time import sleep


# --- Classe de l'interface avec logique intégrée ---
class SecurityForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Système de sécurité")
        self.root.geometry("250x100")

        # État du système
        self.systemStatus = 0  # 0 = désarmé, 1 = armé

        # LEDs 7 segments
        self.segments = [
            LED(8), LED(9), LED(10),
            LED(11), LED(12), LED(13), LED(17)
        ]
        # LED d'alarme
        self.led_alarm = LED(21)

        # Dictionnaire des chiffres/lettres
        self.digits = {
            0: [1,1,1,1,1,1,0],
            1: [0,1,1,0,0,0,0],
            2: [1,1,0,1,1,0,1],
            3: [1,1,1,1,0,0,1],
            4: [0,1,1,0,0,1,1],
            5: [1,0,1,1,0,1,1],
            6: [1,0,1,1,1,1,1],
            7: [1,1,1,0,0,0,0],
            8: [1,1,1,1,1,1,1],
            9: [1,1,1,1,0,1,1],
            'A': [1,1,1,0,1,1,1]
        }

        # Interface graphique
        self.btnArmer = Button(self.root, text="Armer", width=10, command=self.armer_system)
        self.btnDesarmer = Button(self.root, text="Désarmer", width=10, command=self.desarmer_system)
        self.lblStatus = Label(self.root, text="État: Désarmé")

        self.btnArmer.grid(row=0, column=0, padx=10, pady=10)
        self.btnDesarmer.grid(row=0, column=1, padx=10, pady=10)
        self.lblStatus.grid(row=1, column=0, columnspan=2)

        # Initialisation de l'affichage
        self.show_digit(0)

        # Boucle principale
        self.root.mainloop()

    def show_digit(self, val):
        pattern = self.digits[val]
        for seg, state in zip(self.segments, pattern):
            seg.off() if state else seg.on()

    def armer_system(self):
        if self.systemStatus == 0:
            for i in range(10):
                self.show_digit(i)
                sleep(1)
            self.show_digit('A')
            self.systemStatus = 1
            self.lblStatus.config(text="État: Armé")

    def desarmer_system(self):
        if self.systemStatus == 1:
            for i in reversed(range(10)):
                self.show_digit(i)
                sleep(1)
            self.show_digit(0)
            self.systemStatus = 0
            self.lblStatus.config(text="État: Désarmé")


# --- Lancement de l'application ---
if __name__ == "__main__":
    root = Tk()
    app = SecurityForm(root)
