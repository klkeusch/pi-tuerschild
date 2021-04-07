""" new 20210407 """
import RPi.GPIO as GPIO
LED_PIN = 5#32

def turnLEDOn(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 1)
    return HttpResponse('')

def turnLEDOff(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 0)
    return HttpResponse('')

