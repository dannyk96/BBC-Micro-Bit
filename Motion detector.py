from microbit import *
dot28 = Image("99999:""99999:""99999:""99999:""99999")
all_dots= [dot27, dot28, dot29, dot30,]


display.clear()

while True:
    if accelerometer.was_gesture('shake'):
        display.show(dot28)
        sleep(1000)
        display.clear()
