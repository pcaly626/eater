import entities as entity
import conf.conf as config
import random
import time


def create_restaurant(coordinates):
    restaurant = entity.restaurant.Restaurant(coordinates)
    for i in range(0,1):
        restaurant.assign_driver(entity.driver.Driver(restaurant))
    return restaurant


def create_eater(restaurants, coordinates):
    return entity.eater.Eater(restaurants, coordinates)


restaurants = [create_restaurant(config.RESTAURANT_COORDINATES)]
eaters = list()
eaters.append(create_eater(restaurants, config.EATERS_COORDINATES[0]))
eaters.append(create_eater(restaurants, config.EATERS_COORDINATES[1]))
eaters.append(create_eater(restaurants, config.EATERS_COORDINATES[2]))


if __name__ == '__main__':

    hungery_eaters = list()
    remove_eater = None
    while True:
        if random.randint(0, 100) > 90:
            eater = random.choice(eaters)
            if not eater.hungry:
                eater.get_hunger()
                eater.chosen_restaurant.receive_order(eater)
                hungery_eaters.append(eater)
        for eater in hungery_eaters:
            if eater.hungry:
                for driver in eater.chosen_restaurant.drivers:
                    if driver.on_delivery:
                        driver.move()
                    if not driver.eater and not driver.at_restaurant:
                        driver.move()

        if hungery_eaters and remove_eater:
            remove_index = 0
            for index, eater in enumerate(hungery_eaters):
                if eater == remove_eater:
                    remove_index = index
                    remove_eater = None
            hungery_eaters.pop(remove_index)
        time.sleep(1)

