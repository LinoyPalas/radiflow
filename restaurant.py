import time
import random
from doughChef import DoughChef
from toppingChef import ToppingChef
from oven import Oven
from waiter import Waiter
from pizza import Pizza


class Restaurant:
    def __init__(self):
        self.dough_chefs = [DoughChef(1), DoughChef(2)]
        self.topping_chefs = [ToppingChef(1), ToppingChef(2), ToppingChef(3)]
        self.oven = Oven()
        self.waiters = [Waiter(1), Waiter(2)]

    def create_pizza(self, order_id, toppings):
        # Create a new Pizza object with the given order_id and toppings
        pizza = Pizza(order_id, toppings)
        order_time = time.time()

        # Choose a random available dough chef
        dc_id = random.choice([i for i in range(len(self.dough_chefs)) if not self.dough_chefs[i].busy])
        order_time = self.dough_chefs[dc_id].make_dough(pizza, order_time)

        # Choose a random available topping chef
        tc_id = random.choice([i for i in range(len(self.topping_chefs)) if not self.topping_chefs[i].busy])
        order_time = self.topping_chefs[tc_id].add_toppings(pizza, order_time)

        if not self.oven.busy:
            # Have the oven bake the pizza
            order_time = self.oven.bake_pizza(pizza, order_time)

        # Choose a random available waiter
        w_id = random.choice([i for i in range(len(self.waiters)) if not self.waiters[i].busy])
        order_time = self.waiters[w_id].serve_pizza(pizza, order_time)

        # Calculate the preparation time for the pizza
        pizza.prep_time = order_time - time.time()
        return pizza

    def take_orders(self, orders):
        # Create a list to store the created pizzas
        pizzas = []
        # Loop through the given orders
        for order in orders:
            # Create a pizza for each order
            pizza = self.create_pizza(order[0], order[1])
            # Add the created pizza to the list of pizzas
            pizzas.append(pizza)
        return pizzas

    def generate_report(self, pizzas):
        # Calculate the total preparation time for all pizzas
        total_prep_time = 0
        # Loop through the given pizzas
        for pizza in pizzas:
            total_prep_time += pizza.prep_time
            # Print the preparation time for each pizza
            print("Pizza", pizza.order_id, "prepared in", round(pizza.prep_time, 2), "seconds.")
        # Print the total


if __name__ == '__main__':
    orders = [(1, ["cheese", "tomato", "olives"]), (2, ["pepperoni", "mushrooms", "onions"]),
              (3, ["sausage", "peppers", "garlic"])]
    restaurant = Restaurant()
    pizzas = restaurant.take_orders(orders)
    restaurant.generate_report(pizzas)
