import random


class Eater:

    def __init__(self, restaurants, coordinates):
        self.coordinates = coordinates
        self.hungry = False
        self.restaurants = restaurants
        self.chosen_restaurant = None

    def __str__(self):
        return "Eater"

    def receive_order(self):
        if self.hungry:
            self.hungry = False
            print("Yum yum yum {} out of 10".format(random.randint(1, 10)))

    def order_food(self, restaurant):
        self.chosen_restaurant = restaurant
        print("Eater {} is ordering food from {}".format(self, restaurant))


    def get_hunger(self):
        self.hungry = True
        self.order_food(random.choice(self.restaurants))
