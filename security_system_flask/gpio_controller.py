from gpiozero import LED, Button
from threading import Thread
from time import sleep

# Segments de l'afficheur
segments = [LED(8), LED(9), LED(10), LED(11), LED(12), LED(13), LED(17)]
led_alarm = LED(21)
digits = {
    0: [1,1,1,1,1,1,0],
    1: [0,1,1,0,0,0,0],
    2: [1,1,0,1,1,0,1],
    3: [1,1,1,1,0,0,1],
    4: [0,1,1,0,0,1,1],
    5: [1,0,1,1,0,1,1],
    6: [1,0,1,1,1,1,1],
    7: [1,1,1,0,0,0,0],
    8: [1,1,1,1,1,1,1],
    9: [1,1,1,1,0,1,1],
}

zone_buttons = {
    1: Button(22),
    2: Button(5),
    3: Button(6),
    4: Button(19)
}

reset_button = Button(4)
system_on = Button(27)

system_status = {"alarm": False, "zone": 0}
stop_blink = False

def show_digit(val):
    pattern = digits.get(val, [0]*7)
    for seg, state in zip(segments, pattern):
        seg.off() if state else seg.on()

def blink_led():
    global stop_blink
    while not stop_blink:
        led_alarm.on()
        sleep(0.3)
        led_alarm.off()
        sleep(0.3)

def trigger_zone(zone_number):
    global stop_blink
    system_status["zone"] = zone_number
    system_status["alarm"] = True
    show_digit(zone_number)
    stop_blink = False
    Thread(target=blink_led).start()

def reset_alarm():
    global stop_blink
    stop_blink = True
    led_alarm.off()
    system_status["alarm"] = False
    show_digit(0)
