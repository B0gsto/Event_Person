import unittest
from CONTROLLER.ctrl import *
from REPOSITORY.repo import *
from EXCEPTIONS.person_exceptions import *
from EXCEPTIONS.event_exceptions import *


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.__ctrl = Ctrl(InMemoryRepoPerson(), InMemoryRepoEvent())
        Person.no_person = 0
        Person.no_list = 0
        Person.auto_id = 1
        Event.no_event = 0
        Event.auto_id = 1

    def test_black_box_testingadd_person(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_black_box_testingstergere_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.stergere_persoana(1)
        self.assertEqual(len(self.__ctrl.repop.getAll()), 0)

    def test_black_box_testing_modificare_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.modificare_persoana(1, "Diana", "Strada")
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_black_box_testing_cautare_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.cautare_persoana(1)
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_black_box_testing_add_event(self):
        self.__ctrl.add_event("12.12.2020", "12:00", "Eveniment")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_black_box_testing_stergere_event(self):
        self.__ctrl.add_event("12.12.2020", "12:00", "Eveniment")
        self.__ctrl.repoe.get_all()
        self.__ctrl.stergere_event(1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 0)

    def test_black_box_testing_modificare_event(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.modificare_eveniment(1, "12.12.2020", "12", "Eveniment")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_black_box_testing_cautare_event(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.cautare_eveniment(1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_black_box_testing_adaugare_persoana_eveniment(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.adaugare_persoana_eveniment(1, 1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_black_box_testing_verificare_data(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.verificare_data("12.12.2020")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_white_box_testing_add_person(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)
        self.__ctrl.add_person("Diana", "Strada")
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_white_box_testing_stergere_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.stergere_persoana(1)
        self.assertEqual(len(self.__ctrl.repop.getAll()), 0)
        self.__ctrl.stergere_persoana(1)
        self.assertEqual(len(self.__ctrl.repop.getAll()), 0)

    def test_white_box_testing_modificare_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.modificare_persoana(1, "Diana", "Strada")
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)
        self.__ctrl.modificare_persoana(1, "Diana", "Strada")
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_white_box_testing_cautare_persoana(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.cautare_persoana(1)
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)
        self.__ctrl.cautare_persoana(2)
        self.assertEqual(len(self.__ctrl.repop.getAll()), 1)

    def test_white_box_testing_add_event(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)
        self.__ctrl.add_event("12.12.2020a", "12a", "Eveniment")
        self.__ctrl.stergere_event(1)

    def test_white_box_testing_stergere_event(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.repoe.get_all()
        self.__ctrl.stergere_event(1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 0)
        self.__ctrl.stergere_event(1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 0)

    def test_white_box_testing_modificare_event(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.modificare_eveniment(1, "12.12.2020", "12", "Eveniment")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)
        self.__ctrl.modificare_eveniment(1, "12.12.2020", "12", "Eveniment")
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_white_box_testing_cautare_event(self):
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.cautare_eveniment(1)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)
        self.__ctrl.cautare_eveniment(2)
        self.assertEqual(len(self.__ctrl.repoe.getAll()), 1)

    def test_white_box_testing_adaugare_persoana_eveniment(self):
        self.__ctrl.add_person("Diana", "Strada")
        self.__ctrl.add_event("12.12.2020", "12", "Eveniment")
        self.__ctrl.adaugare_persoana_eveniment(1, 1)
        self.assertEqual(len(self.__ctrl.repoe.event_list[0].person_list), 1)
        self.__ctrl.adaugare_persoana_eveniment(1, 1)
        self.assertEqual(len(self.__ctrl.repoe.event_list[0].person_list), 1)
