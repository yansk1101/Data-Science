import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# result = pd.read_csv("Linear Regression\\data.csv")
x = [2, 5, 3, 10, 6]
y = [1, 7, 3, 5, 7]
plt.scatter(x, y)
plt.show()
count_x = 0
count_y = 0
count_x2 = 0
for i in range(len(x)):
    count_x += x[i]
    count_y += y[i]
    count_x2 += x[i]**2

x_bar = count_x / len(x)
y_bar = count_y / len(y)

count = 0 
for i in range(len(x)):
    count += x[i]*y[i]

beta_1 = (count-len(x)*x_bar*y_bar)/(count_x2-len(x)*(x_bar**2))
beta_0 = y_bar-beta_1*x_bar

new_y = []
for i in range(len(y)):
    y = beta_0 + beta_1*x[i]
    new_y.append(y)

plt.scatter(x, y)
plt.scatter(x, new_y)
plt.show()