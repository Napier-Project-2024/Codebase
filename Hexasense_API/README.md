# Hexasense API Documentation

The Hexasense API is built in the Python language and runs on a basic implementation of the [FastAPI Framework](https://fastapi.tiangolo.com/).

The API's main function is to respond to HTTP GET requests at the ```/returnValues``` URL with a JSON string containing the measured positions of each of the actuators in the HEXA robot's legs as a floating point value between 0 and 1.

The API will also respond to root requests with an ```index.html``` page which will display these values live in a web browser window.

These functions are achieved by using the [ADCPi library](https://github.com/abelectronicsuk/ABElectronics_Python_Libraries/tree/master/ADCPi) provided by [ABElectronics](https://www.abelectronics.co.uk/) to interface with their [ADC Pi](https://www.abelectronics.co.uk/p/69/adc-pi) 8-channel analogue to digital converter board to perform voltage readings on the ADC inputs.

The API is served using the [Uvicorn ASGI web server](https://www.uvicorn.org/) which is configured to run as a daemon upon system boot.

## The API Script

The required libraries and frameworks are imported.

```python
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
```

The ADC Pi library requires the hexadecimal I2C bus addressess of the ADC devices and the sampling bit depth to be defined.
In this instance we are using the default addresses and a bit depth of 12.

```pyhton
# Define the ADC devices' I2C addresses and sampling bit-depth
adc0 = ADCPi(0x68, 0x69, 12)
```

The FastAPI application is then defined

```python
# Define the fastAPI application
app = FastAPI()
```

Next, the root directory response of the API is defined. This function returns the ```index.html``` live data view webpage as a file response.

```python
# Define the root directory reponse of the API
@app.get("/")
async def root():    
    # Return the index.html file
    return FileResponse('index.html')
```

Finally, we define the ```/returnValues``` API response.

This function has two parts, one that creates the JSON formatted response string, and one that converts the ADC input values to a floating point value between 0 and 1.

First, the voltage value present at ADC input 1 is read as a base voltage to perform the required conversions.

```python
        # Read a base voltage from ADCPi pin 1 - this measures the supply rail voltage to allow scaling of the actuator sensing measurements between 0 (ground voltage) and 1 (supply rail voltage)     
        baseVoltage = adc0.read_voltage(1)
```

Then a ```createValues``` function is defined which assembles the JSON response by calling a ```convert``` function and supplying the ADC voltage reading for the relevant input and the base voltage reading as parameters.

```python
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
```

The ```convert``` function is then defined, taking two input parameters - an ADC input voltage, and a base voltage.

```python
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
```

This function divides the ADC input voltage by the base voltage to arrive at a value between 0 and 1.
To prevent divide-by-zero errors, a try/catch is used to account for the situation where the base voltage is read in as zero which may occur if there is a wiring error in the ADC circuit. This exception is handled by simply outputing a zero value in all instances.

The entire ```returnValues``` function then returns the assembled JSON string.

## Installation

```
sudo apt update && apt upgrade -y
```


```
sudo apt install git python3 python3-installer python3-build python3-fastapi python3-uvicorn python3.11-venv -y
```

```
cd ~
```

```
git clone -b hexasense-v0.1 --single-branch https://github.com/Napier-Project-2024/Codebase.git
```

```
cd ~/Codebase/Hexasense_API
```

```
git clone https://github.com/abelectronicsuk/ABElectronics_Python_Libraries.git
```

```
cd ABElectronics_Python_Libraries
```

```
python3 -m build
```

```
cd ~/Codebase/Hexasense_API
```

```
sudo chmod 777 hexaboot.sh
```

```
sudo cp hexaboot.sh /etc/systemd/system
```

```
sudo cp hexaboot.service /etc/systemd/system
```

```
cd ~
```

```
sudo cp -r Hexasense_API /usr
```

```
sudo systemctl enable hexaboot
```

```
sudo reboot now
```


