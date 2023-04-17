
class Restaurant:

    def __init__(self, start_coordinates):
        self.coordinates = start_coordinates
        self.drivers = []

    def __str__(self):
        return "Restaurant"

    def assign_driver(self, driver):
        self.drivers.append(driver)

    def receive_order(self, eater):
        for driver in self.drivers:
            if driver.at_restaurant:
                print("Driver {} is delivering order to eater {}".format(driver, eater))
                driver.deliver_order(eater)


