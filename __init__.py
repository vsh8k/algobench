import sort
import time
import random
import numpy as np
class data:
    def __init__(self, count) -> None:
        self.array = []
        for x in range(count):
            self.array.append([])
    def generateRand(self, size, min, max):
        for element in self.array:
            for x in range(size):
                element.append(random.randint(min, max))
    def partialSort(self, x):
        for i in range(len(self.array)):
            element = self.array[i]
            index_to_sort = int(len(element) * x)
            self.array[i] = np.partition(element, index_to_sort)

    def print(self):
        print(self.array)

test = data(1)

test.generateRand(10, 0, 10)
print(test.array)
test.partialSort(0.95)
test.print()

#print(sort.shellSort(arr))