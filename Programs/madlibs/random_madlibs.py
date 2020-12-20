from madlibs_collection import aTale, beautyandbeast, crazydream, hungergames, theFunPark
import random

if __name__ == '__main__':
    m = random.choice([aTale, beautyandbeast, crazydream, hungergames, theFunPark])
    m.madlib()
