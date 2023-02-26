
# TODO:Fixe IMU calibration causing shift on angle's values
# TODO:Adapt the angleZ to rotate the camera smoothly when turning left or right


import time
from serial import Serial
import vgamepad as vg
import numpy as np
gamepad = vg.VX360Gamepad()

port = "COM3"
baudrate = 9600
state_in_broom = 'no movement and not on the broom'
in_broom = False
previousTouch = 0


def wakeUp():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()


def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))


def takeOff():
    gamepad.press_button(
        button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    gamepad.update()
    time.sleep(0.5)
    gamepad.press_button(
        button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    time.sleep(0.5)
    gamepad.reset()
    return True


def landing():
    gamepad.press_button(
        button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    time.sleep(0.1)
    gamepad.reset()
    gamepad.update()
    return False


def broomInMouvment(angleX, angleY, angleZ):
    lowThresholds = [round(x, 2) for x in np.arange(-5, 5, 0.01)]
    if angleX in lowThresholds and angleY in lowThresholds:
        gamepad.reset()
        gamepad.update()
        pass
        return 'No movement and on the broom'
    else:
        if angleX > 25:
            y_values_right_joystick = 1.0
            x_values_left_joystick = round(
                mapRange(angleY, -130.0, 130.0, -1.0, 1.0), 2)
            x_values_right_joystick = round(
                mapRange(angleZ, 40.0, -40.0, -1.0, 1.0), 2)
        elif angleX < -25:
            y_values_right_joystick = -1.0
            x_values_left_joystick = round(
                mapRange(angleY, -130.0, 130.0, -1.0, 1.0), 2)
            x_values_right_joystick = round(
                mapRange(angleZ, 40.0, -40.0, -1.0, 1.0), 2)
        elif angleY > 50:
            x_values_left_joystick = 1.0
            y_values_right_joystick = round(
                mapRange(angleX, -130.0, 130.0, -1.0, 1.0), 2)
            x_values_right_joystick = 0
        elif angleY < -50:
            x_values_left_joystick = -1.0
            y_values_right_joystick = round(
                mapRange(angleX, -130.0, 130.0, -1.0, 1.0), 2)
            x_values_right_joystick = 0
        elif angleX > 25 and angleY > 50:
            y_values_right_joystick = 1.0
            x_values_left_joystick = 1.0
            x_values_right_joystick = 0
        elif angleX < -25 and angleY < 50:
            y_values_right_joystick = -1.0
            x_values_left_joystick = -1.0
            x_values_right_joystick = 0
        else:
            x_values_left_joystick = round(
                mapRange(angleY, -130.0, 130.0, -1.0, 1.0), 2)
            y_values_right_joystick = round(
                mapRange(angleX, -130.0, 130.0, -1.0, 1.0), 2)
            x_values_right_joystick = round(
                mapRange(angleZ, 40.0, -40.0, -1.0, 1.0), 2)

        y_values_left_joystick = abs(round(1-abs(x_values_left_joystick), 2))
        print("angles:", angleX, " ", angleY, " ", "angleZ")
        print("Y_leftstick:", y_values_left_joystick, " ",
              "X_leftstick:", x_values_left_joystick, " ", "y_rightstick:", y_values_right_joystick)
        gamepad.right_joystick_float(
            x_value_float=x_values_right_joystick, y_value_float=y_values_right_joystick)
        gamepad.left_joystick_float(
            x_value_float=x_values_left_joystick, y_value_float=y_values_left_joystick)
        gamepad.right_trigger_float(value_float=1.0)
        gamepad.update()
        return 'Movement and on the broom'


def flyingControl(angleX, angleY, angleZ, up, down):
    if up == 1:
        gamepad.reset()
        gamepad.update()
        gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)
        gamepad.update()
        return 'up'
    elif down == 1:
        gamepad.reset()
        gamepad.update()
        gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)
        gamepad.update()
        return 'down'
    else:
        return broomInMouvment(angleX, angleY, angleZ)


if __name__ == '__main__':
    print("Start")
    wakeUp()
    with Serial(port=port, baudrate=baudrate, timeout=1) as port_serie:
        while True:
            line = port_serie.readline().decode("utf-8").rstrip('\n')
            data = line.split(' ')
            try:
                angleX = float(data[0])  # Pitch
                angleY = float(data[1])  # Roll
                angleZ = float(data[2])  # Taw
                up = int(data[3])
                down = int(data[4])
                touch = int(data[5])

                if in_broom == False:
                    if previousTouch == 0 and touch == 1:
                        state_in_broom = 'take-off'
                        in_broom = takeOff()
                    else:
                        state_in_broom = 'no movement and not on the broom'
                        pass
                else:
                    if previousTouch == 0 and touch == 1:
                        state_in_broom = 'landing'
                        in_broom = landing()
                    else:
                        state_in_broom = flyingControl(
                            angleX, angleY, angleZ, up, down)

                previousTouch = touch
                print(state_in_broom)
            except Exception as e:
                print(e)
                pass
            # except ValueError:
            #     pass
