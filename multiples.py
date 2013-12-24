numbers = [1]
next_2 = 0
next_5 = 0
for i in xrange(100):
    mult_2 = numbers[next_2]*2
    mult_5 = numbers[next_5]*5
    if mult_2 < mult_5:
       next = mult_2
       next_2 += 1
    else:
       next = mult_5
       next_5 += 1

     # The comparison here is to avoid appending duplicates
    if next > numbers[-1]:
       numbers.append(next)

print numbers
