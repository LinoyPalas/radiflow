import time

class Oven:
    def __init__(self):
        self.busy = False

    def bake_pizza(self, pizza, order_time):
        self.busy = True
        print("Oven starts baking Pizza", pizza.order_id, "at", time.strftime("%H:%M:%S", time.gmtime(order_time)))
        time.sleep(10)
        print("Oven finishes baking Pizza", pizza.order_id, "at", time.strftime("%H:%M:%S", time.gmtime(order_time + 10)))
        self.busy = False
        return order_time + 10