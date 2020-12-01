listy = []
def reversed(lists,x,y):
    if x < y:
        lists = lists
        listy.append(lists[x])
        lists[x] = lists[y]
        lists[y] = listy[x]
        reversed(lists,x+1,y-1)
    else:
        pass
    return lists
    



print(reversed([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],0,16))
