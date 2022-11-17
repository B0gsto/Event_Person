from UI.UI import Menu


class Console:
    def __init__(self, ctrl, menu, submenu) -> None:
        self.__ctrl = ctrl
        self.menu = menu
        self.submenu = submenu
        self.optiunea1 = -1
        self.optiunea2 = -1

    def start(self):
        '''
        Apeleaza afisarea meniului
        Setarea optiunilor
        :return: none
        '''

        op1 = self.menu.start()
        self.optiunea1 = op1
        self.submenu.optiune = op1
        op2 = self.submenu.start()
        self.optiunea2 = op2
