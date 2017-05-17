import socket
import threading
import time
from _connection import *

######################################################################
#               Function to response from database                   #
######################################################################
def getResponse():
    db = getConnection()
    cursor = db.cursor()
    query = "SELECT signal_status FROM signal_status WHERE id_signal = (SELECT MAX(id_signal) FROM signal_status)";
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    return row[0][0];
'''
0-> negativo
1-> neutro
2-> positivo
'''
######################################################################
#          Function to receive requests from clients                 #
######################################################################
def worker(id, mutex):
    while True:
        data, addr = sock.recvfrom(8)
        print "received message:", data
        mutex.acquire()
        resp = str(getResponse())
        mutex.release()
        #resp = str(id);
        print "send message:", resp
        sock.sendto(resp, addr)
        #time.sleep(0)

######################################################################
#                           Main                                     #
######################################################################
ip = "10.0.0.1"
port = 9009
#sever socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sokect blind port
sock.bind((ip, port))
#mutex lock
mutex = threading.Lock()
#array with threads ids
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, mutex))
    threads.append(t)
    t.start()
