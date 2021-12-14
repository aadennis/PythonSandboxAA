import time

def f_a():
    """
        The function under test. The real version of this is called by the test,
        but the mocked version of f_b() should be called
    """
    return f_b() + 1

def f_b():
    """
        The function to be replaced by a mock at test run time. Why replace? 
        Because it is long-running, third party, network-dependent, etc. 
        If the mock/patch does its job, the duration of the test run will be 
        short, and certainly not the 3 seconds imposed by the sleep.
    """
    time.sleep(3)
    return 22