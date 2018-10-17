import threading
import time
import sys
import JulTime
import random
#Address and Name
out1='01010101' 
out2='01010102'
def outletData(name):
    voltage=random.gauss(12000,200)
    current=random.gauss(10000,1000)
    phase=random.gauss(-56,1)
    occ=1
    temp=random.gauss(20,.5)
    outError=0
    piError=0
    time1=JulTime.CalJT()
    time2=JulTime.CalJT()
    data=(name,voltage,current,phase,occ,temp,outError,piError,time1,time2)
    print(data)
    return {'voltage':voltage, 'current':current, 'phase':phase, 'occ':occ, 'temp':temp, 'outError':outError, 'piError':piError, 'time1':time1, 'time2':time2}
count=0
startLoop=True
while startLoop:
    time.sleep(4)
    try:
        thread1=threading.Thread(target=outletData,args=(out1,))
        thread1.start()
        thread2=threading.Thread(target=outletData,args=(out2,))
        thread2.start()
        count=count+1
    except:
        print>>sys.stderr,"Error: unable to start threads"
        connection.send('Connection Error')
        connection.close()
    if count==10:
        thread1.join()
        thread2.join()
        startLoop=False
