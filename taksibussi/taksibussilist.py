#!/usr/bin/python3

a = ["taksibussi", False, False, "taksi", False, "bussi", "taksi", False, False, "taksi", "bussi", False, "taksi", False, False]

def taksibussi(n):
    result = a[n % 15]
    return result if result else n

if __name__ == '__main__':
    i = 1
    while i <= 100:
        print(taksibussi(i))
        i += 1
          
