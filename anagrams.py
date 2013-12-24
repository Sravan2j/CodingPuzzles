

def anagrams(lists):
    iter1=0
    lenchk=len(lists)
    while iter1<lenchk:
        i=lists[iter1]
        anagrams=[]
        nj=iter1+1
        while nj<lenchk:
            j=lists[nj]
            anag=j
            if len(i)!=len(j):
                nj=nj+1
                continue
            new1=i.split().sort()
            new2=j.split().sort()
            if new1==new2:
                anagrams.append(j)
                del lists[nj]
            lenchk=len(lists)
            nj=nj+1
        if len(anagrams)>0:
            anagrams.append(i)
            print anagrams
        iter1=iter1+1
        lenchk=len(lists)
        
            


lists=raw_input().split(' ')
anagrams(lists)
