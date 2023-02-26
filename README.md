# Jouer à Hogwarts Legacy dans la vraie vie avec Arduino

## Introduction: 
Ce projet consiste à utiliser l'Arduino Nano et Nano 33 BLE Sense ainsi qu'un ensemble de capteurs et scripts Python afin d'interagir dans le jeu (lancer des sorts et voler avec le balai) avec des vraies objets physique.

composants suivant:
* Arduino Nano
* Arduino Nano 33 BLE Sense
* Capteur tactile
* Centrale Inertielle MPU6050
* Boutons Poussoirs


## Montage électronique
Voici le câblage du projet:

![](cablage_punchingball.JPG#center)

## Structure du projet
```
📦Project
│   📜README.md
│   📜cablage_balai.JPG 
|   📜câblageBalai.fzz 
└───📂HogwartsLegacyBroomstickControl
    │
    └───📜HogwartsLegacyBroomstrickControlArduino.ino
    │
    └───📜HogwartsLegacyBroomstickControlScript.py
└───📂

```
## Explications:
La collecte des données se fait avec le fichier IMU_Capture.ino. Il faut préalablement avoir installé la bibliothèque "LSM9DS1" sur l'IDE Arduino.



<span style="display:block;text-align:center">

[![](#center)]()

</span>
 
