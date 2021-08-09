arr = [5, 8, 1, 4, 2, 9, 3, 7, 6]

arr.sort()

def swap(arr, i):
    temp = arr[len(arr)-1]
    arr.insert(1, temp)
    arr = arr[:-1]
    return arr



# for i in range(1,len(arr)):
#         print(i)
#         arr = swap(arr,i)
#
# print(arr)