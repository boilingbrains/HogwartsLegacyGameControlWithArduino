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

![](câblage_balai.JPG#center)

## Structure du projet
```
📦Project
│   📜README.md
│   📜câblage_balai.JPG
|   📜câblage_balai.fzz
└───📂HogwartsLegacyBroomstickControl
│    │
│    └───📜HogwartsLegacyBroomstrickControlArduino.ino
│    │
│    └───📜HogwartsLegacyBroomstickControlScript.py
└───📂HogwartsLegacyMagicWandControl
     │
     └───📜IMU_Capture.ino
     │
     └───📜IMU_Classifier_HL.ino + model.h
     │
     └───📜HogwartsLegacyMagicWandControlScript.py
    

```
## Explications:
1. Partie balai
<span style="display:block;text-align:center">

[![](minia_balai.jpg#center)](https://youtu.be/TjQjy_GWWaY)

</span>
2. Partie baguette
<span style="display:block;text-align:center">

[![](minia_baguette.jpg#center)](https://youtu.be/TjQjy_GWWaY)

</span>

   * "IMU_Capture.ino" permet de visualiser et collecter les données pour l'entraînement du modèle. Il faut préalablement avoir installé la bibliothèque "LSM9DS1" sur l'IDE Arduino pour pouvoir utiliser la centrale inertielle de l'Arduino Nano 33 BLE Sense.
   
   * "IMU_Classifier_HL.ino" (nécessite model.h) permet d'afficher le nom du sort avec le plus grand score dans le moniteur série.



 
