from pypresence import Presence
import threading
import time
import json

with open('config.json', 'r') as config:
    config = json.load(config)
ID = config['id']

start_time=time.time()
delay=0#12*60*60

default = {
    "pid":None,
    "state":"68 69 66 75 6D 69",
    "details":None,
    "start":start_time-delay,
    "end":None,
    "large_image":"nana3",
    "large_text":None,
    "small_image":None,
    "small_text":None,
    "party_id":None,
    "party_size":None,
    "join":None,
    "spectate":None,
    "match":None,
    "buttons":None
}

pres = default

print("Update default fields: Y/N")
res = input()

if res == "Y":
    print("Load from file")
    res = input()
    if res == "Y":
        pass
    elif res == "N":
        for key,value in list(pres.items()):
            print(key)
            new_val = input()
            if value is None and new_val == "":
                del pres[key]
            else:
                pres[key] = new_val
elif res == "N":
    for key,value in list(pres.items()):
        if value is None:
            del pres[key]
else:
    pass

def presence():
    global ID
    global pres
    print(ID)
    print(pres)
    client_id = ID
    RPC = Presence(client_id)
    RPC.connect()
    while True:
        RPC.update(**pres)
        time.sleep(15)

x = threading.Thread(target=presence)
x.start()

while True:
    time.sleep(1)