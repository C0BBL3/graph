import sys
sys.path.append('src')
from tree import Tree, Node

def order_towns_by_travel_time_from_scratch(starting_town, railroad_segments):
    new_railroad_segments = []
    for arr in railroad_segments:
        if starting_town in arr:
            if starting_town == arr[1]:
                new_railroad_segments.append([arr[1], arr[0]])
        else:
            new_railroad_segments.append(arr)

    return new_railroad_segments

def order_towns_by_travel_time_using_tree_class(starting_town, railroad_segments): #i am technically using the tree class and doing the get children, print parent and repeat
    new_railroad_segments = order_towns_by_travel_time_from_scratch(starting_town, railroad_segments)
    tree = Tree(starting_town)
    tree.build_from_edges(new_railroad_segments)
    tree.print_breadth_first()

            
