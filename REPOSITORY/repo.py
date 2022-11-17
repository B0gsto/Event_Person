from DOMAIN.person import *
from DOMAIN.event import *


class InMemoryRepoPerson:
    def __init__(self) -> None:
        self.person_list = []
        self.list_list = []

    def store(self, p):
        '''
        Adauga o persoana noua in lista
        Test:True
        :param p: clasa Person
        :return: lista persoanelor
        '''
        self.person_list.append(p)
        self.list_list.append(p.list1)
        return self.person_list

    def stergere_pers(self, id):
        '''
        Sterge o persoana dupa un id
        Test:True
        :param id: int
        :return: lista persoanelor
        '''
        for p in self.person_list:
            if p.id == id:
                self.person_list.remove(p)
        return self.person_list

    def modificare_persoana(self, id, nume, adresa):
        '''
        Modifica o persoana dupa un id
        :param id: int
        :param nume: str
        :param adresa: str
        :return: lista persoanelor
        '''
        for p in self.person_list:
            if p.id == id:
                p.nume = str(nume)
                p.adresa = str(adresa)
        return self.person_list

    def cautare_persoana(self, id):
        '''
        Cauta o persoana dupa id
        :param id: int
        :return: clasa Person
        '''
        for p in self.person_list:
            if p.id == id:
                print('Persoana gasita:')
                print(p)
                return p
        print('Nu s-a gasit nicio persoana cu acest id!')

    def get_all(self):
        '''
        Printeaza toata lista
        :return: none
        '''
        for x in self.person_list:
            print(x, end=" | ")

    def get_all_list(self):
        pass


class InMemoryRepoEvent:
    def __init__(self):
        self.event_list = []

    def store(self, e):
        '''
        Adaugare eveniment
        :param e: clasa Event
        :return: lista evenimente
        '''
        self.event_list.append(e)
        return self.event_list

    def stergere_event(self, id):
        '''
        Stergerea unui eveniment
        :param id: int
        :return: lista evenimentelor
        '''
        for p in self.event_list:
            if p.id == id:
                self.event_list.remove(p)
        return self.event_list

    def modificare_eveniment(self, id, data, timp, descriere):
        '''
        Gasirea si modificarea unui eveniment dupa id
        :param id:int
        :param data:str
        :param timp:int
        :param descriere:str
        :return: lista evenimentelor
        '''
        for p in self.event_list:
            if p.id == id:
                p.data = str(data)
                p.timp = int(timp)
                p.descriere = str(descriere)
        return self.event_list

    def cautare_eveniment(self, id):
        '''
        Cautarea unui eveniment dupa id
        :param id: int
        :return: clasa Event
        '''
        for e in self.event_list:
            if e.id == id:
                print('Evenimentul gasit:')
                print(e)
                return e
        print('Nu s-a gasit niciun eveniment cu acest id!')

    def adaugare_persoana_eveniment(self, person, event):
        '''

        :param person: clasa Person
        :param event:clasa Event
        :return:lista de persoana
        '''
        event.person_list.append(person)
        return event.person_list

    def get_all(self):
        '''
        Printeaza toata lista
        :return: none
        '''
        for x in self.event_list:
            print(x, end=" | ")