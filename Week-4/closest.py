# python3
# https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2 

# ~~OPTIMIZED SOLUTION~~
from math import sqrt
from itertools import combinations

# store best solution here
Best = None

def calc_distance(p1, p2):
    global Best
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    if dx < Best[2] and dy < Best[2]:
        dist = sqrt(dx**2 + dy**2)
        if dist < Best[2]:
            Best = p1, p2, dist

def brute_force(points):
    for p1, p2 in combinations(points, 2):
        calc_distance(p1, p2)

def closest_pair(points):
    global Best
    Best = [None, None, float("inf")]
    x_sorted = sorted(points)
    find_closest(x_sorted)
    print(Best)
    return Best[:2]

def find_closest(x_sorted):
    # perform brute force for 3 or 2 points
    points_count = len(x_sorted)
    if points_count <= 3:
        return brute_force(x_sorted)
    # split into two halves (x line) -> keep sorted by x and y
    half = points_count // 2
    _x_sorted1, _x_sorted2 = x_sorted[:half], x_sorted[half:]
    find_closest(_x_sorted1)
    find_closest(_x_sorted2)
    # check best result of split pair
    find_closest_split_pair(x_sorted)

def find_closest_split_pair(x_sorted):
    points_count = len(x_sorted)
    mid_x = x_sorted[points_count // 2][0]
    # consider only point that are no further than best distance from x
    remained_points = sorted([p for p in x_sorted if mid_x - Best[2] < p[0] < mid_x + Best[2]], key=lambda p: p[1])
    remained_count = len(remained_points)
    for i, p1 in enumerate(remained_points[:-1]):
        for p2 in remained_points[i+1:min(i+7, remained_count)]:
            calc_distance(p1, p2)

n = int(input())
points = []
for _ in range(n):
	point = [int(x) for x in input().split()]
	points.append(point)
closest_pair(points)