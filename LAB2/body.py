#Author name: Arses Prasai
# Purpose: Lab 2 checkpoint
#date: 2/18/2025

from cs1lib import *

class Body:

    def __init__(self, m,x, y, v_x, v_y, pixel_radius, r, g, b):
        self.m = m
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.r = r
        self.g = g
        self.b = b
        self.pixel_radius = pixel_radius


    def update_position(self, timestep):


        self.x = self.x + self.v_x* timestep
        self.y = self.y + self.v_y *timestep

    def update_velocity(self, ax, ay, timestep):
        self.v_x = self.v_x + ax*timestep
        self.v_y = self.v_y + ay* timestep

    def draw(self, cx, cy, pixel_per_meter):
        set_fill_color( self.r, self.g, self.b)
        draw_circle ( cx+ (self.x* pixel_per_meter), cy - (self.y * pixel_per_meter), self.pixel_radius)