def combin(lists,out,n,r):
    if r==0:
        print out
        return
    elif len(lists)>0:
        combin(lists[1:],out+[lists[0]],n-1,r-1)
        combin(lists[1:],out,n-1,r)
    return

lists=raw_input().split(' ')
r=input()
combin(lists,[],len(lists)-1,r)
