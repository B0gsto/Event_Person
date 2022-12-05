import copy

from DOMAIN.person import *


class PersonFileRepository:
    def __init__(self, fileName):
        self.fileName = fileName
        self.__persons = []
        self.__loadFromFile()

    def add(self, person):
        self.__persons.append(person)
        self.__storeToFile()

    def getAll(self):
        for p in self.__persons:
            p: Person
            if int(p.id) >= Person.auto_id:
                Person.auto_id = int(p.id) + 1
        return self.__persons[:]

    def __loadFromFile(self):
        try:
            f = open(self.fileName, "a")
            f.close()
            f = open(self.fileName, "r")
        except EOFError:
            # the file does not exist
            return []
        except IOError:
            print("Error loading file " + self.fileName)
            return []
        line = f.readline().strip()
        rez = []
        while line != "":
            attrs = line.split(";")
            p = Person(attrs[1], attrs[2])
            p.id = attrs[0]
            rez.append(p)
            self.__persons.append(p)
            line = f.readline().strip()
        f.close()
        return rez

    def store(self, st):
        """
        Store the student to the file.Overwrite store
        st - student
        Post: student is stored to the file
        raise DuplicatedIdException for duplicated id
        """
        self.__persons = []
        for p in st:
            p: Person
            self.__persons.append(p)
        self.__storeToFile()

    def __storeToFile(self):
        f = open(self.fileName, "w")
        for p in self.__persons:
            p: Person
            f.write(str(p.id) + ';' + str(p.nume) + ';' + str(p.adresa) + "\n")
        f.close()
