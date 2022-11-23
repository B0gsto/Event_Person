class Menu:
    optiune = 0
    is_Ok = 1

    def __init__(self) -> None:
        self.optiune = Menu.optiune

    def start(self):
        print(self)
        try:
            optiune = int(input("Alege optiunea: "))
            self.optiune = optiune
            if optiune == 3:
                Menu.is_Ok = 0
            else:
                Menu.is_Ok = 1
            return optiune
        except:
            print("Optiune invalida")

    def __str__(self) -> str:
        return "1--Adaugă, șterge, modifică, lista de persoane, lista de evenimente " \
               "\n2--Căutare persoane, căutare evenimente " \
               "\n3--Înscriere persoană la eveniment." \
               "\n4--Rapoarte" \
               "\n5--Random"


class SubMenu:
    def __init__(self) -> None:
        self.optiune = -3

    def start(self):

        try:
            print(self)
            if Menu.is_Ok == 1:
                optiune = int(input("Alege optiunea: "))
                self.optiune = optiune
                return optiune
        except:
            print("Optiune invalida")
            return "Optiune invalida"

    def __str__(self) -> str:
        try:
            if self.optiune == 1:
                return "1--Adauga persoana \n2--Adauga eveniment \n3--Sterge persoana \n4--Sterge eveniment " \
                       "\n5--Modifica persoana \n6--Modifica eveniment "
            elif self.optiune == 2:
                return '1--Cauta persoana \n' \
                       '2--Cauta evenimente'
            elif self.optiune == 3:
                return ''
            elif self.optiune == 4:
                return '1--Lista de evenimente la care participă o persoană ordonat după descriere\n' \
                       '2--Lista de evenimente la care participă o persoană ordonat după data\n' \
                       '3--Persoane participante la cele mai multe evenimente\n' \
                       '4--Primele 20% evenimente cu cei mai mulți participanți (descriere, număr participanți)'
            elif self.optiune == 5:
                return '1--Random person\n' \
                       '2--Random event'

            else:
                return 'Optiune invalida'
        except:
            return "Optiune invalida"
