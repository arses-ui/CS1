# Author: Arses Prasai
# Purpose: Lab3 Checkpoint
# Date: 26th 2025

from cs1lib import *
from random import*

class City:

    def __init__(self, countrycode, name, region, population, latitude, longitude):
        self.countrycode = countrycode
        self.name = str(name)
        self.region = str(region)
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return str(self.name) +","+ str(self.population) + "," + str(self.latitude) +","+  str(self.longitude)


    def draw(self, cx, cy):
        px = 2 * self.longitude + cx
        py = 360 - ( 2* self.latitude + cy)
        disable_stroke()
        set_fill_color(1,0,0)
        draw_circle(px, py, 3)
