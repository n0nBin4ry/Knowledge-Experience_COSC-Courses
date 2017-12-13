# OBJECTS a are collection of data and methods that operate on that data
# ABSTRACT DATA TYPE: set of objects and operations on those objects
# python implements data abstraction using classes
class IntSet(object): # creates a 'type'
    """An IntSet is a set of integers"""
    #Information about implementation (not the abstraction)
    #The value of the set is represented by a list of ints, self.vals
    #Each int in the set occurs in self.vals exactly once
    def __init__(self):
        """creates empty set of integers"""
        self.vals = []

    def insert(self, e):
        """assumes e is an integer and inserts e into self"""
        if e not in self.vals: # was: if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        """asumes e is an integer
        returns True if e is in self, and False otherwise"""
        return e in self.vals
    def remove(self, e):
        """assumes e is an integer and removes e from self
        raises valueError if e not in self"""
        try:
            self.val.remove(e)
        except:
            raise ValueError(str(e) + 'not found')
    def getMembers(self):
        """returns a list containing the elements of self,
        nothing can be assumed about the order or elements"""
        return self.vals[:]
    def __str__(self):
        "returns a string representation of self"
        self.vals.sort()
        result = ''
        for e in self.vals:
            if e == self.vals[0]:
                result += '[ ' + str(e) + ' , '
            elif e == self.vals[len(self.vals) - 1]:
                result += str(e) + ' ]'
            else:
                result += str(e) + ' , '
        return result


#Two kinds of operations supposed by classes:
    # 1. Instantiation: used to create an instance of a class
        # EG: >> S = IntSet()
            #creates a new object called an instance of IntSet, makes a class called 'S'
    # 2. Attribute references:
        #Attribution References: use a dot notation to acces attributes associated with class
        # EG: s.member is an access member attribute in instance of class IntSet