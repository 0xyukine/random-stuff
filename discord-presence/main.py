from pypresence import Presence
import threading
import signal
import time
import json
import sys

with open('config.json', 'r') as config:
    config = json.load(config)
ID = config['id']

alive = True

start_time=time.time()
delay=0#12*60*60

keys = ["pid","state","details","start","end","large_image","large_text","small_image","small_text","party_id","party_size","join","spectate","match","buttons"]

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
    global alive
    print(ID)
    print(pres)
    client_id = ID
    RPC = Presence(client_id)
    RPC.connect()
    while alive:
        RPC.update(**pres)
        time.sleep(15)
    RPC.close()

x = threading.Thread(target=presence)
x.start()

def signal_int(sig, frame):
    print("Ctrl-C received, int, killing thread")
    global alive
    alive = False

def signal_term(sig, frame):
    print("Ctrl-C received, term, killing thread")
    global alive
    alive = False

signal.signal(signal.SIGINT, signal_int)
signal.signal(signal.SIGTERM, signal_term)

while True:
    try:
        print("a")
        x = input()
        y = x.split(",")[0].strip(), x.split(",")[1].strip()
        if y[0] in keys:
            pres[y[0]] = y[1]
        else:
            print("Invalid key")
    except Exception as e:
        print(e)
        print("break loop?")
        x = input()
        if x == "Y":
            break
        else:
            pass

print("waiting to close program")
input()

class PresenceThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)
    
    def stop(self, signum=None, frame=None):
        print(signum, frame)
        self._running = False
    
    def run(self):
        global ID
        global pres

        RPC = Presence(ID)
        RPC.connect()
        while self._running:
            RPC.update(**pres)
            time.sleep(15)
        RPC.close()

if __name__ == "__main__":
    try:
        p = PresenceThread()
        p.start()
    except Exception as e:
        pass
