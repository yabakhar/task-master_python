#!/usr/bin/python
import time
from daemon import runner
import os
while True :
    newpid = os.fork()
    if newpid == 0:
        os._exit(0)
    else:
        print("parent id => ", os.getpid(), "child id => ", newpid)
    reply = input("q for quit / c for new fork\n")
    if reply == 'c': 
        continue
    else:
        break