# coding: utf-8
from src.getmenu import GetMenu


class Main:
    def __init__(self):
        pass

    def run(self):
        getmenu = GetMenu()
        menu_array = getmenu.get_lunch_menu()


if __name__ == '__main__':
    main = Main()
    main.run()




