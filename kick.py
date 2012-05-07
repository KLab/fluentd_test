import msgpack
import socket
import time
import sys

PORT = int(sys.argv[1])

def send(msg, n=1):
    s = socket.socket()
    s.connect(('localhost', PORT))
    for _ in xrange(n):
        s.sendall(msg)
    s.close()

def attack():
    msg = msgpack.packb(['foo.bar', 333333, {"foo": "a"*1000}])
    msg *= 100
    t1 = time.time()
    while 1:
        send(msg, 25)
        t2 = time.time()
        td = t2-t1
        t1 += 0.25
        if td < 0.25:
            time.sleep(0.25 - td)

attack()
