# Nikko-RC-using-RPi-Joycon-
Nikko RC Car remake with RPi and Nintendo Joy-Con

up    (pwm) : GPIO20 | orange 
down  (pwm) : GPIO21 | bleu 
right (DC)  : GPIO16 | white 
left  (DC)  : GPIO19 | yellow 

pwm 25ms /3.5 = 8ms period ==> 125hz

rpi b+ gpios pinout :
                  | GND    (GND)   34 
 35 (left) GPIO19 | GPIO16 (right) 36
 37 (NC)   GPIO26 | GPIO20 (up)    38
 39 (GND)  GND    | GPIO21 (down)  40