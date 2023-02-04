import time


class DoughChef:
    def __init__(self, id):
        self.id = id
        self.busy = False

    def make_dough(self, pizza, order_time):
        self.busy = True
        print("Dough Chef", self.id, "starts making dough for Pizza", pizza.order_id, "at",
              time.strftime("%H:%M:%S", time.gmtime(order_time)))
        time.sleep(7)
        print("Dough Chef", self.id, "finishes making dough for Pizza", pizza.order_id, "at",
              time.strftime("%H:%M:%S", time.gmtime(order_time + 7)))
        self.busy = False
        return order_time + 7
