import pandas as pd
import numpy as np
import math
import itertools

def entropy(items, entropy):
    if (len(items) == 1):
        groups = []
        counts = []
        groups.append(list(set(["".join(map(str, x)) if isinstance(x, (list, np.ndarray)) else str(x) for x in result[items[0]].values])))
        for i in range(len(groups)):
            counts.append(result[items[i]].value_counts().tolist())
        
        if (entropy == "n"):
            value = num_entropy(counts[0])
            return value, groups
        else:
            length = [[[] for _ in range(len(groups[i]))] for _ in range(len(groups))]
            for i in range(len(items)):
                for j in range(len(groups[i])):
                    for k in range(len(target_groups[0])):
                        length[i][j].append(len(result[(result[items[i][0]] == groups[i][j]) & (result[target] == target_groups[0][k])]))
        
            total = []
            for i in range(len(counts)):
                temp = 0
                for j in range(len(counts[i])):
                    temp += counts[i][j]
                total.append(temp)

            t_entropy = 0
            for i in range(len(length)):
                for j in range(len(length[i])):
                    for k in range(len(length[i][j])):
                        t_entropy += (length[i][j][k]/total[i]) * (num_entropy(length[i][j]))
                value = t_entropy

            return value
    else:
        groups = [[] for _ in range(len(items))]
        counts = [[] for _ in range(len(items))]

        for i in range(len(items)):
            groups[i].append(list(set(["".join(map(str, x)) if isinstance(x, (list, np.ndarray)) else str(x) for x in result[items[i]].values])))
        for i in range(len(groups)):
            for j in range(len(groups[i][0])):
                counts[i].append(len(result[result[items[i]] == groups[i][0][j]].value_counts().tolist()))
        words = [[] for _ in range(len(items))]
        for i in range(len(items)):
            for j in range(len(groups[i][0])):
                words[i].append(f"(result['{items[i]}'] == '{groups[i][0][j]}')")
        combinations = itertools.product(*words)
        temp = [list(combo) for combo in combinations]
        use = 0
        for i in range(len(groups)):
            if (len(groups[i][0]) > len(groups[use][0])):
                use = i
        word = [[] for _ in range(len(groups[use][0]))]
        length = [[]for _ in range(len(groups[use][0]))]
        for i in range(len(temp)):
                for j in range(len(groups[use][0])):
                    if (str(groups[use][0][j]) in str(temp[i][use])):
                        word[j].append("& ".join(temp[i]))
        for i in range(len(word)):
            for j in range(len(word[i])):
                    length[i].append(len(result[eval(word[i][j])]))
        total = len(result)
        value = 0
        for i in range(len(length)):
            for j in range(len(length[i])):
                value += (length[i][j]/total) * (num_entropy(length[i]))
        
    return value

def num_entropy(numset):
    n_numset = numset.copy()
    total = 0
    flag =  True
    for i in range(len(n_numset)):
        if (n_numset[i] == 0):
            value = 0
            flag = False
    if flag:
        for i in range(len(n_numset)):
            total += n_numset[i]
        for i in range(len(n_numset)):
            n_numset[i] /= total
        value = 0
        for i in range(len(n_numset)):
            value -= (n_numset[i]*math.log(n_numset[i], 2))
    return value

def information_gain(items):
    if (ans_target == "y"):
        value = target_entropy - entropy([items], target_entropy)
    else:
        value = entropy([items[0]], target_entropy) - entropy(items, target_entropy)
    return value

result = pd.read_csv("Classification\\data.csv")

ans_target = str(input("Do you have a target class? (y/n) "))
while (ans_target.lower() != "y") and (ans_target.lower() != "n"):
    ans_target = str(input("Please input y/n: "))
if (ans_target == "y"):
    target = str(input("What is your target class? "))
    flag3 = True
    for i in range(len(result.columns)):
        if target == str(result.columns[i]):
            flag3 = False
    while (flag3):
        target = str(input("Please input the correct target class -> "))
        for i in range(len(result.columns)):
            if target == str(result.columns[i]):
                flag3 = False
    target_entropy, target_groups = entropy([target], "n")
    print(f"The entropy of the target class {target} is {target_entropy: 2f}. \n")
else:
    target_entropy = "n"

flag = True
while (flag):
    choice = str(input("Which do you want to find, Entropy or Information Gain? "))
    while (choice.lower() != "entropy") and (choice.lower() != "information gain"):
        choice = str(input("Please input Entropy or Information Gain: "))
    no = int(input("How many items you could like to find out? "))
    while (no < 1):
        no = int(input("Please input the correct number of items you want to find out -> "))
    items = []
    for i in range(no):
        item = str(input(f"Item {i+1} you want -> "))
        flag2 = True
        for j in range(len(result.columns)):
            if item == str(result.columns[j]):
                flag2 = False
        while (flag2):
            item = str(input("Please enter the correct item you want -> "))
            for k in range(len(result.columns)):
                if item == str(result.columns[k]):
                    flag2 = False
        items.append(item)

    if (choice.lower() == "entropy"):
        value, n_groups = entropy(items, target_entropy)
    else:
        value = information_gain(items)
    print(f"The {choice.lower()} value is {value: 2f}")

    repeat = str(input("Do you want to continue? (y/n) "))
    while (repeat != "y") and (repeat != "n"):
        repeat = str(input("Please eter y/n: \n"))
    if (repeat == "y"):
        flag = True
    else:
        flag = False