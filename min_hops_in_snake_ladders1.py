import collections
from math import ceil
import sys

__author__ = 'sarath'

ladders = collections.defaultdict(tuple)
no_of_tiles = 21
start_point = 1
snake_and_ladders = [0] * 21

for i in range(start_point, no_of_tiles + 1):
    snake_and_ladders[i - 1] = i

with open(sys.argv[1], 'r') as csv_file:
    for line in csv_file:
        ladder_info = line.strip().split(",")
        start_points = []
        end_point = int(ladder_info[2])
        if end_point in ladders:
            print(end_point)
            start_points = ladders[end_point]
        start_points.append(int(ladder_info[1]))
        ladders[end_point] = start_points

print(snake_and_ladders)
print(ladders)

# current tile (current), next tile (next), no. of hops (hops)

ladder_paths = collections.defaultdict(list)

for ladder_end_point in ladders:
    ladder_start_points = ladders[ladder_end_point]
    directed_paths = []
    # if ladder_end_point in ladder_paths:
    # directed_paths = ladder_paths[ladder_end_point]
    for ladder_start_point in ladder_start_points:
        directed_paths.append({ladder_start_point: 1})
    ladder_paths[ladder_end_point] = directed_paths

# touching the end point
max_end_point = max(ladder_paths.keys())


def get_hops(hops_diff):
    if hops_diff < 7:
        return hops_diff
    return (hops_diff / 6) + 1


if max_end_point != no_of_tiles:
    ladder_paths[no_of_tiles] = [{max_end_point: get_hops(no_of_tiles - max_end_point)}]
# touching the start point
for ladder_start_points in ladders.values():
    for ladder_start_point in ladder_start_points:
        if ladder_start_point not in ladders:
            ladder_paths[ladder_start_point] = [{start_point: get_hops(ladder_start_point - start_point)}]

print(ladder_paths)


# Add up all path routes distance
def method_name(current_point, current_weight=0):
    print(current_point)
    next_path_info = []
    for next_path in ladder_paths[current_point]:
        print(next_path)
        for key in next_path:
            next_path_info.append((key, current_weight + next_path[key]))
    return next_path_info


def check_point(current_point):
    if current_point in ladder_paths:
        return True
    return False



paths_remaining = True

point = max(ladder_paths.keys())
tiles = []
weight = 0
tiles.append(point)
exit()
while paths_remaining:
    for next_element in ladder_paths[point]:
        if 't' in next_element:
            continue
        else:
            for key in next_element.keys():
                tiles.append(key)
                weight += next_element[key]
                next_element['t'] = True
                point = key
        break
    new_path = (tiles, weight)
    print(new_path)

    if point == start_point:
        print(ladder_paths)
        point = no_of_tiles







weight = 0
next_elements = method_name(point)
print(next_elements)
for next_element in next_elements:
    point = next_element[0]
    weight += next_element[1]
print(next_elements)
next_elements = method_name(point, weight)

for next_element in next_elements:
    point = next_element[0]
    weight += next_element[1]
print(next_elements)