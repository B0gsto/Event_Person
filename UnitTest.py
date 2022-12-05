import unittest
from CONTROLLER.ctrl import *
from REPOSITORY.repo import *


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.__ctrl = Ctrl(InMemoryRepoPerson(), InMemoryRepoEvent())
        Person.no_person = 0
        Person.no_list = 0
        Person.auto_id = 1
        Event.no_event = 0
        Event.auto_id = 1

    def test_add_person(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_stergere_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.stergere_persoana(1)
        self.assertEqual(len(self.__ctrl.repop.getAll()), 0)

    def test_modificare_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.modificare_persoana(1, "Diana", "Strada")
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_cautare_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.cautare_persoana(1)
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_add_event(self):
        self.__ctrl.add_event("12.12.2020", "12:00", "Eveniment")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_stergere_event(self):
        self.__ctrl.add_event("12.12.2020", "12:00", "Eveniment")
        self.__ctrl.repoe.get_all()
        self.__ctrl.stergere_event(1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 0)

    def test_modificare_event(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.modificare_eveniment(1, "12.12.2020", "12", "Eveniment")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_cautare_event(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.cautare_eveniment(1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_adaugare_persoana_eveniment(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.adaugare_persoana_eveniment(1, 1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_verificare_data(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.verificare_data("12.12.2020")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)
