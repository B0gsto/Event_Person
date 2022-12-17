import copy

from DOMAIN.person import *
from DOMAIN.event import *
from datetime import datetime
from CONTROLLER.random_gen import *
from REPOSITORY.EventFileRepository import *
from REPOSITORY.PersonFileRepository import *
from REPOSITORY.RaportFisier import *
from EXCEPTIONS.person_exceptions import *
from EXCEPTIONS.event_exceptions import *


class InMemoryRepoPerson:
    def __init__(self) -> None:
        '''
        Constructor
        '''
        self.person_list = []
        self.list_list = []
        self.fisier = PersonFileRepository("person.txt")

    def store(self, p):
        '''
        Adauga o persoana noua in lista
        Test:True
        :param p: clasa Person
        :return: lista persoanelor
        '''
        try:
            for x in self.person_list:
                x: Person
                if p.nume == x.nume and p.adresa == x.adresa:
                    raise DuplicatePersonException("Id-ul exista deja!")
            self.person_list.append(p)
            self.list_list.append(p.list1)
            return self.person_list
        except DuplicatePersonException:
            print("Persoana exista deja!")

    def stergere_pers(self, id):
        '''
        Sterge o persoana dupa un id
        Test:True
        :param id: int
        :return: lista persoanelor
        '''
        for p in self.person_list:
            if int(p.id) == int(id):
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

    def random_person_repo(self):
        '''
        Genereaza persoane random
        :return:
        '''
        random_person(self)

    def get_all(self):
        '''
        Printeaza toata lista
        :return: none
        '''
        for x in self.person_list:
            print(x, end=" | ")

    def store_file(self, x):
        '''
        Salveaza in fisier
        :param x:
        :return:
        '''
        self.fisier = PersonFileRepository(x)
        self.fisier.store(self.person_list)

    def load_file(self, x):
        '''
        Citeste din fisier
        :param x:
        :return:
        '''
        self.fisier = PersonFileRepository(x)
        self.person_list = self.fisier.getAll()
        return self.person_list

    def report_3(self):
        '''
        Raport 3
        :return:
        '''
        d = {}
        maxi = -1
        for p in self.person_list:
            p: Person
            if maxi < p.no_events:
                maxi = p.no_events
            d[p.id] = p.no_events
        for k, v in d.items():
            if v == maxi:
                print(f'Persoana cu id-ul {k} are cele mai multe evenimente: {maxi}')
        return d, maxi

    def save_raport(self, x):
        '''
        Salveaza raportul in fisier
        :param x:
        :return:
        '''
        self.raport = RaportFisier(x)
        d, maxi = self.report_3()
        self.raport.store(d, maxi)

    def report_5(self):
        '''
        Raport 5
        :return:
        '''
        d = {}
        for p in self.person_list:
            d[p.id] = p.no_events
        for k, v in d.items():
            if v == 2:
                print(f'Persoana cu id-ul {k} are 2 evenimente')
        return d

    def getAll(self):
        '''
        Returneaza lista
        :return:
        '''
        return self.person_list


class InMemoryRepoEvent:
    def __init__(self):
        '''
        Constructor
        '''
        self.fisier = EventFileRepository('event.txt')
        self.event_list = []

    def store(self, e):
        '''
        Adaugare eveniment
        :param e: clasa Event
        :return: lista evenimente
        '''
        e: Event
        try:
            for x in self.event_list:
                x: Event
                if e.descriere == x.descriere and e.data == x.data and e.timp == x.timp:
                    raise DuplicateEventError("Event-ul exista deja!")
            self.event_list.append(e)
            return self.event_list
        except DuplicateEventError:
            print("Event-ul exista deja!")
        return self.event_list

    def random_event_repo(self):
        '''
        Generarea de evenimente random
        :return:
        '''
        random_event(self)

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
            if int(p.id) == int(id):
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
        Adaugarea unei persoane la un eveniment
        :param person: clasa Person
        :param event:clasa Event
        :return:lista de persoana
        '''
        person: Person
        event: Event
        try:
            for p in event.person_list:
                if p.nume == person.nume and p.adresa == person.adresa:
                    raise DuplicatePersonInEventError("Persoana exista deja!")
            event.person_list.append(person)
            person.no_events += 1
            return event.person_list
        except DuplicatePersonInEventError:
            print("Persoana exista deja!")

    def report_1(self):
        '''
        Lista de evenimente la care participă o persoană ordonat alfabetic
        :return:none
        '''
        d = {}
        for e in self.event_list:
            e: Event
            if len(e.person_list) == 1:
                d[e.descriere] = e.person_list[0], e
        d = dict(sorted(d.items()))
        for i in d.items():
            print(str(i[1][1]))
        return d

    def report_2(self):
        '''
        Lista de evenimente la care participă o persoană ordonat dupa data
        :return:none
        '''
        d = {}
        for e in self.event_list:
            e: Event
            if len(e.person_list) == 1:
                d[e.data] = e.person_list[0], e
        ordered_data = sorted(d.items(), key=lambda x: datetime.strptime(x[0], '%d.%m.%Y'))
        for i in ordered_data:
            print(str(i[1][1]))
        return d

    def report_4(self):
        '''
        Primele 20% evenimente cu cei mai mulți participanți
        :return: None
        '''
        d = {}
        for e in self.event_list:
            e: Event
            d[e.id] = len(e.person_list), e
        ordered_data = dict(sorted(d.items(), key=lambda item: item[1][0], reverse=True))
        a = int(len(self.event_list) / 5)
        print(a)
        count = 0
        for elem in ordered_data.items():
            count += 1
            print(str(elem[1][1]))
            if count >= a:
                break
        return ordered_data

    def get_all(self):
        '''
        Printeaza toata lista
        :return: none
        '''
        for x in self.event_list:
            print(x, end=" | ")

    def store_file(self, x):
        '''
        Salvarea in fisier
        :param x:
        :return:
        '''
        self.fisier = EventFileRepository(x)
        self.fisier.store(self.event_list)
        return self.event_list

    def load_file(self, x):
        '''
        Incarcarea din fisier
        :param x:
        :return:
        '''
        self.fisier = EventFileRepository(x)
        self.event_list = self.fisier.getAll()
        return self.event_list

    def getAll(self):
        '''
        Returneaza lista
        :return:
        '''
        return self.event_list
