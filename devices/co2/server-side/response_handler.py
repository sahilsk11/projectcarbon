#!/usr/bin/python

import cgi
import json

print("Content-type: application/json\n\n")

file_handle = "data.csv"

log = open("test.log", "a")

def parse_csv(values):
    f = open(file_handle, "r")

    raw_data = f.read()
    f.close()
    co2_levels = []
    temp_levels = []
    time_values = []

    parsed_data = raw_data.split("\n")
    if (parsed_data[-1] == ''):
        values += 1
    if (values > len(parsed_data)):
        values = len(parsed_data)
    for i in range(len(parsed_data) - values, len(parsed_data)):
        if (parsed_data[i] != ''):
            parsed_data[i] = parsed_data[i].split(",")
            time_stamp = parsed_data[i][0]
            time_values.append(time_stamp)

            co2_reading = parsed_data[i][1]
            log.write(co2_reading)
            if (co2_reading == None or co2_reading == "None"):
                co2_reading = None
            else:
                co2_reading = int(co2_reading)
            co2_levels.append(int(co2_reading))

            temperature = parsed_data[i][2]
            if (temperature == "None" or temperature == None):
                temperature = None
            else:
                temperature = int(temperature)
            temp_levels.append(temperature)

    #print(time_values)
    return [time_values, co2_levels, temp_levels]

def insert_value(time, co2, temperature):
    f = open(file_handle, "a")
    f.write(time + "," + str(co2) + "," + str(temperature) + "\n")
    f.close()
    success = True
    return success

form = cgi.FieldStorage()
command = form.getfirst("command", "")
values = form.getfirst("values", "")
co2 = form.getfirst("co2")
time = form.getfirst("time")
temperature = form.getfirst("temperature")


if (command == "getchart"):
    data = parse_csv(int(values))
    j = json.dumps(data)
    print(j)

elif (command == "insert"):
    success = insert_value(time, co2, temperature)
    d = {"success": success}
    j = json.dumps(d)
    print(j)
