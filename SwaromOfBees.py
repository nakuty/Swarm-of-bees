from random import random, randint, seed
from math import *
from Bee import *
from Const import *

class SwarmOfBees:
    scouts = []
    best_scouts = []

    def __init__(self):
        for i in range(100):
            rand_a = randint(0, size_map-1)
            rand_b = randint(0, size_map-1)
            self.scouts.append(Bee(rand_a, rand_b))

    def get_value(self, bee):
        return data[bee.coord['x']][bee.coord['y']]

    def delete_near(self):
        delete_scouts = []
        for i in range(0, len(self.scouts)):
            for j in range(i + 1, len(self.scouts)):
                distance = sqrt(pow(self.scouts[i].coord["x"] - self.scouts[i].coord["y"], 2)
                                + pow(self.scouts[j].coord["x"] - self.scouts[j].coord["y"], 2))
                if distance < radius_area:
                    if self.get_value(self.scouts[i]) > self.get_value(self.scouts[j]):
                        delete_scouts.append(j)
                    else:
                        delete_scouts.append(i)

        for i in delete_scouts:
            try:
                self.scouts.remove(i)
            except:
                pass


    def rand_coord_circle(self, bee):
        theta = random() * 2 * pi
        r = randint(-radius_area, radius_area)
        x = bee.coord["x"] + int(r * cos(theta))
        y = bee.coord["y"] + int(r * sin(theta))
        while x < 0 or y < 0 or x >= size_map or y >= size_map:
            theta = random() * 2 * pi
            r = randint(-radius_area, radius_area)
            x = bee.coord["x"] + int(r * cos(theta))
            y = bee.coord["y"] + int(r * sin(theta))
        return x, y

    def init_best_scouts(self):
        for i in range(0, int(len(self.scouts)/2)):
            best_bee = self.scouts[0]
            best_bee_index = 0
            for j in range(len(self.scouts)):
                if self.get_value(self.scouts[j]) > self.get_value(best_bee):
                    best_bee = self.scouts[j]
                    best_bee_index = j
            self.scouts.pop(best_bee_index)
            self.best_scouts.append(best_bee)

    def get_area_bees(self):
        new_bees = {}
        for scout in self.scouts:
            new_bees[scout] = [Bee(*self.rand_coord_circle(scout)) for i in range(0, bees_on_bad + 1)]
        for scout in self.best_scouts:
            new_bees[scout] = [Bee(*self.rand_coord_circle(scout)) for i in range(0, bees_on_good + 1)]
        return new_bees

    def start(self):
        self.delete_near()
        self.init_best_scouts()
        new_bees = self.get_area_bees()

        for i in range(0, 10):
            best_of_bed = self.scouts[0]
            for bee in range(0, len(self.scouts)):
                nb = new_bees[self.scouts[bee]]
                for new_bee in nb:
                    if self.get_value(new_bee) > self.get_value(self.scouts[bee]):
                        self.scouts[bee] = new_bee

            for bee in range(0, len(self.best_scouts)):
                nb = new_bees[self.best_scouts[bee]]
                for new_bee in nb:
                    if self.get_value(new_bee) > self.get_value(self.best_scouts[bee]):
                        self.best_scouts[bee] = new_bee

            new_bees = self.get_area_bees()

            for j in self.scouts:
                print(f"[x: {j.coord['x']}, y: {j.coord['y']}]  value: {self.get_value(j)}", sep=" ")
            for j in self.best_scouts:
                print(f"[x: {j.coord['x']}, y: {j.coord['y']}]  value: {self.get_value(j)}", sep=" ")
            print()