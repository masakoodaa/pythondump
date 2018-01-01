#!/usr/bin/env python3
import time

def play(n):
    if(n/3==n//3):
        if(n/5==n//5):
            return "taksibussi"
        else:
            return "taksi"
    else:
        if(n/5==n//5):
            return "bussi"
        else:
            return str(n)

if __name__ == '__main__':
    i = 1
    while True:
        print(play(i))
        time.sleep(0.1)
        i += 1
