""" Example for using the SGP30 with CircuitPython and the Adafruit library"""

import time
import board
import busio
import adafruit_sgp30
import datetime
import requests
import data_upload

#Customize location of file
file_name = "anvil-data"

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

def write_data(co2, TVOC, current_time):
    f = open(file_name + ".csv", "a")
    f.write("\n" + current_time + "," + str(co2) + "," + str(TVOC))
    f.close()

    last_read = open("last_reading.txt", "w")
    last_read.write(current_time + "," + str(co2) + "," + str(TVOC))
    last_read.close()

while True:
    try:
        co2 = sgp30.eCO2
        TVOC = sgp30.TVOC
        current_time = datetime.datetime.now().strftime("%-m/%d/%y %-I:%M:%S %p")
        time.sleep(1)
        elapsed_sec += 1
        if TVOC == 0:
            print("CALIBRATING")
        print("eCO2 = %d ppm \t TVOC = %d ppb" % (co2, TVOC))
        #Reset baseline
        if elapsed_sec % 10 == 0:
            print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
        if elapsed_sec % 30 == 0:
            write_data(co2, TVOC, current_time)
        if elapsed_sec == 70:
            if (TVOC != 0):
                data_upload.upload(current_time, co2)
                elapsed_sec = 0

    except IOError:
        print("Unable to detect sensor.")
        time.sleep(5)