#include <LedControl.h>
#include <Wire.h>
#include <MPU6050_tockn.h>


MPU6050 mpu6050(Wire);
float angleX;
float angleY;
int pin_Green_Button = 10;
int pin_Blue_Button = 9;

int SENSOR_PIN = 2;
int currentState;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  pinMode(pin_Green_Button, INPUT);
  pinMode(pin_Blue_Button, INPUT);
  pinMode(SENSOR_PIN, INPUT);
}

void loop() {
  mpu6050.update();
  angleX = mpu6050.getAngleX();
  angleY = mpu6050.getAngleY();
  float angleZ = mpu6050.getAngleZ();
  boolean state_Bleu_Bouton = digitalRead(pin_Blue_Button);
  boolean state_Green_Bouton = digitalRead(pin_Green_Button);
  currentState = digitalRead(SENSOR_PIN);
  Serial.print(angleX);
  Serial.print(" ");
  Serial.print(angleY);
  Serial.print(" ");
  Serial.print(angleZ);
  Serial.print(" ");
  Serial.print(state_Green_Bouton);
  Serial.print(" ");
  Serial.print(state_Bleu_Bouton);
  Serial.print(" ");
  Serial.println(currentState);
  delay(150);
}