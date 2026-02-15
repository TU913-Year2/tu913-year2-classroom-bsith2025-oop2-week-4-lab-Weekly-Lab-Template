#run this program when you have completed the first two parts of the exercise
#if you have completed the first two parts correctly this will find the first five perfect nubmers

from perfectNumber import isPerfectNumber
import time

totalPFs = 0
testNumber = 1
tic = time.perf_counter()

while (totalPFs <4):

    if (isPerfectNumber(testNumber)):
        
        print(testNumber," is a perfect number")
        bit = time.perf_counter()
        print(f"{testNumber} number found after {bit - tic:0.4f} seconds")
        
        totalPFs = totalPFs + 1
    testNumber = testNumber + 1

toc = time.perf_counter()
print(f"Complted programme in {toc - tic:0.4f} seconds")
