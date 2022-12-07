from random import random, randint, seed
from math import *
from Bee import *
from Const import *
from SwaromOfBees import *
import time


def main():
    seed(time.time())
    S = SwarmOfBees()
    S.start()


if __name__ == '__main__':
    main()
