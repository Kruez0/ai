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

def linear_program(step_size):
    best_value = None
    best_solution = None
    
    x = 0
    while x <= 10:
        y = 0
        while y <= 10:
            z = 0
            while z <= 10:
                if constraint(x, y, z):
                    value = objective(x, y, z)
                    if best_value is None or value > best_value:
                        best_value = value
                        best_solution = (x, y, z)
                z = round(z + step_size, 2)
            y = round(y + step_size, 2)
        x = round(x + step_size, 2)

    return best_value, best_solution

best_value, best_solution = linear_program(0.1)
print("Approximate optimal value:", best_value)
print("Approximate optimal solution (x, y, z):", best_solution)
