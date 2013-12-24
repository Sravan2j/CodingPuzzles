def calc(list1,res1,list2,res2,lists,n,total):
    global flag
    if flag=='y':
        return 0
    if res1==res2:
        
        print ' '.join(str(i) for i in list1)
        print ' '.join(str(i) for i in list2)
        flag='y'        
        return 0      
    if n==20:
        return 0
    if res1+lists[n]<total:        
        calc(list1+[lists[n]],res1+lists[n],list2,res2,lists,n+1,total)
    if res2+lists[n]<total:
        calc(list1,res1,list2+[lists[n]],res2+lists[n],lists,n+1,total)    
    calc(list1,res1,list2,res2,lists,n+1,total)
    return 0

flag='n'
f=open("C-small.in","r")
lists=f.readlines()
tests=int(lists[0])
i=1
#check=2**20
#check=check-1
while i<=tests:
    values=lists[i].split(' ')        
    intval=[int(each) for each in values]
    a=intval[0]
    k=1
    totsum=0
    while k<=a:
        totsum=totsum+intval[k]
        k=k+1
    del intval[0]
    par1=[]
    print "Case #%d:" %i
    flag=calc(par1+[intval[0]],intval[0],[],0,intval,1,totsum/2)            
    if flag=='n':
        print "Impossible"
    i=i+1
        


