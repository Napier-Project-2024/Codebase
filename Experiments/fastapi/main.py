from fastapi import FastAPI
from starlette.responses import FileResponse 
import datetime
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

adc0 = ADCPi(0x68, 0x69, 12)

app = FastAPI()


@app.get("/")
async def root():    
    return FileResponse('index.html')

@app.get("/test")
async def test():
    def time():
        now = datetime.datetime.now()    
        timeString = now.strftime("%Y-%m-%d %H:%M:%S:%f")
        return timeString

    while True:
        return time()
    
    
@app.get("/returnValues")
async def returnValues():
        baseVoltage = adc0.read_voltage(1) # Pin 1 on adc0 is used to capture the boards base voltage   

        values = {
        1 : adc0.read_voltage(2)/baseVoltage,
        2 : adc0.read_voltage(3)/baseVoltage,
        3 : adc0.read_voltage(4)/baseVoltage,
        4 : adc0.read_voltage(5)/baseVoltage,
        5 : adc0.read_voltage(6)/baseVoltage,
        6 : adc0.read_voltage(7)/baseVoltage,
        7 : adc0.read_voltage(8)/baseVoltage  
    }
    
        return json.dumps(values)
    

