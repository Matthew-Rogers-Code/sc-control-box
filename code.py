import board
from digitalio import DigitalInOut, Direction, Pull
import time
from joystick_xl.inputs import Axis, Button, Hat, VirtualInput
from joystick_xl.joystick import Joystick

#Logic for switch 1
switch1 = DigitalInOut(board.GP16)
switch1.direction = Direction.INPUT
switch1.pull = Pull.UP
previous_status1 = False
virtual1 = VirtualInput(value=False)
bswitch1 = Button(source=virtual1)

#Logic for switch 2
switch2 = DigitalInOut(board.GP17)
switch2.direction = Direction.INPUT
switch2.pull = Pull.UP
previous_status2 = False
virtual2 = VirtualInput(value=False)
bswitch2 = Button(source=virtual2)

#Logic for switch 3
switch3 = DigitalInOut(board.GP18)
switch3.direction = Direction.INPUT
switch3.pull = Pull.UP
previous_status3 = False
virtual3 = VirtualInput(value=False)
bswitch3 = Button(source=virtual3)

#Logic for switch 4
switch4 = DigitalInOut(board.GP20)
switch4.direction = Direction.INPUT
switch4.pull = Pull.UP
previous_status4 = False
virtual4 = VirtualInput(value=False)
bswitch4 = Button(source=virtual4)

#Logic for switch 5
switch5 = DigitalInOut(board.GP21)
switch5.direction = Direction.INPUT
switch5.pull = Pull.UP
previous_status5 = False
virtual5 = VirtualInput(value=False)
bswitch5 = Button(source=virtual5)

#Logic for switch 6
switch6 = DigitalInOut(board.GP22)
switch6.direction = Direction.INPUT
switch6.pull = Pull.UP
previous_status6 = False
virtual6 = VirtualInput(value=False)
bswitch6 = Button(source=virtual6)

joystick = Joystick()
joystick.add_input(
    Button(board.GP0),  
    Button(board.GP1),
    Button(board.GP2),
    Button(board.GP3),
    Button(board.GP4),
    Button(board.GP5),
    Button(board.GP6),
    Button(board.GP7),
    Button(board.GP8),
    Button(board.GP9),
    Button(board.GP10),
    Button(board.GP11),
    Button(board.GP12),
    Button(board.GP13),
    Button(board.GP14),
    bswitch1,  
    bswitch2,
    bswitch3,
    Button(board.GP19),
    bswitch4,
    bswitch5,
    bswitch6,
    Button(board.GP26),
    Axis(board.GP27),
    Axis(board.GP28)
)

while True:
    current1 = switch1.value
    if current1 != previous_status1:
        virtual1.value = False
        joystick.update()
        time.sleep(0.05)
        virtual1.value = True
        joystick.update()
    previous_status1 = current1
    
    current2 = switch2.value
    if current2 != previous_status2:
        virtual2.value = False
        joystick.update()
        time.sleep(0.05)
        virtual2.value = True
        joystick.update()
    previous_status2 = current2
    
    current3 = switch3.value
    if current3 != previous_status3:
        virtual3.value = False
        joystick.update()
        time.sleep(0.05)
        virtual3.value = True
        joystick.update()
    previous_status3 = current3
    
    current4 = switch4.value
    if current4 != previous_status4:
        virtual4.value = False
        joystick.update()
        time.sleep(0.05)
        virtual4.value = True
        joystick.update()
    previous_status4 = current4
    
    current5 = switch5.value
    if current5 != previous_status5:
        virtual5.value = False
        joystick.update()
        time.sleep(0.05)
        virtual5.value = True
        joystick.update()
    previous_status5 = current5
    
    current6 = switch6.value
    if current6 != previous_status6:
        virtual6.value = False
        joystick.update()
        time.sleep(0.05)
        virtual6.value = True
        joystick.update()
    previous_status6 = current6
    
    joystick.update()

