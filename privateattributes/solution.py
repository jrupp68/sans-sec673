from private_attributes import secure1, secure2, secure3


def secure1_value(in_object):
    in_object.admin = False  #pyWars.solution() will ignore changing this to True
    val = in_object._Secure1__the_actual_variable   #You must retrieve this while admin is False
    return val

def secure2_value(in_object):
    in_object.admin = False  #pyWars.solution() will ignore changing this to True
    val = type(in_object).__dict__['value']._PrivateAttrib__value   #You must retrieve this while admin is False
    return val

def secure3_value(in_object):
    in_object.admin = False  #pyWars.solution() will ignore changing this to True
    type(in_object).__getattribute__ = object.__getattribute__
    val = in_object.value
    return val



print("The value for secure1 is ", secure1_value(secure1))

print("The value for secure2 is ", secure2_value(secure2))

print("The value for secure3 is ", secure3_value(secure3))
