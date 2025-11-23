install.packages("arules")
install.packages("arulesViz")
install.packages("ggplot2")
library(arules)
library(arulesViz)
library(ggplot2)

setwd("C:/Users/yanss/Documents/VSCode_try/association rule")

result <- read.csv("data.csv")

items <- c(1, 2, 3, 4, 5)
data <- c()

count_items <- c()
support_items <- c()
frequent_items <- c()
temp_items <- c()
frequent_support_items <- c()
frequent_itemsets <- c()
temp_items <- c()
frequent_itemsets <- c()
all_supports <- c()

minimum_support <- readline("Please enter the minimum support in probability: ")
while ((minimum_support <= 0) | (minimum_support >= 1) | (minimum_support == "")){
    minimum_support <- readline("Please enter the accurate minimum support value: ")
}

for (k in range(1, len(items)+1)){
    count <- 0
    for (i in range(0, len(data))){
        for (j in range(0, len(data[i]))){
            if (data[i][j] == k){
                count <- count + 1
            }
        }
    }
    count_items <- append(count_items, count)
}


for (i in range(0, len(support_items))){
    temp_items <- c()
    if (support_items[i] >= minimum_support){
        temp_items <- append(temp_items, i+1)
        frequent_items <- append(frequent_items, temp_items)
        frequent_itemsets <- append(frequent_itemsets, c(i+1))
    }
}

new_frequent_itemsets <- c()
k <- 1

while ((frequent_itemsets) & (k < len(items))){
    k <- k+1
    temp <- c()
    for (i in range(len(frequent_itemsets))){
        for (j in range(i+1, len(frequent_itemsets))){
            if (frequent_itemsets[i][:-1] == frequent_itemsets[j][:-1])
        }
    }
}



# data <- read.csv("sample.csv")
items <- vector("numeric", length=5)
items[1:5] <- 1:5
data <- list(list(1,3,4), list(2,3,5), list(1,2,3,5), list(2,5), list(1,2,3,5))
count_items <- vector("numeric", length(items))
support_items <- vector("numeric", 0)
frequent_items <- vector("numeric", 0)
frequent_itemsets <- vector("numeric", 0)
frequent_support_items <- vector("numeric", 0)
new_frequent_itemsets <- vector("numeric", 0)

minimum_support <- as.double(readline(prompt="Please enter the minimum support in probability: "))
while (minimum_support <= 0 | minimum_support >= 1 | is.na(minimum_support)){
    minimum_support <- as.double(readline(prompt="Please enter the minimum support in probability: "))
}

for (k in 1:length(items)) {
    count <- 0
    for (i in 1:length(data)) {
        for (j in 1:length(data[[i]])) {
            print(data[[i]][[j]])
            print(items[k])
            if (data[[i]][[j]] == items[k]) {
                count <- count + 1
            }
        }
    }
    count_items[k] <- count
}

for (i in 1:length(items)){
    support <- count_items[i] / length(data)
    if (support < 1){
        support <- round(support, digits=4)
    }
    support_items <- append(support_items, support)
}
for (i in 1:length(support_items)){
    temp_items <- vector("numeric", length(support_items[i]))
    if (support_items[i] >= minimum_support){
        temp_items <- append(temp_items, i)
        frequent_items <- append(frequent_items, temp_items)
        frequent_itemsets <- append(frequent_itemsets, i)
    }
}

k <- 1
while (length(frequent_itemsets) != 0 && k < length(items)){
    k <- k + 1
    temp <- vector("numeric", 0)
    for (i in 1:length(frequent_itemsets)){
        for (j in i+1:length(frequent_itemsets)){
            #if (frequent_itemsets[i][-1] == frequent_itemsets[j[-1]]){
            if (identical(head(frequent_itemsets[i], -1), head(frequent_itemsets[j], -1))) {
                merged <- sort(unique(c(frequent_itemsets[i], frequent_itemsets[j])))
                #if (merged !in temp){
                #    temp <- append(temp, merged)
                #}
                if (!any(sapply(temp, function(x) identical(x, merged)))) {
                    temp <- append(temp, merged)
                }
    for (tem in temp){
        count <- 0
        for (transaction in data){
            match <- TRUE
            for (item in tem){
                if (!any(sapply(item, function(x) identical(x, merged)))){
                    match <- FALSE
                    break
                }
                if (match){
                    count <- count + 1
                }
            }
        }
        support <- round(count/length(data), digits=4)
        if (support >= minimum_support){
            new_frequent_itemsets <- append(new_frequent_itemsets, tem)
            frequent_support_items <- append(frequent_support_items, support)
        }
    }
    frequent_itemsets <- temp
            }
        }
    }
}
unlist(frequent_itemsets)
support <- data.frame()

transaction_list <- split(data$SItems)
transactions <- as(transaction_list, "transactions")
train_indices <- sample(seq_len(length(transactions)), size=0.7*length(transactions))
train_transactions <- transactions[train_indices]
test_transactions <- transactions[-train_indices]
rules <- apriori(train_transactions, parameter=list(supp=0.001,conf=0.3))