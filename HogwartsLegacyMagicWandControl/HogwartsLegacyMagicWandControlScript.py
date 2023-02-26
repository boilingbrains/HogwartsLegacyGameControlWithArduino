import serial
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

port = "COM11"
baudrate = 9600
ser = serial.Serial(port,baudrate)

while True:
    if ser.in_waiting:
        
        data = ser.readline().decode('utf-8').strip()
        
        if  data == "accio": 
            keyboard.press("&") 
            keyboard.release("&")
            
        if  data == "lumos": 
            keyboard.press("é") 
            keyboard.release("é")
            
        if  data== "revelio":
            keyboard.press("r")
            keyboard.release("r")
    
            
        
            
            