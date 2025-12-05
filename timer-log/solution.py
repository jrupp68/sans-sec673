import time
import collections
from functools import wraps
import time

def define_a_function_to_create_a_decorated_timed_function_here():
    #Complete this decorator as outlined in the README.md.
    #You should calculate elapsed time using time.time() not time.process_time()
    #create a variable named exec_times that is a deque that has a maximum length of 10
    #Start a definition for a new function called new_function it should just collect up all of its arguments and keyword argument
        #You will have to be able to update the deque called exec_times so declare it as 'nonlocal'
        #record the current time in a variable called start_time
        #Call the function that was passed to this funcion (that you are decorating). Pass on the arguments you collected and capture its result
        #calculate how much time elapsed since you executed the function.
        #add the calculated elapsed time to the end of your exec_times deque
        #Return the results of the decorated function
    #Start the definition for a new function named times.  It takes no arguments.
        #It should return the values in your exec_times deque as a list
    #Attach the times function to the new_function function as an attribute
    #Attach the exec_times deque to the new_function function as an attribute
    #return the new function
    #Remove th next line it isn't needed after you write your (much better) function.
    start_time = time.time()

@timer_log
def mysum(*args):
    result = sum(args)
    time.sleep( (result %2) + 1)
    return result


@timer_log
def sleep(seconds):
    time.sleep(seconds)


if __name__ == "__main__":
    print(mysum(10,5,100))
    print(mysum(1,2,3,4,5,6))
    print(mysum.times())
    sleep(0.2)
    sleep(0.5)
    sleep(0.6)
    print(sleep.times())
    assert len(sleep.times())==3, "The incorrect number of times were recorded."
    for i in range(15):
        sleep(0.001)
    assert len(sleep.times())==10, "The incorrect number of times were recorded."