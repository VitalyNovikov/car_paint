import time
import math

from lib.controller import *
from lib.display import *
from fischertechnik.controller.Motor import Motor
from fischertechnik.control.VoiceControl import VoiceControl


speed = None
ticks = None
i = None
number = None
size = None
def testMove():
    global speed, ticks, i, number, size
    ticks = 100
    moveF()
    moveB()
    moveL()
    moveR()
    moveFL()
    moveBR()
    moveFR()
    moveBL()

def paintSquare():
    global speed, ticks, i, number, size
    penUp()
    ticks = (size * i) / 2
    moveB()
    moveL()
    penDown()
    ticks = size * i
    moveF()
    moveR()
    moveB()
    moveL()
    penUp()
    ticks = (size * i) / 2
    moveF()
    moveR()

def paintCross():
    global speed, ticks, i, number, size
    penUp()
    ticks = size * i
    moveFL()
    penDown()
    moveBR()
    moveBR()
    penUp()
    moveFL()
    moveFR()
    penDown()
    moveBL()
    moveBL()
    penUp()
    moveFR()

def paintDiamond():
    global speed, ticks, i, number, size
    penUp()
    ticks = (size * i) / 2
    moveFL()
    moveBL()
    penDown()
    ticks = size * i
    moveFR()
    moveBR()
    moveBL()
    moveFL()
    penUp()
    ticks = (size * i) / 2
    moveFR()
    moveBR()

def paintSanta():
    global speed, ticks, i, number, size
    penUp()
    ticks = (size * i) / 2
    moveB()
    moveL()
    penDown()
    ticks = size * i
    moveB()
    moveR()
    moveF()
    moveL()
    ticks = (size * i) * math.sqrt(2)
    moveFR()
    moveBR()
    penUp()
    ticks = (size * i) / 2
    moveL()
    moveB()

def paintCircle():
    global speed, ticks, i, number, size
    penUp()
    ticks = size
    moveF()
    penDown()
    TXT_M1_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M2_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M1_encodermotor.set_distance(int(1270), TXT_M2_encodermotor)
    while True:
        if (not TXT_M1_encodermotor.is_running()):
            break
        time.sleep(0.010)
    penUp()

voice_control = VoiceControl()



def on_txt_button_santaclaus_clicked(event):
    global speed, ticks, i, number, size
    paintSanta()

def on_txt_button_circle_clicked(event):
    global speed, ticks, i, number, size
    paintCircle()

def on_txt_button_square_clicked(event):
    global speed, ticks, i, number, size
    for i in (float(number) <= 1) and upRange(float(number), 1, 1) or downRange(float(number), 1, 1):
        paintSquare()

def on_txt_button_cross_clicked(event):
    global speed, ticks, i, number, size
    paintCross()

def on_txt_button_diamond_clicked(event):
    global speed, ticks, i, number, size
    for i in (float(number) <= 1) and upRange(float(number), 1, 1) or downRange(float(number), 1, 1):
        paintDiamond()

def on_txt_button_up_clicked(event):
    global speed, ticks, i, number, size
    penUp()

def on_txt_button_down_clicked(event):
    global speed, ticks, i, number, size
    penDown()


def upRange(start, stop, step):
    while start <= stop:
        yield start
        start += abs(step)


def downRange(start, stop, step):
    while start >= stop:
        yield start
        start -= abs(step)


def penUp():
    global speed, ticks, i, number, size
    TXT_S1_servomotor.set_position(int(300))
    display.set_attr("txt_status_indicator.active", str(False).lower())
    time.sleep(0.1)


def penDown():
    global speed, ticks, i, number, size
    TXT_S1_servomotor.set_position(int(256))
    display.set_attr("txt_status_indicator.active", str(True).lower())
    time.sleep(0.1)


def moveF():
    global speed, ticks, i, number, size
    TXT_M1_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M2_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M3_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M4_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M1_encodermotor.set_distance(int(ticks), TXT_M2_encodermotor, TXT_M3_encodermotor, TXT_M4_encodermotor)
    while True:
        if (not TXT_M1_encodermotor.is_running()):
            break
        time.sleep(0.010)


