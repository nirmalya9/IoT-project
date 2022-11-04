import requests
import time
from grovepi import *
import os
sound=2;
while True:
    output=analogRead(sound)
    print(output)
    time.sleep(3)
    os.system('clear')
    url=f"https://api.thingspeak.com/update?api_key=5ECW4GV5COG88QIO&field1={output}"
    response = requests.request("GET",url)

    if 0xFF==ord('q'):
        break










