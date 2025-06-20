#Author's name: Arses Prasai
#Purpose: LAB4
#Date: 3/4/2025

from cs1lib import*
from load_graph import create_vertex_dictionary

from bfs import bfs

goal = None
start = None
drawn = True
dictionary = create_vertex_dictionary("dartmouth_graph.txt")
WIDTH = 1012
HEIGHT = 811

image = load_image("dartmouth_map.png")

def m_move(mx, my):
    global goal
    if start is not None:
        for key in dictionary:
            if dictionary[key].is_on_vertex(mx,my):
                goal = dictionary[key].name
                print(goal)


def m_press(mx,my):
    global start, goal
    for key in dictionary:
        if dictionary[key].is_on_vertex(mx,my):
            start = dictionary[key].name
            goal = None
            print(start)
            print(goal)




def main_draw():
    global drawn, start, goal

    clear()
    draw_image(image, 0, 0 )


    for i in dictionary:
        dictionary[i].draw_all_edges(0,1,0)
        dictionary[i].draw_vertex(0,1,0)

    if start is not None and goal is not None:
        path = bfs(start, goal)
        for i in range(len(path) -1 ):
            path[i].draw_edge(path[i+1], 1, 0, 0 )
            path[i].draw_vertex(1,0,0)
            path[i+1].draw_vertex(1,0,0)


    # if start is not None:
    #     start.draw_vertex(1,0,0)
    # if goal is not None:
    #     goal.draw_vertex(1,0,0)

start_graphics(main_draw, width=WIDTH, height=HEIGHT, mouse_press = m_press, mouse_move=m_move)
