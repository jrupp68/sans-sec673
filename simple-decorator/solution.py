def only_lists(function_to_decorate):
    def new_function(*args, **kwargs):
        for arg in args:
            assert isinstance(arg, list), "The argument must be a list"
        result = function_to_decorate(*args, **kwargs)
        assert isinstance(result, list), 'The returned value must be a list'
        return result
    return new_function

@only_lists
def add_lists(a,b):
    return a + b

@only_lists
def add_lists_as_tuple(a,b):
    return tuple( a + b )


if __name__=="__main__":
    print( add_lists([1,2,3], [4,5,6]) )
    print( add_lists(b = [1,2,3], a = [4,5,6]) )
    
    try:
        print( add_lists([1,2,3], 12) )
    except AssertionError as e:
        print("Successfully raised error:", str(e))
    except:
        print("Not good.  The incorrect error was raised.")
    else:
        print("Not good.  Failed to raise an AssertionError")

    try:
        print( add_lists_as_tuple([1,2,3], [1,2,3]) )
    except AssertionError as e:
        print("Successfully raised error ", str(e))
    except:
        print("Not good.  The incorrect error was raised.")
    else:
        print("Not good.  Failed to raise an AssertionError")
