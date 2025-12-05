import time


def decorator_factory():
    #Complete this decorator as outlined in the read me.
    #You should calculate elapsed time similar to the following code.
    start_time = time.process_time()
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    return elapsed_time

@decorator_factory(5,5,10)
def mysum(*args):
    return sum(args)

@decorator_factory(3,[1,2,3,4,5])
def myzip(*args):
    return list(zip(*args))
