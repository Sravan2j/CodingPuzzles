f=open("B-large.in","r")
lists=f.readlines()
tests=int(lists[0])
i=1
m=1
while i<=tests:    
    values=lists[m].split(' ')
    m=m+1
    intval=[int(each) for each in values]
    A=intval[0]
    B=intval[1]
    n=0
    while n<=A:
        values=lists[m].split(' ')
        m=m+1
        perc=[float(each) for each in values]
        n=n+1
            
    k=3
    total=0
    if maxval!=0:
        while num>0:
            if intval[k]==0:
                k=k+1
                num=num-1
                continue
            x=intval[k]%3
            divval=intval[k]/3
            if x==1:            
                if maxval<=divval+1:
                    total+=1
            elif x==0:            
                if maxval<=divval:
                    total+=1
                elif maxval<=divval+1:
                    if surp>0 and (intval[k]>=2 and intval[k]<=28):
                        surp-=1
                        total+=1
            elif x==2:
                if maxval<=divval+1:
                    total+=1
                elif maxval<=divval+2:
                    if surp>0 and (intval[k]>=2 and intval[k]<=28):
                        surp-=1
                        total+=1
            k=k+1
            num=num-1
    else:
        total=num
    print "Case #%d: %d" %(i,total)
    i=i+1
