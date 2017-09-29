 
from datetime import datetime

class ChickenFood(Enum):
    corn = 1
    bread_crumbs = 2
    seeds = 3
    water = 4
    
class Chicken():   

    def __init__(self, name, hatch):
        print("I'm a new chicken named " + name + "!")
        self.hatched = hatch
        self.myname = name
        self.last_fed = datetime.now()
        self.next_feed = datetime.now() + datetime.timedelta(minutes = 10)

    def Hatch(self): 
        if self.hatched == False:
            self.hatched = True
            print(self.myname + ": I've been hatched!")
    
    def GetStatus(self):
        if (self.hatched == True):
            return "peep peep!"
        else:
            return "I'm an egg!"
    
    def FeedChicken(self, food):
        if(type(food) is ChickenFood):
            self.last_fed + datetime.timedelta(minutes = food)
        else:
            print("that's not chicken food, idiot!")

class Farm():
    def __init__(self):
        self.coop = []

    def addChicken(self, chick):
        if(type(chick) is Chicken):
            self.coop.append(chick)
            print("")
            print("cluck cluck!")
        else:
            print("that's not a chicken!")

    def createChicken(self):
        inputName = raw_input("Name a chicken: ")
        inputHatched = raw_input("Is it hatched? ")

        if inputHatched.lower() == "yes":
            hatch = True
            self.coop.append(Chicken(inputName, hatch))

        elif inputHatched.lower() == "no":
            hatch = False
            self.coop.append(Chicken(inputName, hatch))
        else:
            print("Not a valid input! ")
            self.createChicken()

    def listChickens(self):
        print("")
        chickencount = len(self.coop)
        print("we have: " + str(chickencount) + " chickens")    
        for chicken in self.coop:
            print(chicken.myname + ": " + chicken.GetStatus())

    def checkIfHatched(self):
        for chicken in self.coop:
            if chicken.hatched == False:
                print("Don't count your chickens before they've hatched!")
                return

    def getChicken(self, name):
        for chicken in self.coop:
            if chicken.myname == name:
                return chicken

    def hatchChicken(self, name):
        chicken = getChicken(input_name, self.coop)
        if(chicken == None):
            print("")
            print("I don't know a chicken by that name! ..screamed the stable boy")
            return False
        else:
            chicken.Hatch()
            return True

def PrintOptions():
    print("--- Options ---")
    print("")
    print("1: Create Chicken")
    print("2: List Chickens")
    print("3: Hatch Chicken")
    print("4: Feed Chicken")
    print("5: Quit")

def GetOptionFromUser():
    print("")
    try:
        return int(raw_input("Select Option: "))
    except ValueError:
        print("Invalid input. Please try again!")
        GetOptionFromUser()


# ----- Application --------

# ----- function end 

farm = Farm()

chicken1 = Chicken("Peaches", True)
chicken2 = Chicken("Charlie", True)
chicken3 = Chicken("Princess", True)
chicken4 = Chicken("Constantine", True)

farm.addChicken(chicken1)
farm.addChicken(chicken2)
farm.addChicken(chicken3)
farm.addChicken(chicken4)


avariable = True
while(avariable == True):
    print("")
    PrintOptions()

    input_option = GetOptionFromUser()
    print("")

    if input_option == 1:
        farm.createChicken()
        
    elif input_option == 2:
        farm.listChickens()

    elif input_option == 3:
        input_name = raw_input("Name a chicken to hatch: ")
        farm.hatchChicken(input_name)

    print("")
    input_from_user = raw_input("Quit? (Y / N): ")

    if input_from_user.upper() == "Y":
        avariable = False
    elif input_from_user.upper() == "N":
        avariable = True