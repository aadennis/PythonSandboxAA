import time

def db_write():
    time.sleep(1)
    retval = 1001
    print(f"in real db_write, retval is [{retval}]")
    return retval