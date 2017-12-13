# Class Person

import datetime #needed for Class Person
 
#Class Person
class Person(object):

    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(' ') #returns last index where substring ' ' is found
            self.lastName = name[lastBlank+1:] # returns last name
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """Returns self's full name"""
        return self.name

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
            Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError # raise value error if no birthday for self
        return (datetime.date.today() - self.birthday).days # age in number of days

    def __lt__(self, other): # overloads the < operator
        """Returns True if self's name is lexicographically
            less than the other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """Returns self's name"""
        return self.name


# Class WCPerson
class WCPerson(Person):

    nextIdNum = 0  # identification number # class variable

    def __init__(self, name):
            Person.__init__(self, name) #overwrote __init__ of class person
            self.idNum = WCPerson.nextIdNum
            # nextIdNum is a class variable,
            # belongs to Class WCPerson, not instance of class
            WCPerson.nextIdNum += 1

    def getIdNum(self):
            return self.idNum

    def __lt__(self, other): # overwrote __lt__ of class person
            return self.idNum < other.idNum # changes it to be based off ID number instead or name

    def isStudent(self):
            return isinstance(self, Student)


#Class Student
class Student(WCPerson):
    pass


#Class UG
class UG(Student):
    def __init__(self, name, classYear):
        WCPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


#Class Grad
class Grad(Student):
    pass


