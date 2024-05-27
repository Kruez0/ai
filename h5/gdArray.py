from Micrograd.Engine import Value
import numpy as np

def f(p):
    x, y, z = p
    return (x - Value(1))**2 + (y - Value(2))**2 + (z - Value(3))**2
    #this is (x-1)^2 + (y-2)^2 +(z-3) ^2

def gradient_descent(f, p, lr=0.01, max_loops=100000, dump_period=1000):
    for loop in range(max_loops):
        loss = f(p)
        for param in p:
            param.grad = 0.0
        loss.backward()
        grads = [param.grad for param in p]
        glen = np.sqrt(sum([g**2 for g in grads]))
        if loop % dump_period == 0:
            print(f'loop {loop}, p = {[param.data for param in p]}, f(p) = {loss.data}, glen = {glen}')
        if glen < 0.00001:
            break
        gh = np.multiply(grads, -1 * lr)
        for param, step in zip(p, gh):
            param.data += step

    print(f'loop {loop}, p = {[param.data for param in p]}, f(p) = {loss.data}, glen = {glen}')
    return p

p = [Value(0.0), Value(0.0), Value(0.0)]
optimal_p = gradient_descent(f, p)

print(f'{[param.data for param in optimal_p]}')
print(f'Most Optimal: {f(optimal_p).data}')