#Author: Arses Prasai
#Purpose: lab3 checkpoint
#Date: 26th February 2025

from city import City
from cs1lib import *
from quicksort import sort

#variables
W_WIND = 720
H_WIND = 360
cities_list = []
drawn= False
count = 0

def read_cities():
    global cities_list
    with open("world_cities.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                info = line.split(",")
                location = City(info[0], info[1], info[2], info[3], info[4], info[5])
                cities_list.append(location)

def compare_alpha( city1, city2):
    return city1.name.lower() <= city2.name.lower()

def compare_population(city1, city2):
    return city1.population >= city2.population

def compare_latitude(city1, city2):
    return city1.latitude <= city2.latitude

#function to sort the list by name and write in a new txt file
def writing_file_alpha():
    sort(cities_list, compare_alpha)
    with open("cities_alpha.txt", "w") as file: #the "w" instead of "a" makes sure that the items are not repeated everytime
        for i in range(len(cities_list)):
            file.write(str(cities_list[i])+ "\n")

#function to sort the list by population and write in a new txt file
def writing_file_population():
    sort(cities_list, compare_population)
    with open("cities_population.txt", "w") as file:
        for i in range(len(cities_list)):
            file.write(str(cities_list[i])+ "\n")

#function to sort the list by latitude and write in a new txt file
def writing_file_latitude():
    sort(cities_list, compare_latitude)
    with open("cities_latitude.txt", "w") as file:
        for i in range(len(cities_list)):
            file.write(str(cities_list[i])+ "\n")


#abstraction
def process_cities():
    read_cities()
    writing_file_alpha()
    writing_file_latitude()
    writing_file_population()


def main_draw():
    global drawn, count
    img = load_image("world.png")
    if not drawn:
        clear()
        draw_image(img, 0, 0 )
        process_cities()
        drawn = True

    while count< 25:
        cities_list[count].draw(W_WIND//2,H_WIND//2)
        count +=1

start_graphics(main_draw, width= W_WIND, height= H_WIND)





