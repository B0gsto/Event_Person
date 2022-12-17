from CONTROLLER.ctrl import *
from REPOSITORY.repo import *
from UI.console import *
from UI.UI import *


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

    def test_adaugare_persoana_eveniment(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        ctrl.adaugare_persoana_eveniment(1, 1)
        assert ctrl.adaugare_persoana_eveniment(1, 1) == repo2.event_list
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_stergere_persoana(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        ctrl.stergere_persoana(1, 1)
        assert ctrl.stergere_persoana(1, 1) == repo2.event_list
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_cautare_persoana(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        assert ctrl.cautare_persoana('Bogdan') == repo.person_list
        Person.no_person = 0
        Person.auto_id = 0

    def test_modificare_eveniment(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.modificare_eveniment(1, '11.11.2022', 11, 'XD') == repo2.event_list
        Event.no_event = 0
        Event.auto_id = 0

    def test_cautare_eveniment(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.cautare_eveniment('12.10.2022') == repo2.event_list
        Event.no_event = 0
        Event.auto_id = 0

    def test_show_list(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.show_list() == repo2.event_list
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_verificare_data(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.verificare_data('10.10.2022') == True
        Event.no_event = 0
        Event.auto_id = 0

    def test_rperson(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        assert ctrl.rperson() == repo.person_list
        Person.no_person = 0
        Person.auto_id = 0

    def test_revent(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.revent() == repo2.event_list
        Event.no_event = 0
        Event.auto_id = 0

    def test_report_1(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.report_1() == repo2.event_list
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_report_2(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.report_2() == repo2.event_list
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_report_3(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.report_3() == repo2.event_list
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_report_4(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.report_4() == repo2.event_list
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

    def test_report_5(self):
        repo = InMemoryRepoPerson()
        repo2 = InMemoryRepoEvent()
        ctrl = Ctrl(repo, repo2)
        e1 = Event('10.10.2022', 10, 'da')
        e2 = Event('12.10.2022', 20, 'nu')
        p1 = Person('Bogdan', 'Bucuresti')
        p2 = Person('Andrei', 'Focsani')
        repo.store(p1)
        repo.store(p2)
        repo2.store(e1)
        repo2.store(e2)
        assert ctrl.report_5() == repo2.event_list
        Person.no_person = 0
        Person.auto_id = 0
        Event.no_event = 0
        Event.auto_id = 0

