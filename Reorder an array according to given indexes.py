arr = [50, 40, 70, 60, 90]
index = [3,  0,  4,  1,  2]
c =0
for i in range(len(arr)):
    arr[index[c]],arr[c] = arr[c],arr[index[c]]
    index[index[c]], index[c] = index[c],index[index[c]]
    if index[c]==c:
        c=c+1
print(arr)