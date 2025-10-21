# Import libraries
import pandas as pd

# Create variables and lists
items = ["Bread", "Butter", "Egg", "Sweet", "Orange"]
data = [[1, 3, 4], [2,3,5], [1,2,3,5], [2,5], [1, 2, 5]]
count_items = []
support_items = []
frequent_items = []
temp_items = []
frequent_support_items = []
frequent_itemsets = []
all_supports = []

# Input minimum support
minimum_support = float(input("Please enter the minimum support in probability: "))
while (minimum_support <= 0) or (minimum_support >= 1) or (minimum_support == ""):
    minimum_support = float(input("Please enter the accurate minimum support in probability: "))

# Calculate support
for k in range(1, len(items)+1):
    count = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
                if data[i][j] == k:
                    count += 1
    count_items.append(count)
for i in range(0, len(items)):
    support = count_items[i]/len(data)
    if (support < 1): 
        support = round(support, 4)
    support_items.append(support)

# Find frequent 1-itemset
for i in range(0, len(support_items)): 
    temp_items = []
    if support_items[i] >= minimum_support:
        temp_items.append(i+1)
        frequent_items.append(temp_items)
        frequent_itemsets.append([i+1])

# Create a new list for all frequent itemset
new_frequent_itemsets = []
# Assign value of k for the while loop
k = 1

# Find all frequent itemsets
while frequent_itemsets and k < len(items):
    k += 1
    temp = []
    for i in range(len(frequent_itemsets)):
        for j in range(i+1, len(frequent_itemsets)):
            if frequent_itemsets[i][:-1] == frequent_itemsets[j][:-1]:
                merged = sorted(list(set(frequent_itemsets[i]) | set(frequent_itemsets[j])))
                if merged not in temp:
                    temp.append(merged)
    for tem in temp:
        count = 0
        for transaction in data:
            match = True
            for item in tem:
                if item not in transaction:
                    match = False
                    break
            if match:
                count += 1
        support = round(count / len(data), 4)
        if support >= minimum_support:
            new_frequent_itemsets.append(tem)
            frequent_support_items.append(support)
    frequent_itemsets = temp.copy()

# Create Data Frame for displaying supports for each items
supports = pd.DataFrame()
supports["Items"] = items
supports["Support"] = support_items
supports.index = range(1, len(supports)+1)
print(supports)

# Create Data Frame for displaying all frequent itemsets and its support
frequent_supports = pd.DataFrame()
combine_frequent = frequent_items.copy()
combine_frequent.extend(new_frequent_itemsets)
frequent_supports["Frequent Items"] = combine_frequent
supports_combine = []
print(f"frequent_items: {frequent_items}")

flat = [item for sublist in frequent_items for item in sublist]
int_list = [int(x) for x in flat]

for item in int_list:
    supports_combine.append(support_items[item-1])
for item in frequent_support_items:
    supports_combine.append(item)
frequent_supports["Support"] = supports_combine
print("\n Supports for frequent items")
print(frequent_supports)
result_str = ""
for i in range(0, len(frequent_items)):
    for j in range(i+1, len(frequent_items)):
        result_str = result_str + "{" + str(frequent_items[i]) + "}->{" + str(frequent_items[j]) + "}, " + "{" + str(frequent_items[j]) + "}->{" + str(frequent_items[i]) + "}, "
for i in frequent_items:
    for j in new_frequent_itemsets:
        if not set(i).issubset(set(j)):
            result_str = result_str + "{" + str(i) + "}->{" + str(j) + "}, " + "{" + str(j) + "}->{" + str(i) + "}, "
print("\n Output for Apriori Algorithm")
print(result_str)

# Input y/n for calculating confidence, lift and leverage
option = input("Do you want to find out the confidence, lift and leverage? (y/n) ")
while (option != "y") and (option != "n"):
    option = input("Do you want to find out the confidence, lift and leverage? (y/n)")

# Calculate the values for confidence, lift and leverage based on the option 
while (option == "y") or (option_again == "y"):
    # Create variables for further codes
    option = ""
    option_again = ""

    # Input the number of items and their values
    num_items = int(input("How many items you would like to include? "))
    while (num_items == "") or (num_items <= 1):
        num_items = int(input("Please input the correct number of items you would like to include "))
    print(f"Which {num_items} you want to find? ")

    # Find out the index for x, y and (x and y)
    num_set = []
    for i in range(0, num_items):
        num = int(input(f"The {i+1} number: "))
        num_set.append(num)
    sortted_num_set = num_set.copy()
    num_all = sorted(sortted_num_set)
    num_y = [num_set.pop()]
    num_x = num_set.copy()
    for i in range(0, len(frequent_supports["Frequent Items"])):
        if (num_all == frequent_supports["Frequent Items"][i]):
            index_all = i

    count = 0
    for i in range(0, len(data)):
        n_num_x = str(num_x).replace("[", "").replace("]", "")
        n_num_y = str(num_y).replace("[", "").replace("]", "")
        if (n_num_x in str(data[i]) and n_num_y in str(data[i])):
            count += 1
    support_both = round(count / len(data), 4)

    for i in range(0, len(frequent_supports["Frequent Items"])):
        if (num_x == frequent_supports["Frequent Items"][i]):
            index_x = i
    for i in range(0, len(frequent_supports["Frequent Items"])):
        if (num_y == frequent_supports["Frequent Items"][i]):
            index_y = i
            
    # Find the supports
    support_x = frequent_supports["Support"][index_x]
    support_y = frequent_supports["Support"][index_y]

    # Calculate the confidence, lift and leverage
    confidence = support_both / support_x
    lift = confidence / support_y
    leverage = support_both - support_x * support_y

    # Print out the result
    print(f"Confidence({num_set}->{num_y}) \n = {support_both} / {support_x} \n = {confidence}")
    print(f"Lift({num_set}->{num_y}) \n = {confidence} / {support_y} \n = {lift}")
    print(f"Leverage({num_set}->{num_y}) \n {support_both} - {support_x} * {support_y} \n = {leverage}")

    # Ask the user whether continue or not
    option_again = input("Do you want to continue? (y/n) ")
    while (option_again != "y") and (option_again != "n"):
        option_again = input("Do you want to continue? (y/n) ")