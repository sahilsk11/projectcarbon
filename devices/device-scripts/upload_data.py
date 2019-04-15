import requests
import datetime

def upload(current_time_str, co2, temp):
    r = requests.get('http://projectcarbon.io/devices/co2/server-side/response_handler.py',
                      data={"command": "insert", "co2": co2, "time": current_time_str, "temperature": temp,
                            "test": False})
    print("----------------")
    print("Uploaded at " + current_time_str)
    print("Status code: " + str(r.status_code))
    print(r.text)
    print("----------------")

if (__name__ == "__main__"):

    current_time_str = datetime.datetime.now().strftime("%-m/%d/%y %-I:%M:%S %p")
    co2 = 1000
    temp = 25

    r = requests.post('http://projectcarbon.io/devices/co2/server-side/response_handler.py',
                      data={"command": "insert", "co2": co2, "time": current_time_str, "temperature": temp,
                            "test": True})
    print("----------------")
    print("Uploaded at " + current_time_str)
    print("Status code: " + str(r.status_code))
    print(r.text)
    print("----------------")