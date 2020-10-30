import random
import csv

numList = [random.randint(0,100) for i in range(0,1000)]

with open('RandomNums.csv', 'w') as file:
    file.write("x")
    for i in range(0,1000):
        file.write('\n')
        file.write(numList[i].__str__())
file.close()





