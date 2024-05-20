import time

def rec_count(n):
    if n == 0:
        return
    print(n)    
    time.sleep(1)
    rec_count(n - 1)

rec_count(10)

