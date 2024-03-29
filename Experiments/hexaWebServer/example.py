import datetime

def time():
    now = datetime.datetime.now()    
    timeString = now.strftime("%Y-%m-%d %H:%M:%S:%f")
    return timeString

while True:
    print(time())
