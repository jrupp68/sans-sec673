
def to_timezone_factory(strptime_string):
    def new_function(string_to_process, destination_timezone):
        #convert to tz aware timestamp with +z and -HHMM
        #use zoneinfo to creat tzinfo rec for destination_timezone
        #use as_timezone( ) and zoneinfo rec
        return new_datetime
    return new_function

#myfunc = to_timezone_factory("%d/%b/%Y:%H:%M:%S %z")
#myfunc('14/Sep/1990:12:47:07', Iran)


##Can decorator version??

