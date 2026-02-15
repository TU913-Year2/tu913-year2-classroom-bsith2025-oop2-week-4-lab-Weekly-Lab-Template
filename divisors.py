#Brian Watters
#29th Jan 
#Divisors.py

#Add a function below called divisors(num) which takes one argument of type integer
#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder

def divisors(num):
    myList = []
    for i in range(1, num):
        if num % i == 0:
            #print(i)
            myList.append(i)
    return myList

