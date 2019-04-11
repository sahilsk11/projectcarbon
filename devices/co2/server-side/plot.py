#!/usr/bin/python

import cgi
import json

print("Content-type: application/json\n\n")

file_handle = "data.csv"



def parse_csv(values):
    f = open(file_handle, "r")

    raw_data = f.read()
    f.close()
    co2_levels = []
    time_values = []

    parsed_data = raw_data.split("\n")
    if (values > len(parsed_data)):
        values = len(parsed_data)
    for i in range(len(parsed_data) - values, len(parsed_data)):
        parsed_data[i] = parsed_data[i].split(",")
        time_values.append(parsed_data[i][0])
        co2_levels.append(int(parsed_data[i][1]))
    #print(time_values)
    return [co2_levels, time_values]

form = cgi.FieldStorage()
command = form.getfirst("command", "")
values = form.getfirst("values", "")

data = parse_csv(int(values))

if (command == "getchart"):
    j = json.dumps(data)
    print(j)
