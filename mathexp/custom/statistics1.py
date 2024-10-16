# This is an example library, containing some basic statistics functions
def mean(args:list)-> int|float:
    return sum(args)/len(args)
def median(args:list)->int|float:
    return float(sorted(args)[int(((len(args)+1)/2)-1)]) if len(args)%2!=0 else (sorted(args)[int((len(args)/2))-1]+sorted(args)[int((len(args)/2+1)-1)])/2
def range_s(args:list)->int|float:
    return max(args)-min(args)