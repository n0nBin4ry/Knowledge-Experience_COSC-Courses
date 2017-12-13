import time

#N = raw_input("please enter an integer N and we will sum the square and cube of the numbers from 1 to N: ")
#N = int(N)

N = 100000000

t0 = time.time()

sum = 0
for i in range(N+1):
    sum += i + i*i + i*i*i

t1 = time.time()
total = t1-t0

print "the sum = %s" %sum
print "cpu time = %s secs" %total