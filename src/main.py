# coding: utf-8
from datetime import datetime, timedelta
from src.getmenu import GetMenu
from src.repository.lunchmenu_repository import LunchMenuRepository
from src.learning import Leraning


class Main:
    def __init__(self):
        pass

    def getlunchmenu(self):
        getmenu = GetMenu()
        menu_array = getmenu.get_lunch_menu()
        monday_date = datetime.today().date() - timedelta(days=datetime.today().weekday())
        repository = LunchMenuRepository()

        # dbにメニューを格納していく
        for i in range(0, 5):
            date = monday_date + timedelta(days=i)
            menu = [
                menu_array['meat'][i],
                menu_array['fish'][i],
                menu_array['soup'][i],
                menu_array['side1'][i],
                menu_array['side2'][i],
                menu_array['rice1'][i],
                menu_array['rice2'][i],
                menu_array['salad'][i],
                menu_array['dessert'][i]
            ]
            repository.insertmenu(date=date, week=i, menu=menu)
        repository.getlunchmenu()
        repository.closedatabase()

    def predictcurryday(self):
        repository = LunchMenuRepository()
        currydatas = repository.getcurrydayforlearning()
        repository.closedatabase()
        learning = Leraning()
        predict_currydays = learning.predictcurryday(currydatas=currydatas)

        print(predict_currydays)


if __name__ == '__main__':
    main = Main()
    main.predictcurryday()
