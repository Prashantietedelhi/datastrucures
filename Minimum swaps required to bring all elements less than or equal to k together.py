arr = [2, 7, 9, 5, 8, 7, 4]
k=5

count = 0
tempi = 0

for i in range(len(arr)):
    if arr[i]<=k and i!=tempi:
        arr[i],arr[tempi] = arr[tempi],arr[i]
        tempi+=1

        count+=1
    elif i==tempi and arr[i]<=k:
        tempi+=1


print((count))