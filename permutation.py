def permutation(lists,length,boolean,output,check):
    if check==length:
        print output
        return
    else:
        i=0
        while i<length:
            if boolean[i]==True:
                i=i+1
                continue
            output.append(lists[i])
            boolean[i]= True
            permutation(lists,length,boolean,output,check+1)            
            boolean[i]= False
            output.pop()
            i=i+1

lists=raw_input().split(' ')
boolean=[False]*len(lists)
output=[]
#print boolean
permutation(lists,len(lists),boolean,output,0)
