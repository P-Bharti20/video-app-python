import socket 
import time
import threading

irecv_s=socket.socket()
irecv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1) #this is done so that we can reuse a port, otherwise everytime we have 
#to kill service because till some time port is remains active

iirecv_s=socket.socket()
iirecv_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

isend_s=socket.socket()
isend_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

iisend_s=socket.socket()
iisend_s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

irecv_port=2024 #recive from Aman Dev Verma
iirecv_port=2025 #recive from Manasvi Agarwal
isend_port=2026 #send to Aman Dev Verma
iisend_port=2027 #send to Manasvi Agarwal
ip=
irecv_s.bind((ip, irecv_port))
iirecv_s.bind((ip, iirecv_port))
isend_s.bind((ip, isend_port))
iisend_s.bind((ip, iisend_port))

irecv_s.listen()
iirecv_s.listen()
isend_s.listen()
iisend_s.listen()

irecv_session, irecv_addr = irecv_s.accept()
iirecv_session, iirecv_addr = iirecv_s.accept()
isend_session, isend_addr = isend_s.accept()
iisend_session, iisend_addr = iisend_s.accept()

#above we have created total 4 socket 1) it will recive image in bytes from person2
#2)it will send those bytes recived by person2 to the person1
#3)it will recive image in bytes from person1
#2)it will send those bytes recived by person1 to the person2
def irecv() #it will recive from kalyani and send to Manasvi
    while True
        data=irecv_session.recv(10000000)
        time.sleep(0.8)
        iisend_session.send(data)

def iirecv() #it will recive from sudhanshu and send to Aman
    while True
        data=iirecv_session.recv(10000000)
        time.sleep(0.8)
        isend_session.send(data)
#used threading so that above both function will run parellely
i_recv=threading.Thread(target=irecv)
ii_recv=threading.Thread(target=iirecv)
i_recv.start()
ii_recv.start()
