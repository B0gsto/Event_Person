from CONTROLLER.ctrl import *
from REPOSITORY.repo import *


class Test_all:
    def test_all(self):
        self.test_add_person()
        self.test_sterge_persoana()
        self.test_modificare_persoana()
        self.test_add_event()
        self.test_stergere_event()
        self.test_modificare_event()
        Person.auto_id = 1
        Event.auto_id = 1

    def test_add_person(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        p = Person('Bogdan', 'Bucuresti')
        repo.person_list.append(p)
        assert ctrl.repop.store(p) == repo.person_list
        Person.no_person = 0
        Person.auto_id = 0

    def test_sterge_persoana(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        id = 1
        repo.person_list.append(p1)
        repo.person_list.append(p2)
        ctrl.repop.stergere_pers(id=1)
        assert ctrl.repop.stergere_pers(id) == repo.person_list
        Person.no_person = 0
        Person.auto_id = 0

    def test_modificare_persoana(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        id = 1
        repo.person_list.append(p1)
        repo.person_list.append(p2)
        ctrl.repop.modificare_persoana(id, nume='Gabriel', adresa='Botosani')
        assert ctrl.repop.modificare_persoana(id, nume='Gabriel', adresa='Botosani') == repo.person_list
        Person.no_person = 0
        Person.auto_id = 0

    def test_add_event(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e = Event('10.10.2022', 10, 'E frumos')
        repo2.store(e)
        assert ctrl.repoe.store(e) == repo2.event_list
        Event.no_event = 0
        Event.auto_id = 0

    def test_stergere_event(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        repo2.store(e1)
        repo2.store(e2)
        ctrl.repoe.stergere_event(1)
        assert ctrl.repoe.stergere_event(1) == repo2.event_list
        Event.no_event = 0
        Event.auto_id = 0

    def test_modificare_event(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.repoe.modificare_eveniment(1, '11.11.2022', 11, 'XD') == repo2.event_list
