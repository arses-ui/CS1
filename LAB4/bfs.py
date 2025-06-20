
from collections import *
from load_graph import create_vertex_dictionary


dictionary = create_vertex_dictionary("dartmouth_graph.txt")


def helper(object1, object2):

    q = deque()
    q.append(object1)
    backpointer_dictionary = {}
    backpointer_dictionary[object1] = dictionary[object1]

    while object2 not in backpointer_dictionary:
        if len(q) > 0:
            p = (q.popleft())


            for i in dictionary[p].adjacent:
                if i.name == object2:
                    i.backpointer = dictionary[p]
                    return i

                if i.name not in backpointer_dictionary:

                    backpointer_dictionary[i.name] = p
                    q.append(i.name)
                    i.backpointer = dictionary[p]



        else:
            break
    return None

# def bfs(object1, object2):
#     helper(object1, object2)
#

def bfs(object1, object2):
    helper(object1, object2)
    shortest_path = []
    reverse = dictionary[object2]
    while reverse is not None:
        shortest_path.append(reverse)
        reverse = reverse.backpointer
    return shortest_path

    # for i in dictionary:
    #     print(str(dictionary[i]) , str(dictionary[i].backpointer))

# print(bfs("Sudikoff", "1953 Commons"))

    # while reverse is not None :
    #     print(reverse)
    #     reverse = reverse.backpointer
    # return lst


#

# print(path)
# print(helper("Sudikoff", "1953 Commons"))