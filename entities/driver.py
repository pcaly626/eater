

class Driver:

    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.coordinates = restaurant.coordinates
        self.dest_coordinates = None
        self.on_delivery = False
        self.at_restaurant = True
        self.eater = None

    def __str__(self):
        return "Driver"

    def deliver_order(self, eater):
        self.on_delivery = True
        self.at_restaurant = False
        self.eater = eater
        self.dest_coordinates = eater.coordinates

    def arrive(self):
        if self.on_delivery and self.eater and self.eater.hungry:
            self.eater.receive_order()
            self.dest_coordinates = self.restaurant.coordinates
            print("Driver {} is returning to restaurant".format(self))
        elif self.coordinates == self.restaurant.coordinates:
            self.at_restaurant = True
            self.dest_coordinates = None
            self.on_delivery = False
            print("Driver {} is at restaurant".format(self))

    def calcuate_x(self):
        if self.coordinates[0] > self.dest_coordinates[0]:
            return self.coordinates[0] - 1
        elif self.coordinates[0] < self.dest_coordinates[0]:
            return self.coordinates[0] + 1
        else:
            return self.coordinates[0]

    def calcuate_y(self):
        if self.coordinates[1] > self.dest_coordinates[1]:
            return self.coordinates[1] - 1
        elif self.coordinates[1] < self.dest_coordinates[1]:
            return self.coordinates[1] + 1
        else:
            return self.coordinates[1]

    def move(self):
        x = self.calcuate_x()
        y = self.calcuate_y()
        self.coordinates = (x, y)
        print("Driver {} is moving to {}".format(self, self.coordinates))
        if self.on_delivery and self.coordinates == self.dest_coordinates:
            self.arrive()
        if not self.on_delivery and not self.at_restaurant and self.coordinates == self.dest_coordinates:
            self.arrive()
