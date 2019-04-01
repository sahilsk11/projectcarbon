""" Example for using the SGP30 with CircuitPython and the Adafruit library"""

import time
import board
import busio
import adafruit_sgp30
import datetime
import requests

#Customize location of file
file_name = "anvil-03-30-19"

#initialize chip object
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

#print("SGP30 serial #", [hex(i) for i in sgp30.serial])

#Initialize sensor
sgp30.iaq_init()
#Set baseline
sgp30.set_iaq_baseline(0x8973, 0x8aae)

elapsed_sec = 0

def write_data(co2, TVOC):
    f = open(file_name + ".csv", "a")
    f.write("\n" + str(datetime.datetime.now()) + "," + str(co2) + ", " + TVOC)
    f.close()
    publish_file()

def publish_file():
    f = open(file_name + ".csv", "r")
    r = requests.post("https://www.iotspace.tech/projectcarbon/devices/co2", files={file_name + ".csv": f})
    f.close()


while True:
    #Read co2 value
    try:
        co2 = sgp30.eCO2
        TVOC = sgp30.TVOC
        time.sleep(1)
        elapsed_sec += 1
        #Reset baseline
        if elapsed_sec % 10 == 0:
            print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
        if elapsed_sec == 30:
            write_data(co2, TVOC)
            elapsed_sec = 0
    except IOError:
        print("Unable to detect sensor.")
        time.sleep(5)