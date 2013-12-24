import re
def noncontmax(values):
    n=len(values)
    excl=0
    incl=int(values[0])
    i=1
    while i<n:
        previncl=incl
        incl=int(values[i])+excl
        excl=max(previncl,excl,0)
        i=i+1
    return max(excl,incl,0)



string=raw_input()
values=string.split(" ")
print noncontmax(values)

