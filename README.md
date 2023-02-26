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

![](cablage_punchingball.JPG #center)

## Structure du projet
```
📦Project
│   📜README.md
│   📜câblage_balai.JPG
|   📜câblage_balai.fzz
└───📂HogwartsLegacyBroomstickControl
    │
    └───📜HogwartsLegacyBroomstrickControlArduino.ino
    │
    └───📜HogwartsLegacyBroomstickControlScript.py
└───📂

```
## Explications:
1. Partie balai

1. Partie baguette
   * La collecte des données se fait avec le fichier "IMU_Capture.ino". Il faut préalablement avoir installé la bibliothèque "LSM9DS1" sur l'IDE Arduino.
   * "IMU_Classifier_HL.ino" permet d'afficher le nom du sort avec le plus grand score.


<span style="display:block;text-align:center">

[![](câblage_balai.JPG #center)]()

</span>
 
