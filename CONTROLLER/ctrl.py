from DOMAIN.person import Person
from DOMAIN.event import Event
from REPOSITORY.repo import *


class Ctrl:
    def __init__(self, repop, repoe) -> None:
        self.repop = repop
        self.repoe = repoe

    def add_person(self, nume, adresa):
        '''
               Adauga o persoana noua in lista
               Test:True
               :param p: clasa Person
               :return: lista persoanelor
               '''
        p = Person(nume, adresa)
        # self.__val.validator(s)
        self.repop.store(p)

    def stergere_persoana(self, id):
        '''
                Sterge o persoana dupa un id
                Test:True
                :param id: int
                :return: lista persoanelor
                '''
        self.repop.stergere_pers(id)

    def modificare_persoana(self, id, nume, adresa):
        '''
                Modifica o persoana dupa un id
                :param id: int
                :param nume: str
                :param adresa: str
                :return: lista persoanelor
                '''
        self.repop.modificare_persoana(id, nume, adresa)

    def cautare_persoana(self, id):
        '''
                Cauta o persoana dupa id
                :param id: int
                :return: clasa Person
                '''
        self.repop.cautare_persoana(id)

    def add_event(self, data, timp, descriere):
        '''
                Adaugare eveniment
                :param e: clasa Event
                :return: lista evenimente
                '''
        e = Event(data, timp, descriere)
        self.repoe.store(e)

    def stergere_event(self, id):
        '''
                Stergerea unui eveniment
                :param id: int
                :return: lista evenimentelor
                '''
        self.repoe.stergere_event(id)

    def modificare_eveniment(self, id, data, timp, descriere):
        '''
                Gasirea si modificarea unui eveniment dupa id
                :param id:int
                :param data:str
                :param timp:int
                :param descriere:str
                :return: lista evenimentelor
                '''
        self.repoe.modificare_eveniment(id, data, timp, descriere)

    def cautare_eveniment(self, id):
        '''
                Cautarea unui eveniment dupa id
                :param id: int
                :return: clasa Event
                '''
        self.repoe.cautare_eveniment(id)

    def show_people(self):
        '''
        Afisarea persoanelor
        :return:
        '''
        self.repop.get_all()

    def show_list(self):
        '''
        Afisarea listei de persoane
        :return:
        '''
        self.repop.get_all_list()

    def adaugare_persoana_eveniment(self, idp, ide):
        '''
                Adaugarea unei persoane la un eveniment
                :param person: clasa Person
                :param event:clasa Event
                :return:lista de persoana
        '''
        try:
            person_list = self.repop.person_list
            event_list = self.repoe.event_list
            for p in person_list:
                if p.id == idp:
                    person = p
            for e in event_list:
                if e.id == ide:
                    event = e
            self.repoe.adaugare_persoana_eveniment(person, event)
            return event_list
        except Exception as e:
            print('Eroare: ', e)

    def verificare_data(self, data):
        '''
        Verifica data daca este corecta
        :param data: str
        :return: 1/0
        '''
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
            return True
        except:
            return False

    def report_1(self):
        '''
                Lista de evenimente la care participă o persoană ordonat alfabetic
                :return:none
                '''
        self.repoe.report_1()

    def report_2(self):
        '''
                Lista de evenimente la care participă o persoană ordonat dupa data
                :return:none
                '''
        self.repoe.report_2()

    def report_3(self):
        '''
                Persoane participante la cele mai multe evenimente
                :return: none
                '''
        self.repop.report_3()

    def report_4(self):
        '''
                Persoanele care participa la 2 evenimente
        :return:
        '''
        '''
               Primele 20% evenimente cu cei mai mulți participanți
               :return: None
               '''
        self.repoe.report_4()

    def report_5(self):

        '''
                Persoanele care participa la 2 evenimente
        :return: None
        '''
        self.repop.report_5()

    def rperson(self):
        '''
        Citirea din fisier a persoanelor
        :return:
        '''
        ok = 0
        while ok == 0:
            try:
                no = int(input('Numarul de generati: '))
                ok = 1
            except:
                print('Intrare invalida')
                ok = 0
        for i in range(no):
            self.repop.random_person_repo()

    def revent(self):
        '''
        Genereaza evenimente random
        :return:
        '''
        ok = 0
        while ok == 0:
            try:
                no = int(input('Numarul de generati: '))
                ok = 1
            except:
                print('Intrare invalida')
                ok = 0
        for i in range(no):
            self.repoe.random_event_repo()

    def store_file(self):
        '''
        Salveaza in fisier
        :return:
        '''
        y = input('Persoane sau evenimente?\n'
                  '1.Persoane\n'
                  '2.Evenimente\n')
        if y == '1':
            x = input('Numele fisierului: ')
            self.repop.store_file(x)
        elif y == '2':
            x = input('Numele fisierului: ')
            self.repoe.store_file(x)
        else:
            print('Optiune invalida')

    def load_file(self):
        '''
        Incarcarea din fisier
        :return:
        '''
        y = input('Persoane sau eveniment?\n'
                  '1.Persoane\n'
                  '2.Eveniment\n')
        if y == '1':
            x = input('Numele fisierului: ')
            self.repop.load_file(x)
        elif y == '2':
            x = input('Numele fisierului: ')
            self.repoe.load_file(x)
        else:
            print('Optiune invalida')

    def save_raport(self):
        '''
        Salvarea unui raport
        :return:
        '''
        x = input('Numele fisierului: ')
        self.repop.save_raport(x)
