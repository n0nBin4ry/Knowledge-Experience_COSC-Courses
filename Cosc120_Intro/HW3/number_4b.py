print "Please input an integer greater than 2, but no greater than 500."
while True: # user inputs a number greater than 2 up to 500
    while True:
        try:
            N = int(raw_input('> '))
            break
        except ValueError:
            pass
    if 2 < N <= 500:
        break
    else:
        pass
evens = [] #initializes list of evens
k = 0
i = 4
while 3 < i <= N: # adds every even in N to list of evens
    if i%2 == 0:
        evens.append(i)
        k += 1
        i += 1
    else:
        i += 1
        pass
print evens
primes = [] #initializes list of primes
for u in range(3, N + 1): # adds every prime in N to list
    flag = 0
    for j in range(1,u + 1):
        if float(u)/j == u/j:
            flag += 1
    if flag == 2:
        primes.append(u)
#print primes
for a in evens: # every number in evens list
    for b in primes:
        if (a - b) in primes:# gets subtracted by numbers in the prime list until it equals a prime number
            print a, ' = ', b, '+', (a-b)
            break
        else:
            pass