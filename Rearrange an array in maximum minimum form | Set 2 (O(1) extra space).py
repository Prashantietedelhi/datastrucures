import math
ar = [1, 2, 3, 4, 5, 6, 7,8,9]
# [1+9%10*10, 2+91%10*10, 83, 13, ]
min_ind = 0
max_int = len(ar)-1
max_elem = ar[max_int]+1
for i in range(len(ar)):
    if i%2 == 0:
        ar[i] += (ar[max_int]%max_elem)*max_elem
        max_int = max_int-1
    else:
        ar[i] += (ar[min_ind] % max_elem) * max_elem
        min_ind = min_ind + 1
print(ar)
ar = [ math.floor(i/ max_elem) for i in ar]
print(ar)