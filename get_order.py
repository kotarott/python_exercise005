import os
import pandas as pd
# import datetime

# クラスの定義
class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price
    
    def get_price(self):
        return self.price

class Order:
    def __init__(self,item_master):
        self.item_order_list = []
        self.item_master = item_master
        self.item_total_price = 0
        self.payment = 0
        self.orders = []

    def add_item_order(self,item_code, item_num):
        self.item_order_list.append([item_code, item_num])
        
    def view_item_list(self):
        self.orders = []
        for item in self.item_order_list:
            for master in self.item_master:
                if item[0] == master.item_code:
                    self.orders.append([item[0], master.item_name, master.get_price(), item[1], master.get_price() * item[1]])
        return self.orders
    
    def calc_total_price(self):
        self.item_total_price = 0
        for item in self.item_order_list:
            for master in self.item_master:
                if item[0] == master.item_code:
                    self.item_total_price += item[1] * master.get_price()

    def calc_oturi(self, payment):
        self.calc_total_price()
        self.payment = payment
        return self.payment - self.item_total_price

# マスター読み込み
def load_item_master(file_name):
    if os.path.exists(file_name) != True:
        # print("csvファイルは存在しません。")
        return False
    else:
        item_master = []
        items_list = []
        # print("商品マスターを取り込んでいます。")
        df = pd.read_csv(file_name, dtype={"code": object})
        for index, row in df.iterrows():
            item_master.append(Item(row[0], row[1], row[2]))
            items_list.append(f"商品コード:{row[0]} 商品名:{row[1]} 価格:{row[2]}")
        return item_master, items_list