#!/usr/bin/python

from LIS3DH import LIS3DH
from time import sleep

def clickcallback(channel):
    # interrupt handler callback   
    print "Interrupt detected"
    click = sensor.getClick()
    print "Click detected (0x%2X)" % (click)
    if (click & 0x10): print " single click"
    if (click & 0x20): print " double click"


if __name__ == '__main__':
    sensor = LIS3DH(debug=True)
    sensor.setRange(LIS3DH.RANGE_2G)
    sensor.setClick(LIS3DH.CLK_SINGLE,80,mycallback=clickcallback)

    print "Starting stream"
    while True:
        a1 = sensor.getADC(sensor.ADC_1)
        a2 = sensor.getADC(sensor.ADC_2)
        a3 = sensor.getADC(sensor.ADC_3)

# raw values
        print "\r1: %.6f\t2: %.6f\t3: %.6f" % (a1, a2, a3)
        sleep(0.1)
		
# click sensor if polling & not using interrupt		
#        click = sensor.getClick()
#        if (click & 0x30) :
#            print "Click detected (0x%2X)" % (click)
#            if (click & 0x10): print " single click"
#            if (click & 0x20): print " double click"
