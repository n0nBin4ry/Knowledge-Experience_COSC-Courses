def prime(x): # defined a function that detects if a number is prime or not
    flag = 0
    for j in range(1,x+1):
        if x/j == float(x)/j: # checks how many factors are in the number
            flag += 1
    if flag == 2: # if a number only has 2 factors, it is a prime number
        return x
    else:
        return 'not prime'
primes = [0] # initializes list
n = raw_input("Hello. I will find all prime numbers from 1 to __")
n = int(n)
for k in range(1,n): # creates list for storing if each number is prime or not
    primes.append(0)
for i in range(1,n+1): # inputs number in list if prime, if not prime it is stated
    primes[i-1] = prime(i)
noneya = primes.count('not prime') # counts how many times there is not a prime
for r in range(noneya): # removes every element that isn't a prime number
    primes.remove('not prime')
print "These are all the prime numbers from 1 to %d:" %n, primes