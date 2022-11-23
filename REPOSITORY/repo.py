from DOMAIN.person import *
from DOMAIN.event import *
from datetime import datetime
from CONTROLLER.random_gen import *


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

    def random_person_repo(self):
        random_person(self)

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

    def random_event_repo(self):
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
        Adaugarea unei persoane la un eveniment
        :param person: clasa Person
        :param event:clasa Event
        :return:lista de persoana
        '''
        event.person_list.append(person)
        return event.person_list

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

    def report_3(self):
        '''
        Persoane participante la cele mai multe evenimente
        :return: none
        '''
        d = {}
        for e in self.event_list:
            e: Event
            d[str(e)] = len(e.person_list)

        max_keys = [key for key, value in d.items() if value == max(d.values())]
        print()
        for i in max_keys:
            print(i)

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

    def get_all(self):
        '''
        Printeaza toata lista
        :return: none
        '''
        for x in self.event_list:
            print(x, end=" | ")
