#!/usr/bin/python

import cgi
#import json
#import datetime
import door_sensor

lo
form = cgi.FieldStorage()
command = form.getfirst("command", "")

#execute command
door_sensor.turn()