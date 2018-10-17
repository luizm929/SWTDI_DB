import socket
import time
import signal 
import sys
socket.setdefaulttimeout(1)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.settimeout(1)
sock.bind(('',2000))
sock.listen(5)
loop=True

while loop:
    try:
        connection,clientAddress=sock.accept()
        time.sleep(.1)
        data=connection.recv(1024)
        vals=data.split('x')
        name=vals[0]
        v=int(vals[1],16)*256+int(vals[2],16)
        i=int(vals[3],16)*256+int(vals[4],16)
        p=int(vals[5],16)*256+int(vals[6],16)
        t=int(vals[7],16)*256+int(vals[8],16)
        s=int(vals[9],16)*256+int(vals[10],16)
        timeO=int(vals[13],16)*256+int(vals[14],16)
        #print v
        #print i
        #print p
        #print s
        #print timeO
        connection.close()
    except:
        print('Error')

