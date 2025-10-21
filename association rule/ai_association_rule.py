items = ["Bread", "Butter", "Egg", "Sweet", "Orange"]
data = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5], [1, 2, 3, 5]]

minimum_support = float(input("Enter minimum support (as probability): "))
while minimum_support <= 0:
    minimum_support = float(input("Please enter a valid minimum support: "))

# Step 1: Count support for individual items
item_counts = [0] * len(items)
for transaction in data:
    for item in transaction:
        item_counts[item - 1] += 1

support_items = [round(count / len(data), 4) for count in item_counts]
frequent_itemsets = []
level = 1

# Step 2: Get frequent 1-itemsets
current_frequents = [[i + 1] for i, support in enumerate(support_items) if support >= minimum_support]
frequent_itemsets.extend(current_frequents)

# Step 3: Iteratively generate larger itemsets manually
while current_frequents:
    level += 1
    candidates = []

    # Manual combination logic: join itemsets if they share first (level-2) items
    for i in range(len(current_frequents)):
        for j in range(i + 1, len(current_frequents)):
            # Try to merge two itemsets
            if current_frequents[i][:-1] == current_frequents[j][:-1]:
                merged = sorted(list(set(current_frequents[i]) | set(current_frequents[j])))
                if merged not in candidates:
                    candidates.append(merged)

    # Count support for each candidate
    new_frequents = []
    for candidate in candidates:
        count = sum(1 for transaction in data if all(item in transaction for item in candidate))
        support = round(count / len(data), 4)
        if support >= minimum_support:
            new_frequents.append(candidate)

    frequent_itemsets.extend(new_frequents)
    current_frequents = new_frequents

# Step 4: Display all frequent itemsets
print(f"\nAll frequent itemsets with support ≥ {minimum_support}:")
for itemset in frequent_itemsets:
    names = [items[i - 1] for i in itemset]
    print(f"{names}")
    