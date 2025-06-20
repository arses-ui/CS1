#Author name: Arses Prasai
# Purpose: Lab 2 checkpoint
#date: 2/20/2025

from body import Body
from math import*

G = 6.67384e-11 # gravitational constant
class System :

    def __init__(self, body_list ):
        self.body_list = body_list

    #this method loops over all the items in the list and updates the position and velocities
    def update(self,  timestep):
        for n in range (len(self.body_list)):
            ax, ay = self.compute_acceleration(n)
            self.body_list[n].update_velocity(ax, ay,timestep) #

        for body in self.body_list:
            body.update_position(timestep)

#this function computes the total acceleration on a specific body due to all other bodies in the solar system
    def compute_acceleration(self,n ):
        ax= 0
        ay = 0
        for j in range(len(self.body_list)):
            if j != n:
                otherbody = self.body_list[j]
                dx = otherbody.x - self.body_list[n].x
                dy = otherbody.y - self.body_list[n].y
                r = sqrt(dx ** 2 + dy ** 2)
                a = (G*otherbody.m)/(r**2)
                ax += a*(dx/r)
                ay += a*(dy/r)

        return ax, ay

    #call the draw method from body class on the items in the list
    def draw(self, cx, cy, pixel_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixel_per_meter)


# The compute_acceleration method computes the x and y components of the acceleration of the body at index n in the list.
# (The method takes the index n as a parameter.) Remember that to compute the acceleration, you will have to loop over all
# other bodies to add up their contributions to the acceleration of body n