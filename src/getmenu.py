# coding: utf-8
import json
from selenium.webdriver import Chrome, ChromeOptions


class GetMenu:
    def __init__(self):
        pass

    def get_lunch_menu(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        driver = Chrome(executable_path='../bin/chromedriver.exe', options=options)

        # 社食のメニューサイトへアクセスして情報を取得
        json_path = '../json/menusite.json'
        jsonfile = open(json_path, 'r')
        menusiteurl = json.load(jsonfile)['url']
        driver.get(menusiteurl)
        menu_element = driver.find_elements_by_class_name("name")

        # メニューの情報を整理
        menus = []
        last_num = len(menu_element) - 5  # ジュースの情報はいらないため"-5"して配列を調整
        for n in range(0, last_num):
            menus.append(menu_element[n].text)

        menu_array = {'meat': [], 'fish': [], 'soup': [], 'side1': [], 'side2': [], 'rice1': [], 'rice2': [], 'salad': [], 'dessert': []}
        meat_startnum = menus.index(u'肉料理') + 1
        for meat_num in range(meat_startnum, meat_startnum + 5):
            menu_array['meat'].append(menus[meat_num])

        fish_startnum = menus.index(u'魚') + 1
        for fish_num in range(fish_startnum, fish_startnum + 5):
            menu_array['fish'].append(menus[fish_num])

        soup_startnum = menus.index(u'スープ\n煮込み') + 1
        for soup_num in range(soup_startnum, soup_startnum + 5):
            menu_array['soup'].append(menus[soup_num])

        side_startnum = menus.index(u'サイド\nメニュー') + 1
        for side_num in range(side_startnum, side_startnum + 5):
            menu_array['side1'].append(menus[side_num])
            side_num += 1
            menu_array['side2'].append(menus[side_num])

        rice_startnum = menus.index(u'ごはん') + 1
        for rice_num in range(rice_startnum, rice_startnum + 5):
            menu_array['rice1'].append(menus[rice_num])
            rice_num += 1
            menu_array['rice2'].append(menus[rice_num])

        salad_startnum = menus.index(u'サラダ') + 1
        for salad_num in range(salad_startnum, salad_startnum + 5):
            menu_array['salad'].append(menus[salad_num])

        dessert_startnum = menus.index(u'デザート') + 1
        for dessert_num in range(dessert_startnum, dessert_startnum + 5):
            menu_array['dessert'].append(menus[dessert_num])

        return menu_array








