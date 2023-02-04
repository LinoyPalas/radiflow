import time


class Waiter:
    def __init__(self, id):
        self.id = id
        self.busy = False

    def serve_pizza(self, pizza, order_time):
        self.busy = True
        print("Waiter", self.id, "starts serving Pizza", pizza.order_id, "at",
              time.strftime("%H:%M:%S", time.gmtime(order_time)))
        time.sleep(5)
        print("Waiter finishes serving Pizza", pizza.order_id, "at",
              time.strftime("%H:%M:%S", time.gmtime(order_time + 5)))
        self.busy = False
        return order_time + 5
