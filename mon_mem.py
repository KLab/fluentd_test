import sys
import time

def monitor(pid):
    fn = "/proc/%s/status" % pid
    while 1:
        with open(fn) as f:
            lines = f.readlines()
        for L in lines:
            if L.startswith('VmRSS'):
                #print L
                print L.split()[1]
        time.sleep(1.1)

monitor(sys.argv[1])
