import RPi.GPIO as GPIO
import time
import multiprocessing
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def rotServo(pin, angle):
    speedDelay = 0.2
    try:
        p = GPIO.PWM(pin, 50)
        p.start(10)
        duty = (angle / 20.0) + 3
        p.ChangeDutyCycle(duty)
        time.sleep(speedDelay)
        p.stop()
    except KeyboardInterrupt:
        GPIO.cleanup()


def move(delta):
    global motor
    global possition1
    t7 = multiprocessing.Process(target=rotServo, args=(motor[6], possition1[6] + delta[6]))
    t1 = multiprocessing.Process(target=rotServo, args=(motor[0], possition1[0] + delta[0]))
    t2 = multiprocessing.Process(target=rotServo, args=(motor[1], possition1[1] + delta[1]))
    t3 = multiprocessing.Process(target=rotServo, args=(motor[2], possition1[2] + delta[2]))
    t4 = multiprocessing.Process(target=rotServo, args=(motor[3], possition1[3] + delta[3]))
    t5 = multiprocessing.Process(target=rotServo, args=(motor[4], possition1[4] + delta[4]))
    t6 = multiprocessing.Process(target=rotServo, args=(motor[5], possition1[5] + delta[5]))
    t8 = multiprocessing.Process(target=rotServo, args=(motor[7], possition1[7] + delta[7]))

    t7.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t8.start()

    t7.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t8.join()


def ahead():
    l = lineFollow()
    a = l[0] + 2
    b = l[1] + 12
    c = l[2]
    d = l[3]
    e = l[4]
    move([0, -b, 0, e, 0, 0, 0, 0])
    move([0, -b, 0, e, c, 0, c - 5, 0])
    move([-a, 0, d + 5, -10, c, 0, c - 5, 0])
    # move([-a,0,d+5,-20,c,0,0,0])
    print(a, b, d, e, c)

    l = lineFollow()
    a = l[0] + 2
    b = l[1] + 12
    c = l[2]
    d = l[3]
    e = l[4]
    move([-a, 0, d + 5, -10, 0, 0, 0, 0])
    move([-a, 0, d + 5, -10, 0, -c + 5, 0, -c])
    move([0, -b, 0, e, 0, -c + 5, 0, -c])
    # move([0,-b,0,e,0,0,0,-c])
    print(a, b, d, e, c)


def aheadNotTurn():
    a, b, d, e, c = 45, 45, 50, 50, 30
    move([0, -b, 0, e, 0, 0, 0, 0])
    move([0, -b, 0, e, c, 0, c - 5, 0])
    move([-a, 0, d + 5, -10, c, 0, c - 5, 0])
    move([-a, 0, d + 5, -10, 0, 0, 0, 0])
    move([-a, 0, d + 5, -10, 0, -c + 5, 0, -c])
    move([0, -b, 0, e, 0, -c + 5, 0, -c])
    print("aheadNotTurn")


def reverse():
    a, b, d, e, c = 40, 40, 40, 40, 30

    move([a, 0, -d, 0, c, 0, c, 0])
    move([a, 0, -d, 0, 0, 0, 0, 0])
    move([a, 0, -d, 0, 0, -c, 0, -c - 10])
    # move([a,0,-d,0,0,-c,0,-c-10])
    move([0, b, 0, -e, 0, -c, 0, -c - 10])
    move([0, b, 0, -e, 0, 0, 0, 0])
    '''
    move([0,b,0,-e,c,0,c,0]) 
    move([a,b,d,-e,c,0,c,0]) 
    move([a,b,d,-e,0,0,0,0]) '''


def leftTurn():
    a, b, d, e, c = 20, 20, 20, 20, 30

    move([0, 0, 0, 0, 0, -c, 0, -c])
    move([a, -b, d, -e, 0, -c, 0, -c])
    move([a, -b, d, -e, 0, 0, 0, 0])
    move([-a, b, -d, e, c, 0, c, 0])
    move([-a, b, -d, e, 0, 0, 0, 0])


def rightTurn():
    a, b, d, e, c = 28, 28, 28, 28, 30

    move([0, 0, 0, 0, c, 0, c, 0])
    move([a, 0, d, 0, c, 0, c, 0])
    move([a, 0, d, 0, 0, 0, 0, 0])
    move([-a, 0, -d, 0, 0, -c, 0, -c])
    move([-a, b, -d, e, 0, 0, 0, 0])


def readyPhoto():
    move([50, -50, 50, -50, 0, 0, 0, 0])


def lineFollow():

    f = 40.0
    c = 30.0

    return(f, f, c, f, f)



motor = [21, 2, 3, 16, 12, 4, 22, 20]
possition1 = [80, 105, 75, 90, 95, 95, 60, 110]
for pin in motor:
    GPIO.setup(pin, GPIO.OUT)


speedDelay = 0.2

try:
    while True:        
        aheadNotTurn()        

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()



