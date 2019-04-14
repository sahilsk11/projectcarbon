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

valid_temp = []

while True:
    try:
        current_time = datetime.datetime.now().strftime("%-I:%M:%S %p %-m/%d/%y")
        time.sleep(1)
        elapsed_sec += 1

        co2 = read_co2.read_data()
        temperature = read_temp.read_data()
        read_temp.append_to_valid(valid_temp, temperature)
        print(current_time, co2, temperature)
        if elapsed_sec == 30:
            write_data(current_time, co2, temperature)
        #if (elapsed_sec == 60):
            if (temperature == None and len(valid_temp) > 0):
                temperature = int(sum(valid_temp) / len(valid_temp))
            upload_data.upload(current_time, co2, temperature)
            elapsed_sec = 0

    except IOError:
        print("Unable to detect sensor.")
        time.sleep(5)