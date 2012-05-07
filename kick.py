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
    while 1:
        t1 = time.time()
        send(msg, 100)
        t2 = time.time()
        time.sleep(1 - (t2-t1))

attack()
