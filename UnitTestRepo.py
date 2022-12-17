import unittest
from CONTROLLER.ctrl import *
from REPOSITORY.repo import *
from DOMAIN.event import *
from DOMAIN.person import *
from EXCEPTIONS.person_exceptions import *
from EXCEPTIONS.event_exceptions import *


class Test(unittest.TestCase):
    def setUp(self) -> None:
        Person.auto_id = 1
        Event.auto_id = 1

    def test_store(self):
        p = Person('a', 'b')
        r = InMemoryRepoPerson()
        r.store(p)
        self.assertEqual(r.person_list[0].nume, 'a')
        self.assertEqual(r.person_list[0].adresa, 'b')

    def test_stergere_pers(self):
        p = Person('a', 'b')
        print(p.id)
        r = InMemoryRepoPerson()
        r.store(p)
        r.stergere_pers(1)
        self.assertEqual(r.person_list, [])

    def test_modificare_persoana(self):
        p = Person('a', 'b')
        r = InMemoryRepoPerson()
        r.store(p)
        r.modificare_persoana(1, 'c', 'd')
        self.assertEqual(r.person_list[0].nume, 'c')
        self.assertEqual(r.person_list[0].adresa, 'd')

    def test_cautare_person(self):
        p = Person('a', 'b')
        r = InMemoryRepoPerson()
        r.store(p)
        self.assertEqual(r.cautare_persoana(1), p)

    def test_random_person_repo(self):
        r = InMemoryRepoPerson()
        r.random_person_repo()
        self.assertEqual(len(r.person_list), 1)

    def test_report_3(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert repo.report_3() == ({1: 0, 2: 0}, 0)
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_report_5(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert repo.report_5() == {1: 0, 2: 0}
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_getAll(self):
        repo = InMemoryRepoPerson()
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        assert repo.getAll() == [p1, p2]
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_store2(self):
        e = Event('11.11.2011', '11', 'a')
        r = InMemoryRepoEvent()
        r.store(e)
        self.assertEqual(r.event_list[0].data, '11.11.2011')
        self.assertEqual(r.event_list[0].timp, '11')
        self.assertEqual(r.event_list[0].descriere, 'a')

    def test_random_event_repo(self):
        r = InMemoryRepoEvent()
        r.random_event_repo()
        self.assertEqual(len(r.event_list), 1)

    def test_stergere_event(self):
        e = Event('11.11.2011', '11', 'a')
        r = InMemoryRepoEvent()
        r.store(e)
        r.stergere_event(1)
        self.assertEqual(r.event_list, [])

    def test_modificare_eveniment(self):
        e = Event('11.11.2011', '11', 'a')
        r = InMemoryRepoEvent()
        r.store(e)
        r.modificare_eveniment(1, '12.12.2012', '12', 'b')
        self.assertEqual(r.event_list[0].data, '12.12.2012')
        self.assertEqual(r.event_list[0].timp, 12)
        self.assertEqual(r.event_list[0].descriere, 'b')

    def test_cautare_eveniment(self):
        e = Event('11.11.2011', '11', 'a')
        r = InMemoryRepoEvent()
        r.store(e)
        self.assertEqual(r.cautare_eveniment(1), e)

    def test_adaugare_persoana_eveniment(self):
        p = Person('a', 'b')
        e = Event('11.11.2011', '11', 'a')
        r = InMemoryRepoEvent()
        r.store(e)
        r.adaugare_persoana_eveniment(p, e)
        self.assertEqual(e.person_list, [p])

    def test_report_1(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert repo2.report_1() == {}
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_report_2(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert repo2.report_2() == {}
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_report_4(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        print(repo2.report_4())
        assert repo2.report_4() == {3: (0, e1), 4: (0, e2)}

        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_getAllE(self):
        repo = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        repo.store(e1)
        repo.store(e2)
        assert repo.getAll() == [e1, e2]
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_white_box_testing_store(self):
        repo = InMemoryRepoPerson()
        p1 = Person('Bogdan', 'Bucuresti')
        repo.store(p1)
        self.assertEqual(repo.person_list[0].nume, 'Bogdan')
        self.assertEqual(repo.person_list[0].adresa, 'Bucuresti')
        repo.store(p1)
        self.assertEqual(repo.person_list[0].nume, 'Bogdan')
        self.assertEqual(repo.person_list[0].adresa, 'Bucuresti')
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_white_box_testing_stergere_pers(self):
        repo = InMemoryRepoPerson()
        p1 = Person('Bogdan', 'Bucuresti')
        repo.store(p1)
        repo.stergere_pers(1)
        self.assertEqual(repo.person_list, [])
        repo.stergere_pers(1)
        self.assertEqual(repo.person_list, [])
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_white_box_testing_modificare_persoana(self):
        repo = InMemoryRepoPerson()
        p1 = Person('Bogdan', 'Bucuresti')
        repo.store(p1)
        repo.modificare_persoana(1, 'Andrei', 'Focsani')
        self.assertEqual(repo.person_list[0].nume, 'Andrei')
        self.assertEqual(repo.person_list[0].adresa, 'Focsani')
        repo.modificare_persoana(1, 'Andrei', 'Focsani')
        self.assertEqual(repo.person_list[0].nume, 'Andrei')
        self.assertEqual(repo.person_list[0].adresa, 'Focsani')
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_white_box_testing_cautare_persoana(self):
        repo = InMemoryRepoPerson()
        p1 = Person('Bogdan', 'Bucuresti')
        repo.store(p1)
        self.assertEqual(repo.cautare_persoana(1), p1)
        self.assertEqual(repo.cautare_persoana(2), None)
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_white_box_testing_store_event(self):
        repo = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        repo.store(e1)
        self.assertEqual(repo.event_list[0].data, '10.10.2022')
        self.assertEqual(repo.event_list[0].timp, 10)
        self.assertEqual(repo.event_list[0].descriere, 'da')
        repo.store(e1)
        self.assertEqual(repo.event_list[0].data, '10.10.2022')
        self.assertEqual(repo.event_list[0].timp, 10)
        self.assertEqual(repo.event_list[0].descriere, 'da')
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_white_box_testing_stergere_event(self):
        repo = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        repo.store(e1)
        repo.stergere_event(3)
        print(e1)
        self.assertEqual(repo.event_list, [])
        repo.stergere_event(2)
        self.assertEqual(repo.event_list, [])
        repo.stergere_event(1)
        self.assertEqual(repo.event_list, [])
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_white_box_testing_modificare_eveniment(self):
        repo = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        repo.store(e1)
        repo.modificare_eveniment(3, '12.10.2022', 20, 'nu')
        self.assertEqual(repo.event_list[0].data, '12.10.2022')
        self.assertEqual(repo.event_list[0].timp, 20)
        self.assertEqual(repo.event_list[0].descriere, 'nu')
        repo.modificare_eveniment(3, '12.10.2022', 20, 'nu')
        self.assertEqual(repo.event_list[0].data, '12.10.2022')
        self.assertEqual(repo.event_list[0].timp, 20)
        self.assertEqual(repo.event_list[0].descriere, 'nu')
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_white_box_testing_cautare_event(self):
        repo = InMemoryRepoEvent()
        e1 = Event('10.10.2022', 10, 'da')
        repo.store(e1)
        self.assertEqual(repo.cautare_eveniment(3), e1)
        self.assertEqual(repo.cautare_eveniment(2), None)
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_black_box_testing_store_pers(self):
        repo = InMemoryRepoPerson()
        p1 = Person('Bogdan', 'Bucuresti')
        repo.store(p1)
        self.assertEqual(repo.person_list[0].nume, 'Bogdan')
        self.assertEqual(repo.person_list[0].adresa, 'Bucuresti')
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0
