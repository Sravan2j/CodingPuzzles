def selfread(lists):
    i=1
    length=len(lists)
    count=1
    newlist=[]
    ch=lists[0]
    while i<length:        
        if lists[i]==lists[i-1]:
            count=count+1
        else:
            newlist.append(count)
            newlist.append(lists[i-1])
            count=1
        i=i+1
    newlist.append(count)
    newlist.append(lists[i-1])
    print newlist

        

lists=raw_input().split(' ')
selfread(lists)
