f=open("squaredetector.txt","r")
lists=f.readlines()
tests=int(lists[0])
i=1
t=1
while t<=tests:
    size=int(lists[i])
    req=size+i
    j=0
    flag="true"
    found="false"
    startindex=0
    endindex=0
    endline=0
    startline=0
    while j<size:
        j=j+1
        i=i+1
        line=lists[i]
        k=0        
        
        for ch in line:
            k=k+1
            if ch=='#':
                if found=="false":
                    found="true"
                    startindex=k
                    startline=j
                    #print "startindex: ",startindex
                    #print "startline: ",startline
                else:
                    if (k<startindex or k>endindex or j<startline or j>endline) and endindex!=0:
                        #print "false1: ",startindex, "endindex", endindex , "startline", startline, "endline", endline
                        #print "k:", k
                        #print "j:", j
                        flag="false"
                        break
                    
            elif ch==".":
                if found=="true" and startline==j and endindex==0:
                    endindex=k-1
                    #print "endindex1: ",endindex
                    
                    
                elif found=="true":
                    if k>=startindex and k<=endindex and j>=startline and j<=endline:
                        #print "false1: ",startindex, "endindex", endindex , "startline", startline, "endline", endline
                        #print "k:", k
                        #print "j:", j
                        flag="false"
                        break            
        if flag=="false":
            break
        
        if startindex!=0 and endindex==0:
            endindex=size
            #print "endindex2: ",endindex
            
        if startline!=0 and endline==0:
            endline=endindex-startindex+startline
            #print "endline: ",endline
    
    if flag=="true":
        print "Case #%d: YES" %t
    else:
        print "Case #%d: NO" %t
        i=req
                        
    i=i+1
    t=t+1
