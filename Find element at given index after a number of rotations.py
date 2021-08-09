arr =  [1, 2, 3, 4, 5]
ranges = [ [0, 2], [0, 3] ]
index = 2
for i,d in reversed(list(enumerate(ranges))):
    left = d[0]
    right = d[1]
    if index>=left and index<=right:
        if index ==left:
            index =right
        else:
            index = index-1


print(arr[index])

