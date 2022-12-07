from random import randint
from Const import *

data = [[randint(0, 1000) for i in range(0, size_map)] for i in range(0, size_map)]

class Bee:
    def __init__(self, x, y):
        self.coord = {'x': x, 'y': y}

    def get_value(self, bee):
        return data[bee.coord['x']][bee.coord['y']]

    def __str__(self):
        return "[" + str(self.coord['x']) + ", " + str(self.coord['y']) + "]"