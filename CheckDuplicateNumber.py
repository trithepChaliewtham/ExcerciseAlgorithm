
class Duplicate():
    dicts = dict()

    def check(self,x,lists):
        try:
            self.count = -1
            self.lists = lists
            if x > len(lists):
                self.dicts.update({f"Numer {lists[x]}":f"Colli is = {self.count}"})
                return self.dicts
            elif x < len(lists):
                for i in lists:
                    if lists[x] == i:
                        self.count += 1
                        self.dicts.update({f"Numer {lists[x]}":f"Colli is = {self.count}"})
                x = x+1

                # recursive
                self.check(x,self.lists)

                return self.dicts 
            else:
                
                pass
        except Exception as track:
            print()
            print("ERROR IN check(x)")
            pass



