#approch 1

inp = [0, 0, 1, 1, 0, 0, 0, 0 ]
k =3
j = 0
n1= 0
max = 0
curr = 0
for i in range(len(inp)):
    if inp[i] == 0 and j<k:
        j = j+1
        if n1!=0:
            curr = n1+1
        else:
            curr = curr+1
        n1 = 0

    if inp[i]==1:
        curr = curr+1
        n1 = n1+1
        j = 0


    if max<curr:
        max = curr

print(max)


