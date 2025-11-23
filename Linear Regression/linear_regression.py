import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def simple(x, y):
    x_bar = 0
    y_bar = 0
    s_xx = 0
    s_xy = 0
    for i in x:
        x_bar += i
    for j in y:
        y_bar += j
    for i in x:
        s_xx += (i-x_bar)**2
        for j in y:
            s_xy += (i-x_bar)*(j-y_bar)
    beta_1 = s_xy/s_xx
    beta_0 = y_bar-beta_1*x_bar
    hat_y = []
    for i in x:
        temp = beta_0+beta_1*i
        hat_y.append(temp)
    return x, hat_y

def multiple(x, y):
    return x, hat_y

def define():
    x = []
    y = []

    nop = int(input("How many points do you have? "))
    for i in range(nop):
        temp = float(input(f"What is the {i+1} value for x: "))
        x.append(temp)
    for i in range(nop):
        temp = float(input(f"What is the {i+1} value for y: "))
        y.append(temp)

    return x, y

def import_file(path):
    result = pd.read_csv(path)
    x = result.iloc[:,0]
    y = result.iloc[:,1]
    return x, y

# result = pd.read_csv("Linear Regression\\data.csv")

choice = str(input("Do you want to handle a simple or multiple linear regression? (simple/multiple) "))
while (choice.lower() != "simple") and (choice.lower() != 'multiple'):
    choice = str(input("Please input simple or multiple: "))
choice_2 = str(input("Do you want to input the values for import a file? (input/import) "))
while (choice_2.lower() != "input") and (choice_2.lower() != "import"):
    choice_2 = str(input("Please input input or import: "))
if (choice_2 == "input"):
    x, y = define()
else:
    path = str(input("What is the file path? "))
    check = str(input(f"Are you sure {path} is the corrected path? (y/n) "))
    if (check.lower() == "y"):
        x, y = import_file(path)
    else:
        path = str(input("Please input the correct path: "))
if choice.lower() == "simple":
    x, hat_y = simple(x, y)
else:
    x, hat_y = multiple(x, y)

plt.scatter(x, y, color="blue")
plt.scatter(x, hat_y, color="red")
plt.xlabel("Advertising Expenditure")
plt.ylabel("Sales Revenus")
plt.show()