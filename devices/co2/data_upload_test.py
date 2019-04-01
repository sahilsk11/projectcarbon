import requests

file_name = "data"

f = open(file_name + ".csv", "r")
r = requests.post("https://www.iotspace.tech/projectcarbon/devices/co2", files={file_name + ".csv": f})
f.close()