def moveB():
    global speed, ticks, i, number, size
    TXT_M1_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M2_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M3_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M4_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M1_encodermotor.set_distance(int(ticks), TXT_M2_encodermotor, TXT_M3_encodermotor, TXT_M4_encodermotor)
    while True:
        if (not TXT_M1_encodermotor.is_running()):
            break
        time.sleep(0.010)


def moveL():
    global speed, ticks, i, number, size
    TXT_M1_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M2_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M3_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M4_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M1_encodermotor.set_distance(int(round(ticks * math.sqrt(2))), TXT_M2_encodermotor, TXT_M3_encodermotor, TXT_M4_encodermotor)
    while True:
        if (not TXT_M1_encodermotor.is_running()):
            break
        time.sleep(0.010)


def moveR():
    global speed, ticks, i, number, size
    TXT_M1_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M2_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M3_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M4_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M1_encodermotor.set_distance(int(round(ticks * math.sqrt(2))), TXT_M2_encodermotor, TXT_M3_encodermotor, TXT_M4_encodermotor)
    while True:
        if (not TXT_M1_encodermotor.is_running()):
            break
        time.sleep(0.010)


def moveFL():
    global speed, ticks, i, number, size
    TXT_M2_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M3_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M2_encodermotor.set_distance(int(ticks), TXT_M3_encodermotor)
    while True:
        if (not TXT_M2_encodermotor.is_running()):
            break
        time.sleep(0.010)


def moveFR():
    global speed, ticks, i, number, size
    TXT_M1_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M4_encodermotor.set_speed(int(speed), Motor.CCW)
    TXT_M1_encodermotor.set_distance(int(ticks), TXT_M4_encodermotor)
    while True:
        if (not TXT_M1_encodermotor.is_running()):
            break
        time.sleep(0.010)


def moveBL():
    global speed, ticks, i, number, size
    TXT_M1_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M4_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M1_encodermotor.set_distance(int(ticks), TXT_M4_encodermotor)
    while True:
        if (not TXT_M1_encodermotor.is_running()):
            break
        time.sleep(0.010)


def moveBR():
    global speed, ticks, i, number, size
    TXT_M2_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M3_encodermotor.set_speed(int(speed), Motor.CW)
    TXT_M2_encodermotor.set_distance(int(ticks), TXT_M3_encodermotor)
    while True:
        if (not TXT_M2_encodermotor.is_running()):
            break
        time.sleep(0.010)


def command_callback(event):
    global speed, ticks, i, number, size
    if (event).lower() == 'quadrat' or (event).lower() == 'square':
        paintSquare()
    elif (event).lower() == 'kreuz' or (event).lower() == 'cross':
        paintCross()
    elif (event).lower() == '#' or (event).lower() == 'diamond':
        paintDiamond()
    elif (event).lower() == 'kreis' or (event).lower() == 'circle':
        paintCircle()
    elif (event).lower() == 'santa claus' or (event).lower() == 'santa clause':
        paintSanta()
    elif (event).lower() == 'hoch' or (event).lower() == 'up':
        penUp()
    elif (event).lower() == 'runter' or (event).lower() == 'down':
        penDown()
    elif (event).lower() == 'test' or (event).lower() == 'move':
        testMove()
    else:
        print(event)


voice_control.add_command_listener(command_callback)


display.button_clicked("txt_button_santaclaus", on_txt_button_santaclaus_clicked)
display.button_clicked("txt_button_circle", on_txt_button_circle_clicked)
display.button_clicked("txt_button_square", on_txt_button_square_clicked)
display.button_clicked("txt_button_cross", on_txt_button_cross_clicked)
display.button_clicked("txt_button_diamond", on_txt_button_diamond_clicked)
display.button_clicked("txt_button_up", on_txt_button_up_clicked)
display.button_clicked("txt_button_down", on_txt_button_down_clicked)



speed = 250
number = 1
size = 70
i = 1
penUp()
while True:
    pass


