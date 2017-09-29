 

class Chicken():   

    def __init__(self, name, hatch):
        print("I'm a new chicken named " + name + "!")
        self.hatched = hatch
        self.myname = name
        
    def Hatch(self): 
        if self.hatched == False:
            self.hatched = True

# ----- Application --------

chicken1 = Chicken("Peaches", True)
chicken2 = Chicken("Charlie", True)
chicken3 = Chicken("Princess", False)
chicken4 = Chicken("Constatine", False)

coop = []
coop.append(chicken1)
coop.append(chicken2)
coop.append(chicken3)
coop.append(chicken4)

print("")

chickencount = len(coop)
print("we have: " + str(chickencount) + " chickens")

print("")

for chicken in coop:
    print(chicken.myname)
    if chicken.hatched == False:
        print("Don't count your chickens before they've hatched!")



