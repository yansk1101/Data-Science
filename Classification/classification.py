import pandas as pd
import numpy as np
import math

def discretization(column):
    print(column)
    choice = str(input(f"Do you want to decide the bins for the columns (y/n): "))
    while (choice.lower() != "y") and (choice.lower() != "n"):
        choice = str(input("Please input y/n: "))
    no = int(input("How many divisions do you want to have -> "))
    while (no <= 1):
        no = int(input("Please enter the correct numbers of divisions: "))
    if (choice == "y"):
        bins_arr = []
        labels_arr = []
        for i in range(no+1):
            bin = float(input("Please input bin {i}: "))
            bins_arr.append(bin)
        for i in range(len(bins_arr)-1):
            label = str(input(f"Please input the label {i} for the elements from {bins_arr[i]} to {bins_arr[i+1]}"))
        
    else:
        labels_arr = []
        
        for i in range(no):
            label = str(input(f"Please input label {i}: "))
            labels_arr.append(label)
        
    column = pd.cut(column, bins = bins_arr, labels = labels_arr)
    
    return column

result = pd.read_csv("Classification\\data2.csv")
