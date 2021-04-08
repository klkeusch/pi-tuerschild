import RPi.GPIO as GPIO
import time

from django.http import HttpResponseRedirect

LED_PIN = 5

def turnLEDOn(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def turnLEDOff(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 0)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def toggleLED(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 1)
    time.sleep(5)
    GPIO.output(LED_PIN, 0)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
