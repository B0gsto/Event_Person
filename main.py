from CONTROLLER.commands import *
from CONTROLLER.ctrl import *
from DOMAIN.person import *
from REPOSITORY.repo import *
from UI.console import *
from UI.UI import *
from test_all import *

# Meniul si submeniul
menu = Menu()
submenu = SubMenu()

# Repository
repoperson = InMemoryRepoPerson()
repoevent = InMemoryRepoEvent()

# Controller
ctrl = Ctrl(repoperson, repoevent)

# Test
test = Test_all()

# Rularea programului
while True:
    con = Console(ctrl, menu, submenu)
    con.start()
    commands = Commands(ctrl, con.optiunea1, con.optiunea2)
    commands.start()
    print()
    print('Listele curente:')
    repoperson.get_all()
    print()
    repoevent.get_all()
    print()
