import pandas as pd
import numpy as np

def calculation(value):
    if len(value) == 1:
        count = 1
    return result
def counted(file):
    return True


result = pd.read_csv("Classification\\data3.csv")

lmbda = int(input("Please input the lambda value -> "))
nov = int(input("Do you want to find out the conditional probability? "))
object1 = str(input("Input the first object you want: "))
value1 = str(input("What is its value: "))
object2 = str(input("Input the second object you want: "))
value2 = str(input("What is its value: "))

count1 = 0
count2 = 0
for i in range(len(result["Sample"])):
    if result[object1][i] == value1:
        count1 += 1
    if result[object2][i] == value2:
        count2 += 1

