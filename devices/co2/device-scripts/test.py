import datetime

co2_reading = 1000
data_obj = '{"time": "' + str(datetime.datetime.now()) + '", "co2": ' + str(co2_reading) + '}'
print(data_obj)