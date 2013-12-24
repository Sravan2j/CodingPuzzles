def subsets(lst):
    if(len(lst) == 1):
        return [lst]
    else:
        a = subsets(lst[1:])
        c = [[lst[0]]]
        #print "a:", a
        #print "c:", c
        for elem in a:
            b = elem + [lst[0]]
            c.append(elem)
            c.append(b)
        return c

lists=[1,2,3,4,5]
print subsets(lists)
