arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
count = 0
for i in range(len(arr)):
    if arr[i]<0:
        arr[i],arr[count] = arr[count],arr[i]
        count +=1
print(arr)