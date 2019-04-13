import board
import busio
import adafruit_sgp30
import time

#initialize chip object
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

#print("SGP30 serial #", [hex(i) for i in sgp30.serial])

#Initialize sensor
sgp30.iaq_init()
#Set baseline
sgp30.set_iaq_baseline(0x8973, 0x8aae)

def read_data():
    co2 = sgp30.eCO2
    TVOC = sgp30.TVOC
    if TVOC == 0:
        return None
    return co2

if (__name__ == "__main__"):
    elapsed_sec = 0
    while True:
        co2 = sgp30.eCO2
        TVOC = sgp30.TVOC
        time.sleep(1)
        elapsed_sec += 1
        if TVOC == 0:
            print("CALIBRATING")
        print("eCO2 = %d ppm \t TVOC = %d ppb" % (co2, TVOC))
        # Reset baseline
        if elapsed_sec == 10:
            print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
            elapsed_sec = 0