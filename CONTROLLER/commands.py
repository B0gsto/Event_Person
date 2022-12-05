from CONTROLLER.ctrl import *


class Commands:
    def __init__(self, ctrl, op1, op2):
        self.op1 = op1
        self.op2 = op2
        self.ctrl = ctrl

    def start(self):
        '''
        Setarea submeniurilor
        :return: none
        '''
        ctrl: Ctrl
        # Adaugare persoana
        if self.op1 == 1 and self.op2 == 1:
            nume = ''
            adresa = ''
            while nume == '' or adresa == '':
                nume = str(input("Numele persoanei: "))
                adresa = str(input("Adresa persaonei: "))
                if nume == '':
                    print("Nume invalid")
                if adresa == '':
                    print("Adresa invalida")
            self.ctrl.add_person(nume, adresa)
            self.op1 = -1
            self.op2 = -1
        # Adaugare eveniment
        if self.op1 == 1 and self.op2 == 2:
            data = ''
            descriere = ''
            timp = 0
            while data == '' or descriere == '' or timp == 0 or self.ctrl.verificare_data(data) == False:

                data = str(input("Data eveniment: "))
                try:
                    timp = int(input("Durata eveniment: "))
                except:
                    pass
                descriere = str(input("Descriere eveniment: "))
                if data == '' or self.ctrl.verificare_data(data) == False:
                    print("Data invalid")
                if descriere == '':
                    print("Descriere invalida")
                if timp == 0:
                    print("Durata invalida")
            self.ctrl.add_event(data, timp, descriere)
            self.op1 = -1
            self.op2 = -1
        # Sterge persoana
        if self.op1 == 1 and self.op2 == 3:
            id = -2
            while id == -2:
                try:
                    id = int(input("Alege id-ul pentru stergerea persoanei: "))
                except:
                    print('Id invalid')
                    id = int(input("Alege id-ul pentru stergerea persoanei: "))
            self.ctrl.stergere_persoana(id)
        # Sterge eveniment
        if self.op1 == 1 and self.op2 == 4:
            id = -2
            while id == -2:
                try:
                    id = int(input("Alege id-ul pentru stergerea evenimentului: "))
                except:
                    print('Id invalid')
                    id = int(input("Alege id-ul pentru stergerea evenimentului: "))
            self.ctrl.stergere_event(id)
        # Modificare persoana
        if self.op1 == 1 and self.op2 == 5:
            id = int(input("Alege id-ul pentru modificarea persoanei: "))
            nume = str(input("Noul nume: "))
            adresa = str(input("Noua adresa: "))
            self.ctrl.modificare_persoana(id, nume, adresa)
        # Modificare eveniment
        if self.op1 == 1 and self.op2 == 6:
            id = int(input('Alege id-ul pentru modificarea evenimentului: '))
            data = str(input('Alege data noua: '))
            timp = int(input('Alege durata noua: '))
            descriere = str(input('Alege descrierea noua: '))
            self.ctrl.modificare_eveniment(id, data, timp, descriere)
        # Cautare persoana
        if self.op1 == 2 and self.op2 == 1:
            id = -1
            while id < 1:
                try:
                    id = int(input('Cauta persoana dupa id: '))
                    if id < 1:
                        print('Optiune invalida')
                except:
                    print('Optiune invalida')
            self.ctrl.cautare_persoana(id)

        # Cautare eveniment
        if self.op1 == 2 and self.op2 == 2:
            id = -1
            while id < 1:
                try:
                    id = int(input('Cauta eveniment dupa id: '))
                    if id < 1:
                        print('Optiune invalida')
                except:
                    print('Optiune invalida')
            self.ctrl.cautare_eveniment(id)
        if self.op1 == 3:
            try:
                idp = int(input('Id-ul persoanei adaugate: '))
                ide = int(input('Id-ul evenimentului la care se adauga persoana: '))
                self.ctrl.adaugare_persoana_eveniment(idp, ide)
            except:
                print('Invalid')
        if self.op1 == 4 and self.op2 == 1:
            self.ctrl.report_1()
        if self.op1 == 4 and self.op2 == 2:
            self.ctrl.report_2()
        if self.op1 == 4 and self.op2 == 3:
            self.ctrl.report_3()
        if self.op1 == 4 and self.op2 == 4:
            self.ctrl.report_4()
        if self.op1 == 4 and self.op2 == 5:
            self.ctrl.report_5()
        if self.op1 == 5 and self.op2 == 1:
            self.ctrl.rperson()
        if self.op1 == 5 and self.op2 == 2:
            self.ctrl.revent()
        if self.op1 == 6 and self.op2 == 1:
            self.ctrl.store_file()
        if self.op1 == 6 and self.op2 == 2:
            self.ctrl.load_file()
