import random

from DOMAIN.person import *
from DOMAIN.event import *


def random_person(person_repo):
    name_list = ['Bogdan', 'Andrei', 'Sergiu', 'Maria', 'Gabriel', 'Gabriela']
    adresa_list = ['Bucuresti', 'Galati', 'Focsani', 'Vatra Dornei', 'Bacau', 'Brasov']
    p: Person
    name = random.choice(name_list)
    adresa = random.choice(adresa_list)
    p = Person(name, adresa)
    print(p)
    person_repo.store(p)


def random_event(event_repo):
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30]
    data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    data3 = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
             2018, 2019, 2020, 2021, 2022]
    data = str(random.choice(data1)) + '.' + str(random.choice(data2)) + '.' + str(random.choice(data3))
    timp = int(random.choice(range(120)))
    descriere_list = ['Balet', 'Joc de Baschet', 'Joc de fotbal', 'Teatru']
    descriere = str(random.choice(descriere_list))
    e: Event
    e = Event(data, timp, descriere)
    event_repo.store(e)
