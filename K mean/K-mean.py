import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def euclidean_distance(p1, p2):
    print(f"The distance between {p1}  and {p2} is {np.sum((p1 - p2) ** 2)}")
    return np.sqrt(np.sum((p1 - p2) ** 2))

def WSS(data, k):
    temp = []
    for i in range (2, k+1):
        distance = 0
        centroids = []

        for j in range(i):
            no = random.randint(1, len(data)-1)
            centroids.append(data[no])

        flag = True
        while (flag):
            groups = grouping(data, centroids, i)
            new_centroids = compute_centroids(groups)
            if compare_centroids(centroids, new_centroids):
                flag = False
            else: 
                centroids = new_centroids

        for i in range(len(groups)):
            distance = 0
            for points in groups[i]:
                distance += (euclidean_distance(points, centroids[i]))**2
        temp.append(distance)

    lowest = 0
    for i in range(1, len(temp)):
        if (temp[i] > temp[lowest]):
            lowest = i
    
    return temp[lowest]

def compute_centroids(groups):
    new_centroids = []
    for i in range(len(groups)):
        x = 0
        y = 0
        for points in groups[i]:
            x += points[0]
            y += points[1]
        average_x = float(x / len(groups[i]))
        average_y = float(y / len(groups[i]))
        new_centroids.append([average_x, average_y])
    return new_centroids

def grouping(data, centroids, no_of_cluster):
    distances = [[0 for _ in range(len(centroids))] for _ in range(len(data))]
    groups = [[] for _ in range(int(no_of_cluster))]

    for i in range(len(data)):
        for j in range (len(centroids)):
            distances[i][j] = euclidean_distance(centroids[j], data[i])
    for k in range(len(distances)):
        nearest = 0
        for y in range(1, len(distances[k])):
            if distances[k][y] < distances[k][nearest]:
                nearest = y
        groups[nearest].append(data[k])

    return groups

def compare_centroids(centroids, new_centroids):
    flag = True
    if (len(centroids) != len(new_centroids)):
        flag = False
    else:
        np_new_centroids = np.array(new_centroids)
        for center in centroids:
            if not any(np.array_equal(center, new_center) for new_center in np_new_centroids):
            # if center not in np_new_centroids.any():
                flag = False
    return flag

def plotting(groups, new_centroids):
    colours = ["orange", "green", "blue", "purple", "yellow"]
    np_groups = [[] for _ in range(len(groups))]
    for i in range (len(groups)):
        np_groups[i] = np.array(groups[i])
    np_new_centroids = np.array(new_centroids)

    for i in range(len(groups)):
        plt.scatter(np_groups[i][:, 0], np_groups[i][:, 1], c=colours[i])

    plt.scatter(np_new_centroids[:, 0], np_new_centroids[:, 1], c="red", marker="X", s=50)
    plt.title("K-means Clustering")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

result = pd.read_csv("K mean\\data3.csv")  
data = np.array(result)

centroids = []
choice = str(input("Do you want to decide the number of clusters? (y/n) "))
while (choice != "n") and (choice != "y"):
    choice = str(input("Do you want to enter the initial centroid(s)? (y/n) "))
if (choice == "y"):
    no_of_clusters = int(input("Enter the number of clusters -> "))
else:
    no_of_clusters = WSS(data, len(data)//2)
choice = str(input("Do you want to set the initial centroid(s)? (y/n) "))
while (choice != "n") and (choice != "y"):
    choice = str(input("Do you want to enter the initial centroid(s)? (y/n) "))
if (choice == "y"):
    for i in range (1, no_of_clusters+1):
        centroid = int(input(f"Which subject you want to set the {i} initial centroid as? "))
        centroids.append(data[centroid-1])

flag = True 
count = 0
while (flag):
    count += 1
    #print(f"The iteration {count}: ")

    groups = grouping(data, centroids, no_of_clusters)
    new_centroids = compute_centroids(groups)        
    print(f"The computed centroids are {centroids[0]} and {centroids[1]}")
    print(f"Group 1: {groups[0]}")
    print(f"Group 2: {groups[1]} \n")
    if compare_centroids(centroids, new_centroids):
        grouping(data, new_centroids, no_of_clusters)
        flag = False
    else:
        centroids = new_centroids
print(f"The final computed centroids are {new_centroids[0]} and {new_centroids[1]}")
print(f"Group 1 (Final) : {groups[0]}")
print(f"Group 2 (Final) : {groups[1]} \n")
plotting(groups, new_centroids)