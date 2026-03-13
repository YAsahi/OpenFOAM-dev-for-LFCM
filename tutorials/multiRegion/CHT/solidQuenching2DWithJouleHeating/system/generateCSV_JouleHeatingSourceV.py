#/usr/bin/python3
import csv
import pprint
import math

print ("Hello")
freq  = 1              #[Hz] Frequency
Va    = 20             #[V]  Amplitude
omega = freq*math.pi #[rad/s]=[1/s]*[rad]
with open('operation.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow( ['time[sec]', 'jouleHeatingSource:V[V]' ] )
    for stp in range(1000):
        t = stp / 100
        v = Va*math.sin(omega*t)
        writer.writerow( [t, v] )


