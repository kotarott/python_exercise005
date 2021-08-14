import eel
import desktop
import get_order

app_name = "web"
end_point = "index.html"
size = (800,700)
item_master = ""
order = ""

@ eel.expose
def load_item_master(file_name):
    items = get_order.load_item_master(file_name)
    if items == False:
        return False
    else:
        global order
        order = get_order.Order(items[0])
        return items[1]

@ eel.expose
def add_order(item_code, item_num):
    order.add_item_order(item_code, int(item_num))
    order.calc_total_price()
    eel.add_table(order.view_item_list())
    eel.show_item_totale_price(order.item_total_price)

@ eel.expose
def calc_oturi(order_payment):
    eel.show_order_oturi(order.calc_oturi(int(order_payment)))
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)