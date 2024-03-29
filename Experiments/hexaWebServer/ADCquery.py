#!/usr/bin/env python

import json


try:
    from ADCPi import ADCPi
except ImportError:
    print("Failed to import ADCPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append('..')
        from ADCPi import ADCPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")

adc0 = ADCPi(0x68, 0x69, 18)   

baseVoltage = adc0.read_voltage(1) # Pin 1 on adc0 is used to capture the boards base voltage   
    
def main():
    
    values = {
        1 : convert(baseVoltage, adc0.read_voltage(2)),
        2 : convert(baseVoltage, adc0.read_voltage(3)),
        3 : convert(baseVoltage, adc0.read_voltage(4)),
        4 : convert(baseVoltage, adc0.read_voltage(5)),
        5 : convert(baseVoltage, adc0.read_voltage(6)),
        6 : convert(baseVoltage, adc0.read_voltage(7)),
        7 : convert(baseVoltage, adc0.read_voltage(8))       
    }
        
    return json.dumps(values)


def convert(base, input):   
    try:
        output = input/base
    except:
        output = 0   
    return output    

main()