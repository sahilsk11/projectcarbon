import datetime
import time
import read_co2
import read_temp
import upload_data

file_name = "anvil.csv"
elapsed_sec = 0

def write_data(current_time, co2, temperature):
    f = open(file_name + ".csv", "a")
    f.write("\n" + current_time + "," + str(co2) + "," + str(temperature))
    f.close()

while True:
    try:
        current_time = datetime.datetime.now().strftime("%-m/%d/%y %-I:%M:%S %p")
        time.sleep(1)
        elapsed_sec += 1

        co2 = read_co2.read_data()
        temperature = read_temp.read_data()
        print(current_time, co2, temperature)
        if elapsed_sec == 30:
            write_data(current_time, co2, temperature)
            upload_data.upload(current_time, co2, temperature)
            elapsed_sec = 0

    except IOError:
        print("Unable to detect sensor.")
        time.sleep(5)