#!/usr/bin/python

from Subfact_ina219 import INA219

ina = INA219()
result = ina.getBusVoltage_V()

print "Shunt   : %.3f mV" % ina.getShuntVoltage_mV()
print "Bus     : %.3f V" % ina.getBusVoltage_V()
print "Current : %.3f mA" % ina.getCurrent_mA()
