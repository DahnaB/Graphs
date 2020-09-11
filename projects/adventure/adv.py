from room import Room
from player import Player
from world import World


import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

visited = set()

backtrack = {"n": "s", "s": "n", "e": "w", "w": "e"}

stack = Stack()

direction_dict = {}

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def traverse_maze():
    while len(visited) < len(room_graph):
        current_room_id = player.current_room.id 
        if current_room_id not in visited:
            visited.add(current_room_id)
            exits = player.current_room.get_exits()
            direction_dict[current_room_id] = exits

        num_exits = len(direction_dict[current_room_id])
        
        while num_exits > -1:
            # checking that we are not at a dead end
            if num_exits is not 0:
                direction = direction_dict[current_room_id].pop()
                if player.current_room.get_room_in_direction(direction).id not in visited:
                    stack.push(direction)
                    player.travel(direction)
                    traversal_path.append(direction)
                    break

            num_exits = len(direction_dict[current_room_id])
            # However, if we do have a deadend, have player retrace steps
            if num_exits is 0:
                prev_move = stack.pop()
                prev_direction = backtrack[prev_move]
                player.travel(prev_direction)
                traversal_path.append(prev_direction)
                break

traverse_maze()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
