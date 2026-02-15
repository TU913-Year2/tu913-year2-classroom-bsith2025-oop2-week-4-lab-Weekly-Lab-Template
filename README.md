# oop2labPerfectNumbers
This lab exercise has four objectives:
- To get you started using git and github
- To get you started using the Command Line Interface
- To guide you through a Top Down Design solution to a problem
- To get you to correctly translate pseudo-code

The challenge is to find the first five "perfect Numbers" - 
A perfect Number is one for which the sum of all it's divisors adds up to the number itself.
These numbers are rare. The first four are 28, 496, 8128

Using a "Top down design" approach we imagine a function that when passed a number,
will return true if the number is perfect and false if it is not

The solution is then to keep a count (accumulator varialbe) of the total number of perfect numbers found and
keep trying to find another perfect number until 5 are found. Each time around the loop we must also increment the testNumber by 1
```
totalPFs = 0
testNumber = 1
while (totalPFs <5):
    if (perfectNumber(testNumber)):
        print(testNumber,"is a perfect number")
        totalPFs = totalPFs + 1
        testNumber = testNumber + 1
```
        
Having imagined a function (perfectNumber) that tells us whether a number is perfect or not, the solution is simple.
Now we tackle the problem at a lower level and try to figure out how to create the perfectNumber function. If only we had a function that
gave us back a list of all the divisors of the function - the solution would be easier - so we imagine a function like that.

In the exercise: 
1. open the file divisors.py and translate the pseudo code to create a function which will return a list of divisors
2. open the file perfectNumber.py and translate the psuedo code to create a function which will return True or False based on whether the number passed is perfect or not
3. run the program in findFirstFivePNs.py to find the first five perfect numbers 
