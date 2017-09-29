
from datetime import datetime, timedelta

class ChickenFood(object):
    corn = 1
    bread = 2
    seeds = 3
    water = 4

    def __init__(cls, intype):
        if intype == "corn":
            cls.value = cls.corn
            cls.name = "corn"
        elif intype == "bread":
            cls.value = cls.bread
            cls.name = "bread"
        elif intype == "seeds":
            cls.value = cls.seeds
            cls.name = "seeds"
        elif intype == "water":
            cls.value = cls.water
            cls.name = "water"
        else:
            raise ValueError("not a valid food")

class Chicken(object):   

    def __init__(self, name, hatch):
        print("I'm a new chicken named " + name + "!")
        self.hatched = hatch
        self.myname = name
        self.last_fed = datetime.now()
        self.next_feed = datetime.now() + timedelta(minutes = 10)
        self.fat_storage = timedelta(minutes = 10)
        self.is_alive = True

    def getLastFedTime(self):
        return self.last_fed.strftime('%Y-%m-%d %H:%M:%S')

    def getNextFedTime(self):
        return self.next_feed.strftime('%Y-%m-%d %H:%M:%S')

    def getHealth(self):
        if (self.is_alive == False):
            return "DEAD"
        elif (datetime.now() > (self.next_feed + self.fat_storage)):
            self.is_alive = False
            return "DEAD"
        return "ALIVE"

    def getIsHungry(self):
        if(self.getHealth() == "DEAD"):
            raise ValueError("Chicken is dead!")
        if (self.next_feed <= datetime.now()):
            return True
        elif (self.next_feed > datetime.now()):
            return False

    def hatch(self): 
        if self.hatched == False:
            self.hatched = True
            print(self.myname + ": I've been hatched!")
    
    def getStatus(self):
        if (self.hatched == True):
            return "Hatched"
        else:
            return "I'm an egg!"
    
    def feedChicken(self, food):
        if (self.getIsHungry() == True):
            if(type(food) is ChickenFood):
                self.last_fed = datetime.now()
                self.next_feed += timedelta(minutes = food.value)
            else:
                print("that's not chicken food, idiot!")
                return
        print("cluck cluck! I'm full!")

class Farm():
    def __init__(self):
        self.coop = []

    def addChicken(self, chick):
        if(type(chick) is Chicken):
            self.coop.append(chick)
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
        chickencount = len(self.coop)
        print("We have: " + str(chickencount) + " chickens!")    
        for chicken in self.coop:
            print("")
            print(chicken.myname + " " \
                  + "\n\t Status: " + chicken.getStatus() \
                  + "\n\t Health: " + chicken.getHealth() \
                  + "\n\t Hungry: " + str(chicken.getIsHungry()) \
                  + "\n\t Last fed: " + chicken.getLastFedTime() \
                  + "\n\t Next feeding: " + chicken.getNextFedTime())

    def checkIfHatched(self):
        for chicken in self.coop:
            if chicken.hatched == False:
                print("Don't count your chickens before they've hatched!")
                return

    def getChicken(self, name):
        for chicken in self.coop:
            if chicken.myname.lower() == name.lower():
                return chicken
        raise ValueError("I don't know a chicken by that name! ..screamed the stable boy")

    def hatchChicken(self, name):
        try:
            chicken = self.getChicken(input_name, self.coop)
            chicken.hatch()
            return True
        except ValueError, e:
            print(e)
            return False

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
    
    elif input_option == 4:
        try:
            input_name = raw_input("Name a chicken to feed: ")
            chicken = farm.getChicken(input_name)
        except ValueError, e:
            print(e)
            continue;
        try:
            infood = ChickenFood(raw_input("Choose a food: "))
            chicken.feedChicken(infood)
        except ValueError, e:
            print(e)
            continue;

    print("")
    input_from_user = raw_input("Quit? (Y / N): ")

    if input_from_user.upper() == "Y":
        avariable = False
    elif input_from_user.upper() == "N":
        avariable = True