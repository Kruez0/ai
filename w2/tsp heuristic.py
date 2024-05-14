import random
cities = [
    (0,6),(4,1),(1,2),(5,3),
    (1,1),(1,3),
    (2,5),(2,3),
    (3,7),(3,3)
]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def tsp(cities):
    start=random.randint(0, len(cities) - 1)
    path = [start]
    visited = set([start])
    total_distance=0
    while len(visited) < len(cities):
        city_now=path[-1]
        shortest_distance=float('inf')
        shortest_index=None
        
        for i in range(len(cities)): 
            if i not in visited:
                    dist=distance(cities[city_now],cities[i])
                    if dist<shortest_distance:
                        shortest_distance=dist
                        shortest_index=i
        if shortest_index is not None:
            path.append(shortest_index)
            visited.add(shortest_index)
            total_distance += shortest_distance
            print(f"From {cities[city_now]} to {cities[shortest_index]}, Distance: {shortest_distance}")

    total_distance += distance(cities[path[-1]], cities[start])
    path.append(start)
    return path, total_distance

path_taken, total_distance = tsp(cities)
print("Path taken:", path_taken)
print("Total distance:", total_distance)
print("Path coordinates:", [cities[index] for index in path_taken])