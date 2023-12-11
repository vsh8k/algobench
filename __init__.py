from progress.bar import ShadyBar
from progress.spinner import PixelSpinner
import time
import sort
import random
import numpy as np

class data:
    def __init__(self, count) -> None:
        self.array = []
        for x in range(count):
            self.array.append([])
    def generateRand(self, size, min, max):
        it = 0
        for element in self.array:
            with ShadyBar(f'Generating random numbers for array #{it}:', max=size) as bar:
                for x in range(size):
                    element.append(random.randint(min, max))
                    bar.next();
            it += 1
    def partialSort(self, x):
        for i in range(len(self.array)):
            spinner = PixelSpinner(f'Partially sorting array #{i}')
            element = self.array[i]
            index_to_sort = int(len(element) * x)
            self.array[i] = np.partition(element, index_to_sort)
            spinner.next()

    def print(self):
        print(self.array)

print("Shell Sort Test")
test = data(5)
avg_shell = [0, 0, 0, 0, 0]
for i in range(1, 6):#5 skirtingi duomenų kiekiai
    test.generateRand(i * 10, 0, 10)
    for x in range(6): #Bandymus atliekame 6 kartus
        spinner = PixelSpinner(f'Sorting with Shellsort size:{i*1000}, attempt:{x+1}...')
        for x in test.array:
            start_time = time.time()
            sort.shellSort(x, spinner)
            end_time = time.time()
            diff = end_time - start_time
            print(f"\nTime taken to sort using Shellsort: {diff}") 
            avg_shell[i-1] += diff
        spinner.finish()
    avg_shell[i-1] /= 6
print(f"Average sorting times for Shellsort: {avg_shell}")

print("Quicksort Test")

test_quick = data(5)

size = 20000000

test_quick.generateRand(size, 55, 100)

test_quick.partialSort(0.95)

avg_quick = 0;

for x in range(len(test_quick.array)): #Bandymus atliekame 6 kartus
        spinner = PixelSpinner(f'Sorting with Quicksort size:{size}, attempt:{x+1}...')
        start_time = time.time()
        sort.quick_sort(test_quick.array[x], 0, len(test_quick.array[x])-1)
        end_time = time.time()
        diff = end_time - start_time
        print(f"\nTime taken to sort using Quicksort: {diff}") 
        avg_quick += diff
        spinner.finish()
        
avg_quick /= 6

print(f"Average Quicksort sorting time: {avg_quick}")

