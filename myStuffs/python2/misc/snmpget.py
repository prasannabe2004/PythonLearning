#!/bin/python2

import subprocess

var = ["1.3.6.1.4.1.9.9.273.1.1.2.1.1.1",
"1.3.6.1.4.1.9.9.273.1.1.2.1.1.2",
"1.3.6.1.2.1.10.7.2.1.19.1",
"1.3.6.1.2.1.10.7.2.1.19.2",
"1.3.6.1.2.1.2",
"1.3.6.1.4.1.9.10.105.1.1.1",
"1.3.6.1.4.1.9.9.273.1",
"1.3.6.1.2.1.47.1.1.1.1.7.4",
"1.3.6.1.2.1.2.2.1.5.1",
"1.3.6.1.2.1.2.2.1.5.2",
"1.3.6.1.2.1.2.2.1.7.1",
"1.3.6.1.2.1.2.2.1.7.2",
"1.3.6.1.2.1.2.2.1.8.1",
"1.3.6.1.2.1.2.2.1.8.2",
"1.3.6.1.2.1.2.2.1.10.1",
"1.3.6.1.2.1.2.2.1.10.2",
"1.3.6.1.2.1.2.2.1.16.1",
"1.3.6.1.2.1.2.2.1.16.2",
"1.3.6.1.4.1.9.9.413.1.1.1.1.6",
"1.3.6.1.4.1.9.9.413.1.1.1.1.19",
"1.3.6.1.4.1.9.9.413.1.1.1.1.20",
"1.3.6.1.4.1.9.9.413.1.1.1.1.7",
"1.3.6.1.4.1.9.9.413.1.1.1.1.11",
"1.3.6.1.4.1.9.9.413.1.1.1.1.12",
"1.3.6.1.4.1.9.9.272.1.1.1.10.1.6",
"1.3.6.1.4.1.9.9.272.1.1.1.10.1.8"]

for i in var:
    print 'Snmpget for ' + i
    p = subprocess.Popen([
        'snmpget',
        '-v', '1',
        '-c', 'public',
        '172.19.134.240',
        i],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
    out, err = p.communicate()
    print out

