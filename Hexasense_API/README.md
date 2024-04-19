# Hexasense API Documentation

The Hexasense API is built in the Python language and runs on a basic implementation of the [FastAPI Framework](https://fastapi.tiangolo.com/).

The API's main function is to respond to HTTP GET requests at the ```/returnValues``` URL with a JSON string containing the measured positions of each of the actuators in the HEXA robot's legs as a floating point value between 0 and 1.
The API will also respond to root requests with an ```index.html``` page which will display these values live in a web browser window.

This is achieved using the [ADCPi library](https://github.com/abelectronicsuk/ABElectronics_Python_Libraries/tree/master/ADCPi) provided by [ABElectronics](https://www.abelectronics.co.uk/) to interface with their [ADC Pi](https://www.abelectronics.co.uk/p/69/adc-pi) 8-channel analogue to digital converter board.

The API is served using the [Uvicorn ASGI web server](https://www.uvicorn.org/) which is configured to run as a daemon upon system boot.

## The API Script




