class hashfun():
    listsMod = []
    Mods = []
    Address = []
    dicts = dict()
    
    
    def __init__(self,lists):
        self.lists = lists

    def checkDup(self,x):
      
        self.count = -1

        if x > len(self.lists):
            self.dicts.update({f"Numer {self.lists[x]}":f"{self.count}"})
            return self.dicts
        elif x < len(self.lists):
            if self.dicts != {}:
                for i,v in self.dicts.items():
                    print(i,v)
                # if int(v) == 2:
                #     print("Yes")
                #     print(self.dicts[f'{i}'])

                #     # Address.append()
                # else:
                #     print("No")
                    #     continue
            else:
                for i in self.lists:
                    if self.lists[x] == i:
                        self.count += 1
                        self.dicts.update({f"Numer {self.lists[x]}":f"{self.count}"})
                x = x+1

                # recursive
                self.checkDup(x)

                return self.dicts 
                    


    def H(self,mods):
        self.mods = mods
        for i in self.lists:
            self.listsMod.append( i % self.mods )
        self.Mods.append(self.mods)
        return f'Finish Mod : {self.listsMod}'


    

    def show(self):
        from CheckDuplicateNumber import Duplicate as Dup
        self.shows = Dup().check(0,self.listsMod)
        return self.shows

    def f(self,x):
        self.H = self.H(10)
        # self.shows = self.show()
        # self.solution  = (self.H[x] + (self.shows[x]*self.shows[x])) % self.Mods[0]
        return self.solution
hash = hashfun([1,2,3,1,5,6,7,5,9])
print(hash.H(5))
print(hash.checkDup(0))
print(hash.show())

# [print(i,v) for i,v in hash.show().items()]

# print(hash.f(5))
