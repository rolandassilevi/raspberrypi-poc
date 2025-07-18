# RASPBERRY PI - POC (Périphériques et Objets Connectés)
Programmer des objets et périphériques et les connecter à internet à travers un Raspberry Pi

---

## 📌 Lab : Simulation d'un mini Système de Sécurité à 4 Zones

Ce Lab simule un système de sécurité domotique à 4 zones à l’aide d’un Raspberry Pi, de boutons poussoirs et d’un afficheur 7 segments à anode commune. Il est destiné à un usage pédagogique dans le cadre du cours *Périphériques et Objets Connectés (POC)*.

---

## 🎯 Objectifs pédagogiques

- Contrôler des composants électroniques via les GPIO d’un Raspberry Pi.
- Lire l’état de capteurs simulés à l’aide de boutons-poussoirs.
- Afficher dynamiquement un état système sur un afficheur 7 segments.
- Gérer un système d’armement, de détection et de désactivation d’alarme.
- Modéliser un système de sécurité multi-zones.

---

## 🧰 Matériel requis

| Composant                         | Quantité |
|----------------------------------|----------|
| Raspberry Pi (avec GPIO header)  | 1        |
| GPIO T-Plus (adaptateur GPIO)    | 1        |
| Breadboard                       | 1        |
| Afficheur 7 segments (anode commune) | 1    |
| Boutons-poussoirs                | 5        |
| Résistances 220Ω (segments)      | 7        |
| Résistance 330Ω (LED alarme)     | 1        |
| Fils de connexion                | ~30      |

---

## ⚙️ Fonctionnement

1. **État désarmé** : le système affiche `0`.
2. **Armement** : appui sur le bouton ON/OFF → délai de 10s → affichage de `A`.
3. **Détection** : pression sur un bouton de zone déclenche une alarme :
    - Afficheur indique `1`, `2`, `3` ou `4` selon la zone fautive.
4. **Désactivation** : appui sur le bouton correspondant à la zone active éteint l’alarme et revient à `A`.

---

## 🖥️ Lancement du code

```bash
python segment_zones_1.py
