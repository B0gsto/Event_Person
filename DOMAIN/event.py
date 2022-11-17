class Event:
    no_event = 0
    auto_id = 0

    def __init__(self, data, timp, descriere):
        self.id = Event.auto_id
        self.data = data
        self.timp = timp
        self.descriere = descriere
        self.person_list = []
        Event.auto_id += 1
        Event.no_event += 1

    @staticmethod
    def get_no_event():
        '''
        Numarul de evenimente
        :return: int
        '''
        return Event.no_event

    def get_event(self):
        '''
        Evenimentul apelat
        :return: clasa Event
        '''
        return self

    def set_event(self, data, timp, descriere):
        '''
        Seteaza un Eveniment
        :param data: str
        :param timp: str
        :param descriere:str
        :return: clasa Event
        '''
        e = Event(data, timp, descriere)
        return e

    def __str__(self):
        '''
        Printarea evenimentului
        :return: str(event)
        '''
        return 'ID:' + str(self.id) + ' Data:' + str(self.data) + ' Descriere:' + str(
            self.descriere) + ' Durata:' + str(
            self.timp) + ' Lista persoane:' + str([str(item) for item in self.person_list])

    def __eq__(self, other):
        '''
        Verificare daca 2 evenimente sunt la fel
        :param other: class Event
        :return: bool
        '''
        return self.descriere == other.descriere and self.timp == other.timp and self.data == other.data
