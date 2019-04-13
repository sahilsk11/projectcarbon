import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin=4)


def read_data(return_humidity=False):
    result = instance.read()
    if result.is_valid():
        temperature = result.temperature
        if temperature == 0:
            temperature = None
        temperature = celsius_to_fahrenheit(temperature)
        if return_humidity:
            return temperature, result.humidity
        return temperature

def celsius_to_fahrenheit(cel):
    return round((cel * 9.0/5) + 32)

if (__name__ == "__main__"):
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d F" % celsius_to_fahrenheit(result.temperature))
            print("Humidity: %d %%" % result.humidity)

        time.sleep(1)