#Brian Watters
#29 Jan 2024
#perfectNumber.py

#A perfect number is one for which all the divisors of the number add up to the
#number itself. For example the divisors of 28 are 1,2,4,7,14 which added together gives 28
#write a function below called perfectNumber(x) which checks to see if x is a perfect number
#The function should return True if the number is perfect and False if it is not

from divisors import divisors
#define the function header called perfectNumber expecting one argument

def isPerfectNumber(num):
    result = False
    total = 0
    #print(divisors(num))
    for i in divisors(num):
        total = total + i
    if total == num :
        result = True
    else:
        result = False
    return result



