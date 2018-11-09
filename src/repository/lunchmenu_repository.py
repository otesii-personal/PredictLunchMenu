import sqlite3


class LunchMenuRepository:
    def __init__(self):
        self.dbname = '../db/lunchmenu.sql'
        self.conn = sqlite3.connect(self.dbname)
        self.conn.text_factory = str

    def createlunchmenutable(self):
        sql = 'CREATE TABLE lunch_menu(id INTEGER PRIMARY KEY, date DATE UNIQUE, week int, meat NCHAR, fish NCHAR, soup NCHAR, side1 NCHAR, side2 NCHAR, rice1 NCHAR, rice2 NCHAR, salad NCHAR, dessert NCHAR);'
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    def insertmenu(self, date, week, menu):
        cursor = self.conn.cursor()
        try:
            sql = 'INSERT INTO lunch_menu (date, week, meat, fish, soup, side1, side2, rice1, rice2, salad, dessert) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
            data = (date, week, menu[0], menu[1], menu[2], menu[3], menu[4], menu[5], menu[6], menu[7], menu[8])
            cursor.execute(sql, data)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print('UNIQUE constraint failed: ' + date.strftime('%Y-%m-%d') + 's data already exists')

    def closedatabase(self):
        self.conn.close()

    def getlunchmenu(self):
        cursor = self.conn.cursor()
        select_sql = 'select * from lunch_menu;'
        for row in cursor.execute(select_sql):
            print(row)

    def getcurrydayforlearning(self):
        cursor = self.conn.cursor()
        res = [[], []]
        select_sql = "select week from lunch_menu where meat like '%カレー%' or fish like '%カレー%';"
        response = cursor.execute(select_sql)
        for row in response:
            # 曜日番号を元に1週間のうちのカレーの日に1をたてて格納(ex: [0,0,1,0,0,], [0,1,0,0,0], [0,0,0,0,1]...)
            week = [0, 0, 0, 0, 0]
            week[row[0]] = 1
            res[0].append(week)

            res[1].append(row[0])  # 曜日番号を配列に格納
        print(res)
        return res


if __name__ == '__main__':
    main = LunchMenuRepository()
    main.getlunchmenu()

