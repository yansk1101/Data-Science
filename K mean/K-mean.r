install.packages(plyr)
install.packages(ggplot2)
install.packages(cluster)
install.packages(lattice)
install.packages(graphics)
install.packages(grid)
install.packages(gridExtra)
library(plyr)
library(ggplot2)
library(cluster)
library(lattice)
library(graphics)
library(grid)
library(gridExtra)

data <- as.data.frame(read.csv("K mean/data2.csv"))
kmdata_orig <- as.matrix(data)
kmdata <- kmdata_orig[1:2]

wss <- numeric(5)
for (i in 1:5)
wss <- numeric(15)
for (i in 1:15) {
  kmeans_result <- kmeans(data, centers = i)
  wss[i] <- kmeans_result$tot.withinss
}

plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="WSS")
km <- kmeans(data, 3, nstart=25)
df <- as.data.frame(kmdata_orig[1:2])
centers <- as.data.frame(km$centers)

g1 <- ggplot(data, aes(Height, Weight)) +
  geom_point() +
  theme(legend.position = "right") +
  geom_point(data = centers, aes(x = Height, y = Weight, 
            color = as.factor(rep(1:3, length.out = nrow(centers)))),
            size = 10, alpha = 0.3, show.legend = FALSE)

temp <- ggplot_gtable(ggplot_build(g1))
grid.arrange(arrangeGrob(g1, top = "Height VS Weight"))
