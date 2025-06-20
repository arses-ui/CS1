#Author's name: Arses Prasai
#Purpose: LAB4
#Date: 3/4/2025

from vertex import Vertex


def parse_line(line):
    section_split = line.split(";")
    vertex_name = section_split[0].strip()
    adjacent = section_split[1].strip().split(",")
    coordinates = section_split[2].strip().split(",")

    adjacent_list = []
    for a in adjacent:
        if a:
            adjacent_list.append(a.strip())

    coordinates_list = []
    for a in coordinates:
        if a:
            coordinates_list.append(str(a.strip()))
    return vertex_name, adjacent_list, coordinates_list

vertex_dict = {}

def create_vertex_dictionary(filename):

    with open(filename, "r") as file:
        for line in file:
            result = parse_line(line)
            vertex_name = result[0]
            x_coord = int(result[2][0])
            y_coord = int(result[2][1])

            vertex_dict[vertex_name] = Vertex(vertex_name, [],x_coord, y_coord)
        file.close()

    with open(filename, "r") as file:
        for line in file:
            result = parse_line(line)
            name_current = result[0]
            adjacent_vertices = result[1]
            for i in adjacent_vertices:
                vertex_dict[name_current].adjacent.append( vertex_dict[i])
        file.close()
        return vertex_dict








