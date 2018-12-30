# Nikko Remote Car remade with RPi and 
# 4 pins are being used for UP/DOWN/RIGHT/LEFT
# bleutooth connection need to be done before runing the code

import RPi.GPIO as GPIO
import evdev 

# pwm 25ms /3.5 = 8ms period ==> 125hz
# up    (pwm) : GPIO20 | orange 
# down  (pwm) : GPIO21 | bleu 
# right (DC)  : GPIO16 | white 
# left  (DC)  : GPIO19 | yellow 

# rpi b+ gpios pinout :
#                  | GND    (GND)   34 
# 35 (left) GPIO19 | GPIO16 (right) 36
# 37 (NC)   GPIO26 | GPIO20 (up)    38
# 39 (GND)  GND    | GPIO21 (down)  40

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT) #right
GPIO.setup(19, GPIO.OUT) #left
GPIO.setup(20, GPIO.OUT) #up   
GPIO.setup(21, GPIO.OUT) #down 

GPIO.output(16, GPIO.LOW) #right
GPIO.output(19, GPIO.LOW) #left
GPIO.output(20, GPIO.LOW) #up
GPIO.output(21, GPIO.LOW) #down

# see all bt devices
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)

device = evdev.InputDevice('/dev/input/event0')
print(device)

# 125Hz freq for the Nikko Car
pUp   = GPIO.PWM(20, 125)   #up
pDown = GPIO.PWM(21, 125) #down

# default 50% DC
DutyCycle = 50

for event in device.read_loop():
    
    #print(event) # debug

    if event.code == 17 and event.type == 3 and event.value == -1:
        print("Up:activated")
        pUp.start(DutyCycle)
    
    if event.code == 17 and event.type == 3 and event.value == 1:
        print("Down:activated")
        pDown.start(DutyCycle)
               
    if event.code == 17 and event.type == 3 and event.value == 0:
        print("Up and Down :des-activated")
        pUp.stop()
        pDown.stop()

    if event.code == 16 and event.type == 3 and event.value == 1:
        print("Right:activated")
        GPIO.output(16, GPIO.HIGH) #right
        GPIO.output(19, GPIO.LOW) #left

    if event.code == 16 and event.type == 3 and event.value == -1:
        print("Left:activated")
        GPIO.output(16, GPIO.LOW) #right
        GPIO.output(19, GPIO.HIGH) #left

    if event.code == 16 and event.type == 3 and event.value == 0:
        print("Right and Left :des-activated")
        GPIO.output(16, GPIO.LOW) #right
        GPIO.output(19, GPIO.LOW) #left

    if event.code == 306 and event.type == 1 and event.value == 1:
        print("Normal mode : enable")
        DutyCycle = 50

    if event.code == 307 and event.type == 1 and event.value == 1:
        print("Boost mode : enable")
        DutyCycle = 95

    if event.code == 304 and event.type == 1 and event.value == 1:
        print("Slow mode : enable")
        DutyCycle = 25

GPIO.cleanup()
