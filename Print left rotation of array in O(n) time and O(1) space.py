arr = [1, 3, 5, 7, 9]
r = 4
for i in range(len(arr)):
    print(arr[(i+r)%len(arr)])