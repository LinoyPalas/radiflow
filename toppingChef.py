import time


class ToppingChef:
    def __init__(self, id):
        self.id = id
        self.busy = False

    def add_toppings(self, pizza, order_time):
        self.busy = True
        print("Topping Chef", self.id, "starts adding toppings for Pizza", pizza.order_id, "at",
              time.strftime("%H:%M:%S", time.gmtime(order_time)))
        time.sleep(4 * len(pizza.toppings))
        print("Topping Chef", self.id, "finishes adding toppings for Pizza", pizza.order_id, "at",
              time.strftime("%H:%M:%S", time.gmtime(order_time + 4 * len(pizza.toppings))))
        self.busy = False
        return order_time + 4 * len(pizza.toppings)
