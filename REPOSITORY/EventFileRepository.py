from DOMAIN.event import *


class EventFileRepository:
    def __init__(self, fileName):
        self.fileName = fileName
        self.__events = []
        self.__loadFromFile()

    def add(self, person):
        self.__events.append(person)
        self.__storeToFile()

    def getAll(self):
        for e in self.__events:
            e: Event
            if int(e.id) >= Event.auto_id:
                Event.auto_id = int(e.id) + 1
        return self.__events[:]

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
            e = Event(attrs[1], attrs[2], attrs[3])
            e.id = attrs[0]
            rez.append(e)
            self.__events.append(e)
            line = f.readline().strip()
        f.close()
        return rez

    def store(self, st):

        self.__events = []
        for e in st:
            e: Event
            self.__events.append(e)
        self.__storeToFile()

    def __storeToFile(self):
        f = open(self.fileName, "w")
        for e in self.__events:
            e: Event
            f.write(str(e.id) + ';' + str(e.data) + ';' + str(e.timp) + ';' + str(e.descriere) + "\n")
        f.close()
