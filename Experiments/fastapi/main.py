from fastapi import FastAPI
from starlette.responses import FileResponse 
import datetime

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

