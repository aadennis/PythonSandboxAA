import time

def a(duration):
    def s(duration):
        print(f"it is {duration}")
        time.sleep(duration)
        return duration * 2
    return s(duration)


def function_with_call(b, duration):
    return b(duration).s()

if __name__ == '__main__':
    c = a(3)
    assert c != None
    x = function_with_call(a, 22)
    print(x)
