lists = []
def nx(n,x):
    
    if (x == 1):
        ans = n
        print(f'{n} x {x} : {ans}')

    else:
        ans = n + (nx(n,x-1))
        print(f'{n} x {x} : {ans}')
    return ans
print("nx : ",nx(5,10))