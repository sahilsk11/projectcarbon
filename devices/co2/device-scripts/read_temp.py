import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)


def read_data(return_humidity=False):
    result = instance.read()
    temperature = result.temperature
    if temperature == 0:
        temperature = None
    if return_humidity:
        return temperature, result.humidity
    return temperature

if (__name__ == "__main__"):
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)

        time.sleep(1)