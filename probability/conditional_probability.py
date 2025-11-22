import math
def conditional_probability(counts):
    probability = counts[0]/counts[1]
    return probability

def geometric(p, x):
    mean = 1/p
    var = (1-p)/p**2
    sd = math.sqrt(var)
    probability = (1-p)**(x-1)*p
    return mean, var, sd, probability

def binomial():
    return

def normal():
    return