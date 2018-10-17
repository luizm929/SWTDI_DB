#!/usr/bin/python

import kitchen, bedroom1, bedroom2, bedroom3, master_bedroom, garage, other_room
import living_room
import sys
import sched, time
#while True:
starttime = time.time()

while True:
    #print("Working...")
    #master_bedroom.main()
    bedroom1.main()
    #bedroom2.main()
    #bedroom3.main()
    #kitchen.main()
    #garage.main()
    #living_room.main()
    #other_room.main()
    time.sleep(4.0 - ((time.time() - starttime) % 4.0))
    print("Sending Data...\n ")
