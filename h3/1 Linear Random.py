import random

def constraint(x, y, z):
    return (
        x + y <= 10 and
        2 * x + z <= 9 and
        y + 2 * z <= 11 and
        x >= 0 and
        y >= 0 and
        z >= 0
    )

def objective(x, y, z):
    return 3 * x + 2 * y + 5 * z

def linear_program(max_iterations):
    best_value = None
    best_solution = None
    for _ in range(max_iterations):
        x = round(random.uniform(0, 10),2)
        y = round(random.uniform(0, 10),2)
        z = round(random.uniform(0, 10),2)

        if constraint(x, y, z):
            value = objective(x, y, z)
            if best_value is None or value > best_value:
                best_value=value
                best_solution = (x, y, z)
    return best_value, best_solution

best_value, best_solution = linear_program(500000)
print("Approximate optimal value:", best_value)
print("Approximate optimal solution (x, y, z):", best_solution)
