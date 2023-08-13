# python projetct 3
from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity   # initial value is 20
        self.pakuri = []   # when you are in the add pakuris function, you will add 1 pakuris at a time   append to end of the list # store a list of pskuti objects
        self.size = 0   # keep track of the # of concrete pakuri objects in self.pakuris

    def get_size(self):
        return len(self.pakuri)

    def get_capacity(self):
        return self.capacity
        #capacity2 = (self.capacity - len(self.pakuri))
        #return capacity2

    def get_species_array(self):
        res = []
        # loop through self.pakuri to look at each pakuri object
        if self.pakuri == []:
            return None
        else:
            for x in self.pakuri:
                # append pakuri.species to the res
                res.append(x)
            return res

    def get_stats(self, species):
        list = []
        # loop through self.pakuri to look at each pakuri object
        if species not in self.pakuri:
            return None
        else:
            for k in self.pakuri:
                # compare pakuri.species == species
                if k == species:
                    object2 = Pakuri(species)
                    # if true, return [pakuri.attack, pakuri.defence, pakuri.speed]
                    w = object2.get_attack()
                    q = object2.get_defense()
                    r = object2.get_speed()
                    list.extend([w, q, r])
                else:
                    continue
        return list

    def sort_pakuri(self):
        return self.pakuri.sort()

    # species (Ex. "pikachu") vs. pakuri object
    def add_pakuri(self, species): # the species in () is only the name of the pakuris
            # need to increment self.size when species is added
        # 1. check duplicates => return False
        if species in self.pakuri:
            return False
        # 1a. loop through self.pakuri to look at each pakuri object
            # compare pakuri.species == species
            # want to see of the species matches up with the self.pakuris []
        # then add an if-statement to see if the self.size is == to size.capacity
        if self.size == self.capacity:
            return False

        # Now how i can add pakuri # add a new pakuri object into teh list
        else:
            self.pakuri.append(species) # remove the Pakiri
            # increment self.size (becuase i know i have 1 more pakuri in my list)
            self.size += 1
            return True

    def evolve_species(self, species):
        if species in self.pakuri:
            for h in self.pakuri:
                if h == species:
                    object5 = Pakuri(h)
                    object5.evolve()
                else:
                    continue
            return True
        if species not in self.pakuri:
            return False