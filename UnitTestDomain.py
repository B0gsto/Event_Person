import unittest
from CONTROLLER.ctrl import *
from REPOSITORY.repo import *
from DOMAIN.event import *
from DOMAIN.person import *


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_black_box_testing_get_no_person(self):
        p = Person('a', 'b')
        self.assertEqual(Person.get_no_person(), 1)

    def test_black_box_testing_get_no_event(self):
        e = Event('11.11.2011', '11', 'a')
        self.assertEqual(Event.get_no_event(), 1)

    def test_black_box_testing_set_person(self):
        p = Person('a', 'b')
        p1 = p.set_person('c', 'd')
        self.assertEqual(p1.nume, 'c')
        self.assertEqual(p1.adresa, 'd')

    def test_black_box_testing_set_event(self):
        e = Event('11.11.2011', '11', 'a')
        e1 = e.set_event('11.11.2011', '11', 'b')
        self.assertEqual(e1.descriere, 'b')

    def test_white_box_testing_get_no_person(self):
        p = Person('a', 'b')
        self.assertEqual(Person.get_no_person(), 4)

    def test_white_box_testing_get_no_event(self):
        e = Event('11.11.2011', '11', 'a')
        self.assertEqual(Event.get_no_event(), 4)

    def test_white_box_testing_set_person(self):
        p = Person('a', 'b')
        p1 = p.set_person('c', 'd')
        self.assertEqual(p1.nume, 'c')
        self.assertEqual(p1.adresa, 'd')

    def test_white_box_testing_set_event(self):
        e = Event('11.11.2011', '11', 'a')
        e1 = e.set_event('11.11.2011', '11', 'b')
        self.assertEqual(e1.descriere, 'b')
