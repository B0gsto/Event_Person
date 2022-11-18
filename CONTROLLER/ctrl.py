from DOMAIN.person import Person
from DOMAIN.event import Event
from REPOSITORY.repo import *


class Ctrl:
    def __init__(self, repop, repoe) -> None:
        self.repop = repop
        self.repoe = repoe

    def add_person(self, nume, adresa):
        p = Person(nume, adresa)
        # self.__val.validator(s)
        self.repop.store(p)

    def stergere_persoana(self, id):
        self.repop.stergere_pers(id)

    def modificare_persoana(self, id, nume, adresa):
        self.repop.modificare_persoanaa(id, nume, adresa)

    def cautare_persoana(self, id):
        self.repop.cautare_persoana(id)

    def add_event(self, data, timp, descriere):
        e = Event(data, timp, descriere)
        self.repoe.store(e)

    def stergere_event(self, id):
        self.repoe.stergere_event(id)

    def modificare_eveniment(self, id, data, timp, descriere):
        self.repoe.modificare_eveniment(id, data, timp, descriere)

    def cautare_eveniment(self, id):
        self.repoe.cautare_eveniment(id)

    def show_people(self):
        self.repop.get_all()

    def show_list(self):
        self.repop.get_all_list()

    def adaugare_persoana_eveniment(self, idp, ide):
        person_list = self.repop.person_list
        event_list = self.repoe.event_list
        for p in person_list:
            if p.id == idp:
                person = p
        for e in event_list:
            if e.id == ide:
                event = e
        self.repoe.adaugare_persoana_eveniment(person, event)

    def verificare_data(self, data):
        a = data.split('.')
        try:
            if len(a) != 3:
                return 0
            if int(a[0]) < 0 or int(a[0]) > 32:
                return 0
            if int(a[1]) < 0 or int(a[1]) > 12:
                return 0
            if int(a[2]) < 2000:
                return 0
            return 1
        except:
            return 0

    def report_1(self):
        print(self.repoe.report_1())

    def report_2(self):
        pass

    def report_3(self):
        pass

    def report_4(self):
        pass
