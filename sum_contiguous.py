def sum_contiguous(ls):
    curr=0
    prev=0
    for i in ls:
        curr=curr+i
        if curr>prev:
            prev=curr
        elif curr<0:
            curr=0                    
    return curr

lists=raw_input().split(' ')
intlists=[int(i) for i in lists]
neg_check=list(intlists)
neg_check.sort()
if neg_check[-1]>=0:
    print sum_contiguous(intlists)
else:
    print neg_check[-1]
