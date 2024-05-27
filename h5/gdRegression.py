import matplotlib.pyplot as plt
from Micrograd.Engine import Value
import numpy as np

x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)
x_values = [Value(xi) for xi in x]
y_values = [Value(yi) for yi in y]

def predict(a, xt):
    return a[0] + a[1] * xt

def MSE(a, x, y):
    total = Value(0.0)
    for i in range(len(x)):
        total += (y[i] - predict(a, x[i]))**2
    return total

def loss(p):
    return MSE(p, x_values, y_values)

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

p = [Value(0.0), Value(0.0)]
optimal_p = gradient_descent(loss, p, max_loops=3000, dump_period=100)

y_predicted = [optimal_p[0].data + optimal_p[1].data * xi for xi in x]
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()
