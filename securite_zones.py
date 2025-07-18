# Importation des classes nécessaires de la bibliothèque gpiozero
from gpiozero import LED, Button

# Importation de la fonction sleep pour introduire des délais
from time import sleep

# --- INITIALISATION DU MATÉRIEL ---

# Initialisation des 7 segments de l'afficheur à anode commune
# Chaque segment (A à G) est connecté à un GPIO via une résistance
sega = LED(8)
segb = LED(9)
segc = LED(10)
segd = LED(11)
sege = LED(12)
segf = LED(13)
segg = LED(17)

# Liste des segments pour pouvoir les parcourir facilement dans les fonctions
segments = [sega, segb, segc, segd, sege, segf, segg]

# --- CONFIGURATION DES BOUTONS ---

# Bouton principal qui permet d’armer/désarmer le système
btn = Button(27)

# Boutons correspondant aux zones de sécurité
zone1 = Button(22)  # Porte (contact magnétique)
zone2 = Button(5)   # Détecteur de fumée
zone3 = Button(6)   # Détecteur de mouvement
zone4 = Button(19)  # Détecteur de lumière

# --- VARIABLES DU SYSTÈME ---

# Indicateur de l’état du système :
# 0 = désarmé (OFF), 1 = armé (ACTIVE)
systemStatus = 0

# --- DICTIONNAIRE DES VALEURS À AFFICHER SUR LE 7 SEGMENTS ---

# Chaque chiffre/lettre est défini par un motif de 7 bits (de A à G)
# 1 = segment allumé, 0 = segment éteint
# Comme c’est un afficheur à anode commune, on éteint le segment en mettant à ON et on l’allume en mettant à OFF.
# Dans le cas d'un afficheur à cathode commune, ce serait l'inverse.
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
    'A': [1,1,1,0,1,1,1]  # A = état armé
}

# --- FONCTIONS D’AFFICHAGE ---

# Fonction pour afficher un chiffre ou une lettre sur le 7 segments
def show_digit(val):
    pattern = digits[val]  # Récupère le motif correspondant. Exemple : digits[0] donne [1,1,1,1,1,1,0]
    for seg, state in zip(segments, pattern): # Parcourt en parallèle les segments et leur état
        # Comme c’est une anode commune, on inverse :
        # 1 => .off() (segment allumé), 0 => .on() (segment éteint)
        seg.off() if state else seg.on()
# La fonction zip() crée des paires entre les éléments des deux listes. Elle sert à parcourir deux listes en parallèle :
# - segments : la liste des objets représentant les 7 segments de l’afficheur (chaque segment est un objet LED).
# - pattern : une liste de 7 valeurs (0 ou 1), définissant quels segments doivent être allumés ou éteints pour un chiffre donné.


# Fonction de compte à rebours vers le haut (de 0 à 9)
# utilisée pour simuler le délai d’armement
def count_up():
    for i in range(10):
        show_digit(i)
        sleep(1)

# Fonction de compte à rebours vers le bas (de 9 à 0)
# utilisée pour simuler le délai de désarmement
def count_down():
    for i in reversed(range(10)):
        show_digit(i)
        sleep(1)

# --- GESTION DE L’ÉTAT DU SYSTÈME ---

# Fonction qui change l’état du système :
# - Si désarmé, on l’arme (affiche A après un compte à rebours)
# - Si armé, on le désarme (affiche 0 après compte à rebours inverse)
def toggle_system():
    global systemStatus
    if systemStatus == 0:
        count_up()           # Compte de 0 à 9
        show_digit('A')      # Affiche A pour signifier que le système est armé
        systemStatus = 1     # Passe à l’état armé
    else:
        count_down()         # Compte de 9 à 0
        show_digit(0)        # Affiche 0 pour signifier que le système est désarmé
        systemStatus = 0     # Passe à l’état désarmé

# On configure le bouton principal pour appeler la fonction toggle_system quand il est pressé
btn.when_pressed = toggle_system

# Affichage initial à 0 (système désarmé au démarrage)
show_digit(0)

# --- BOUCLE PRINCIPALE ---

# Boucle infinie qui vérifie en continu si le système est armé et si une zone est activée
while True:
    if systemStatus == 1:  # Seulement si le système est armé
        # Si un bouton de zone est pressé, on affiche son numéro
        if zone1.is_pressed:
            show_digit(1)
        elif zone2.is_pressed:
            show_digit(2)
        elif zone3.is_pressed:
            show_digit(3)
        elif zone4.is_pressed:
            show_digit(4)
    sleep(0.1)  # Petite pause pour éviter une surcharge du processeur
# Fin de la boucle principale
# Le programme continuera à tourner indéfiniment jusqu'à ce qu'il soit arrêté manuellement
# ou que le Raspberry Pi soit éteint.