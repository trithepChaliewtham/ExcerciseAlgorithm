ilist = list(map(int, input("Enter Value in lists : ").split(" ")))
finds = int(input("Find number : "))

ilist = [1,2,10,12,0]

def Isearch(i, j, x):
    count = i
    if ilist[i] == x:
        return count
    elif i == j:
        return f'No value in this range {i} - {j}'
    else:
        count += 1
    return Isearch(i+1, j, x)
Isearch(0,1,10)
[print(i,end=" | ") for i in ilist]
print()

print("Result is : ",Isearch(0,2,finds))