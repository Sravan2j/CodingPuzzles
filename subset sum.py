def three_subset_sum(ls):
    length=len(ls)
    for i in xrange(length):
      for j in xrange(i+1,length):
         x = -(ls[i]+ls[j])
         if x in ls[j+1:]:
            return (ls[i], ls[j], x)
    return None

lists=raw_input().split(' ')
intlists=[int(i) for i in lists]
print three_subset_sum(intlists)
