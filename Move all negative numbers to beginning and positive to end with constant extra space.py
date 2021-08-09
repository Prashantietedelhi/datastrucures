def rearrange(arr, n):
   j = 0
   for i in range(n):
       if arr[i]>0:
           arr[i],arr[j] = arr[j],arr[i]
           j+= 1

# Driver code
arr = [1,-1,3,2,-7,-5,11,6]
n = len(arr)
rearrange(arr, n)
print(arr)