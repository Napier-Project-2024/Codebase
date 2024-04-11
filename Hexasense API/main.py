# Hexasense API v0.1 - Group Project Team 104

# An API to reade voltages from a series of ADC inputs and return values as a JSON string of floats between 0 and 1.
# Makes use of the ADCPi library and the fastAPI library.

# Imports
from fastapi import FastAPI
from starlette.responses import FileResponse 
import datetime
import json

# Load from the ADCPi library provided by ABElectronics
# Try the import
try:
    from ADCPi import ADCPi

# Handle any errors
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

# Define the ADC devices' I2C addresses and sampling bit-depth
adc0 = ADCPi(0x68, 0x69, 12)

# Define the fastAPI application
app = FastAPI()

# Define the root directory reponse of the API
@app.get("/")
async def root():    
    # Return the index.html file
    return FileResponse('index.html')

# Define the "test" directory responce of the API
@app.get("/test")
async def test():
    # Assemble and return a timestamp string 
    def time():
        now = datetime.datetime.now()    
        timeString = now.strftime("%Y-%m-%d %H:%M:%S:%f")
        return timeString

    # Respond to the API call with a timestamp string
    while True:
        return time()
    
# Define the "returnValues" directory response of the API
@app.get("/returnValues")
async def returnValues():
        
        # Read a base voltage from ADCPi pin 1 - this measures the supply rail voltage to allow scaling of the actuator sensing measurements between 0 (ground voltage) and 1 (supply rail voltage)     
        baseVoltage = adc0.read_voltage(1)
        
        # Read all the actuator sensing data into a single sample dictionary
        # Convert each of the sensed voltages into the scaled 0-1 range 
        def createValues(baseVoltage):
            values = {
            0 : baseVoltage,
            1 : convert(adc0.read_voltage(2), baseVoltage),
            2 : convert(adc0.read_voltage(3), baseVoltage),
            3 : convert(adc0.read_voltage(4), baseVoltage),
            4 : convert(adc0.read_voltage(5), baseVoltage),
            5 : convert(adc0.read_voltage(6), baseVoltage),
            6 : convert(adc0.read_voltage(7), baseVoltage),
            7 : convert(adc0.read_voltage(8), baseVoltage)  
        }
            
            # Return the single sample dictionary
            return values
        
        # Define a function to scale the sensing data
        def convert(input, base):
            # Try the conversion
            try:
                output = input/base
            
            # Handle Divide By Zero exceptions
            except:
                output = 0
            
            # Return the scaled sensing data
            return output
            
        # Return the single sample dictionary of scaled sensing data
        return createValues(baseVoltage)
    