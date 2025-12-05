import time
import collections


def decorator_factory(num_times, *o_args, **o_kwargs):
    def mydecorator(func_to_decorate):
        def newfunc(*args, **kwargs):
            start_time = time.process_time()
            all_results = []
            for _ in range(num_times):
                combined = dict( **o_kwargs, **kwargs)
                result = func_to_decorate(*o_args, *args)
                all_results.append(result)
            end_time = time.process_time()
            elapsed_time = end_time - start_time
            return (all_results, elapsed_time)
        return newfunc
    return mydecorator


@decorator_factory(5,5,10)
def mysum(*args):
    return sum(args)

@decorator_factory(3,[1,2,3,4,5])
def myzip(*args):
    return list(zip(*args))
