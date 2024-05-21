import random
import matplotlib.pyplot as plt
cities = [
    (0, 6), (4, 1), (1, 2), (5, 3),
    (1, 1), (1, 3),
    (2, 5), (2, 3),
    (3, 7), (3, 3)
]
def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def total_distance(order):
    return sum(distance(cities[order[i]], cities[order[(i + 1) % len(order)]]) for i in range(len(order)))

def hill_climbing_tsp(max_iterations):
    solution = random.sample(range(len(cities)), len(cities))
    distanceNow = total_distance(solution)
    
    for _ in range(max_iterations):
        new_solution = solution[:]
        i, j = sorted(random.sample(range(len(solution)), 2))
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i] 
        distanceNew = total_distance(new_solution)
        
        if distanceNew < distanceNow:
            solution= new_solution
            distanceNow=distanceNew
    
    return solution, distanceNow

def plot_tsp_solution(solution):
    tour = [cities[i] for i in solution] + [cities[solution[0]]]
    x_coords, y_coords = zip(*tour)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, 'o-', color='blue')
    for i, (x, y) in enumerate(tour[:-1]):
        plt.text(x, y, str(i), fontsize=12, ha='center')
    
    plt.title("TRAVELLING SALESMAN PROBLEM W/ HILL CLIMBING")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)
    plt.show()

solution, min_distance = hill_climbing_tsp(2000)
print("Optimal Tour Order:", solution)
print("Optimal Tour Distance:", min_distance)
path_coordinates = [(cities[i], cities[solution[(idx + 1) % len(solution)]]) for idx, i in enumerate(solution)]
for (start, end) in path_coordinates:
    print(f"From {start} to {end}, Distance: {distance(start, end)}")

plot_tsp_solution(solution)
