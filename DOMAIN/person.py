class Person:
    no_person = 0
    auto_id = 0

    def __init__(self, nume, adresa) -> None:
        self.id = Person.auto_id
        self.nume = nume
        self.adresa = adresa
        self.list1 = [nume, adresa]
        Person.no_person += 1
        Person.auto_id += 1

    @staticmethod
    def get_no_person():
        '''
        Numarul de persoane
        :return: int
        '''
        return Person.no_person

    def get_person(self):
        '''
        Returneaza instanta apelata
        :return:clasa Person
        '''
        return self

    def set_person(self, nume, adresa):
        '''
        Seteaza o persoana
        :param nume: str
        :param adresa: str
        :return: clasa Person
        '''
        p = Person(nume, adresa)
        return p

    def __str__(self) -> str:
        '''
        Printarea persoanei
        :return: str
        '''
        return "ID:" + str(self.id) + " Nume:" + str(self.nume) + " Adresa:" + str(self.adresa)

    def __eq__(self, __o: object) -> bool:
        '''
        Verificare 2 persoane sunt la fel
        :param __o: clasa Person
        :return: bool
        '''
        return self.nume == __o.nume and self.adresa == __o.adresa
