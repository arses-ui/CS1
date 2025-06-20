#Author name: Arses Prasai
# Purpose: Lab 2
#date: 2/18/2025

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 800

WINDOW_HEIGHT = 800

TIME_SCALE = 1.5e6         # real seconds per simulation second
PIXELS_PER_METER = 10 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

#function to draw and update the solar system
def main():

    set_clear_color(0, 0, 0)    # black background
    clear()
    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)
    # print(earth.x) to check if working


#objects for the list (planets)
sun = Body(1.989e30, 0 , 0 , 0 , 0 , 30, 1,1,0 )
mercury = Body(0.330e24,57.9e9, 0, 0, 47890, 10, 0.5,0.5,0.5 )
venus = Body(4.87e24, 108.9e9, 0,0,35040,12, 0.5,0.5,0) #grey venus
earth = Body(5.9736e24, 149.6e9 , 0, 0, 29790, 12, 0, 0, 1) #blue earth
mars = Body( 0.642e24, 228e9, 0, 0, 24140, 7, 0.8,0.3, 0) #orange mars


solar_system= System([sun, mercury, venus, earth, mars])


start_graphics(main, 2400, framerate=FRAMERATE, width= WINDOW_WIDTH, height= WINDOW_HEIGHT)