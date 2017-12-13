evens = [] # initializes list of evens
k = 0
i = 4
while 3 < i <= 100: # finds all even numbers greater than 2 up to 100, then puts them in list of evens
    if i%2 == 0:
        evens.append(i)
        k += 1
        i += 1
    else:
        i += 1
        pass
print evens
primes = [] # initializes list of primes
for u in range(3, 101): # finds all prime numbers greater than 2 up to 100, then puts them in  the list of primes
    flag = 0
    for j in range(1,u + 1):
        if float(u)/j == u/j:
            flag += 1
    if flag == 2:
        primes.append(u)
#print primes
for a in evens: # every number in evens list
    for b in primes: # gets subtracted by numbers in the prime list until it equals a prime number
        if (a - b) in primes:
            print a, ' = ', b, '+', (a-b) # the new prime number then gets displayed of a sum of itself and the other prime number to equal the even number
            break
        else:
            pass