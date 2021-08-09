from math import floor
arr=[1, 3, 6]
k=10

mid = floor(len(arr)/2)

def check_possibiliity(ar, k, val):
    ar2 = sum([val-i for i in ar ])
    if ar2<=k:
        return True

    return False


def search_val(arr, k):
    arr.sort()
    mid =  floor(len(arr)/2)
    arr2 = arr[mid:]
    startVal = min(arr2+[k,])
    endVal = max(arr2+[k,])
    lastVal = -1
    for i in range(startVal,endVal+1):
        if check_possibiliity(arr2, k, i)==True and lastVal<i:
            lastVal = i
    return lastVal

print(search_val(arr, k))
