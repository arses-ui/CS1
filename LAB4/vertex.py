#Author's name: Arses Prasai
#Purpose: LAB 4
#Date: 4th March
from cs1lib import*
class Vertex:



    def __init__(self, name, adjacent, ax, ay):
        self.name = name
        self.ax = ax
        self.ay = ay
        self.adjacent = adjacent
        self.backpointer = None

    def __str__(self):
        return str(self.name) + ":"

    def draw_vertex(self, r, g, b):
        set_stroke_width(1)
        set_stroke_color(0,0,0)
        set_fill_color(r, g, b)
        draw_circle(self.ax, self.ay, 8)

    def draw_edge(self, vertex, r, g, b):
        set_stroke_color(r, g, b)
        set_stroke_width(2)
        draw_line(self.ax, self.ay, vertex.ax, vertex.ay )

    def draw_all_edges(self, r, g, b):
        set_stroke_color(r, g, b)
        for i in self.adjacent:
            self.draw_edge(i, r, g, b)

    def is_on_vertex(self,x,y):
        return(self.ax - 10 <= x<= self.ax + 10) and (self.ay - 10 <=y <= self.ay + 10)