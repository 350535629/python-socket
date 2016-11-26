
import socket
import select
import Queue
import time   
   
server=('10.21.17.56',9898)
   
msg=['000000','1','22','333','4444','55555']

counter = 0
while True:
    socks = []
    rs, ws, es = select.select(rlists, wlists, rlists, timeout)

    for i in range(10):
       sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socks.append(sock)

    for s in socks:
            s.connect(server)


    for m in msg:
        for s in socks:
            a=raw_input('Please enter the message:')
            s.send(a)
            print s.recv(1024)
            counter=counter+1
        for s in socks:
            data =s.recv(1024)
            print '%s echo %s' %(s.getpeername(),data)
            if not data:
                s.close()
        time.sleep(2)
