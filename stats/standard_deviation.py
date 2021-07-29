from array import *
import math

def calc_mean(data):
    global mean
    mean = 0.0
    length = len(data)
    for i in range(0, length):
        mean += float(data[i])
    mean = mean/length
    print ("Mean is: " + str(mean))

def calc_standard_deviation(data, mean1):
    global standard_deviation
    length = len(data)
    sum_squares = 0.0
    for i in range (0, length):
        diff = mean1-float(data[i])
        sum_squares += math.pow(diff, 2)
    sample_variance = sum_squares/(length -1)
    print ("Sample variance is: " + str(sample_variance))
    sample_standard_deviation = math.sqrt(sample_variance)
    print ("Sample standard deviation is: " + str(sample_standard_deviation))
    population_variance =  sum_squares/length
    print ("Population variance is: " + str(population_variance))
    population_standard_deviation = math.sqrt(population_variance)
    print ("Population standard deviation is: " + str(population_standard_deviation))


to_parse = input("Enter numbers serpated by commas: ")
raw_data = str(to_parse).split(',')
calc_mean(raw_data)
calc_standard_deviation(raw_data, mean)
