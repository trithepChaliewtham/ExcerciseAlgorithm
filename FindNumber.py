class MaxsMins():
    def __init__(self,lists):
        self.lists = lists

    def maxs(self):
        self.maxs= self.lists[0]
        for i in range(len(self.lists)):
            if  self.maxs < self.lists[i]:
                self.maxs = self.lists[i]
            else:
                pass
        return f'Max : {self.maxs}'


    def oddsandevens(self):
        
        self.oddslists = []
        self.evenslists = []
        for i in self.lists:
            if  i % 2 == 1 :
                self.oddslists.append(i) 
            elif i % 2 == 0:
                self.evenslists.append(i)
            else:
                pass
        return f'Odd : {self.oddslists}\nEvens : {self.evenslists}'
    def mins(self):
        self.mins = self.lists[0]
        for i in range(len(self.lists)):
            if  self.mins > self.lists[i]:
                self.mins = self.lists[i]
            else:
                pass
        return f'Mins : {self.mins}'
