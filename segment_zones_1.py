from gpiozero import LED, Button
from time import sleep

# Segments du display 7 segments : A-G
sega = LED(8)
segb = LED(9)
segc = LED(10)
segd = LED(11)
sege = LED(12)
segf = LED(13)
segg = LED(17)

segments = [sega, segb, segc, segd, sege, segf, segg]

# Configuration des boutons
btn = Button(27)  # Bouton d'activation du système
zone1 = Button(22)
zone2 = Button(5)
zone3 = Button(6)
zone4 = Button(19)

# État initial du système : 0 = désarmé, 1 = armé
systemStatus = 0

# Table d’allumage pour chaque chiffre/lettre sur 7 segments
digits = {
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

# Fonction pour afficher un chiffre/lettre
def show_digit(val):
    pattern = digits[val]
    for seg, state in zip(segments, pattern):
        seg.off() if state else seg.on()

# Compte à rebours vers le haut (armement)
def count_up():
    for i in range(10):
        show_digit(i)
        sleep(1)

# Compte à rebours vers le bas (désarmement)
def count_down():
    for i in reversed(range(10)):
        show_digit(i)
        sleep(1)

# Fonction de bascule de l'état du système
def toggle_system():
    global systemStatus
    if systemStatus == 0:
        count_up()
        show_digit('A')  # Système armé
        systemStatus = 1
    else:
        count_down()
        show_digit(0)  # Système désarmé
        systemStatus = 0

# Associe l’événement de pression du bouton à la fonction
btn.when_pressed = toggle_system

# Affiche initial
show_digit(0)

# Boucle principale
while True:
    if systemStatus == 1:
        if zone1.is_pressed:
            show_digit(1)
        elif zone2.is_pressed:
            show_digit(2)
        elif zone3.is_pressed:
            show_digit(3)
        elif zone4.is_pressed:
            show_digit(4)
    sleep(0.1)
