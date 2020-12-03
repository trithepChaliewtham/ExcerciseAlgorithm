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
    



print(reversed([4,3,6,2,6],0,4))
