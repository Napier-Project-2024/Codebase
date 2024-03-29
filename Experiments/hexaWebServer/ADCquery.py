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
    

def main():
  
    adc = ADCPi(0x68, 0x69, 12)


        # read from the ADC channels and print to screen
    print("Channel 1: %02f" % adc.read_voltage(1))
    print("Channel 2: %02f" % adc.read_voltage(2))
    print("Channel 3: %02f" % adc.read_voltage(3))
    print("Channel 4: %02f" % adc.read_voltage(4))
    print("Channel 5: %02f" % adc.read_voltage(5))
    print("Channel 6: %02f" % adc.read_voltage(6)
    print("Channel 7: %02f" % adc.read_voltage(7))
    print("Channel 8: %02f" % adc.read_voltage(8))