#!/usr/bin/python

import tableCreator
import sys
import sched, time
#while True:
starttime = time.time()
import random
from random import randrange
while True:
    #print("Working...")
    #tableCreator.main()
    time.sleep(4.0 - ((time.time() - starttime) % 4.0))
    #print("\nSending Data... ")
    p=random.choice([True, False])
    print(p)

