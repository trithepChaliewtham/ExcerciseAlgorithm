from FindNumber import MaxsMins
from CheckDuplicateNumber import Duplicate

lists = list(map(int, input('Enter Number : ').split()))
x = MaxsMins(lists)
print(x.oddsandevens())
print(x.maxs())
[print(key,values) for key,values in Duplicate().check(0,lists).items()]