import flask
import subprocess
import time

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

app = flask.Flask()

@app.route('/')
def index():
    def inner():
 
        #     proc = subprocess.Popen(
        #     ['python3 /home/team-member/ABElectronics_Python_Libraries/ADCPi/demos/demo_readvoltage.py'],  # Call any function
        #     shell=True,
        #     stdout=subprocess.PIPE,
        #     universal_newlines=True
        # )

        # for line in iter(proc.stdout.readline,''):
        #     time.sleep(0.01)  # Add control to output
        #     yield line.rstrip() + '<br/>\n'

        adc = ADCPi(0x68, 0x69, 12)


        # read from the ADC channels and print to screen
        print("Channel 1: %02f" % adc.read_voltage(1))
        print("Channel 2: %02f" % adc.read_voltage(2))
        print("Channel 3: %02f" % adc.read_voltage(3))
        print("Channel 4: %02f" % adc.read_voltage(4))
        print("Channel 5: %02f" % adc.read_voltage(5))
        print("Channel 6: %02f" % adc.read_voltage(6))
        print("Channel 7: %02f" % adc.read_voltage(7))
        print("Channel 8: %02f" % adc.read_voltage(8))

    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

app.run(debug=True, port=5000, host='0.0.0.0')