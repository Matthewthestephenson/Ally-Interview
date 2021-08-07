import sys
import time
import urllib.request
import json

from crafts import Crafts
from iss import ISSTracking


def main():
    if "loc" in sys.argv[1:len(sys.argv)]:
        iss = ISSTracking()
        loc = iss.get_location()
        print("The ISS current location at {} is at {}".format(loc[0], loc[1]))
    if "people" in sys.argv[1:len(sys.argv)]:
        crafts = Crafts()
        craft_people_dict = crafts.get_craft_people()

        for k in craft_people_dict.keys():
            print("There are {} people aboard the {}. They are {}".format(len(craft_people_dict[k]), k,
                                                                          craft_people_dict[k]))
    if "pass" in sys.argv[1:len(sys.argv)]:
        print("pass has been deprecated by the api")


if __name__ == "__main__":
    main()
