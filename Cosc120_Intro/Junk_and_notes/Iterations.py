# iterations(looping)
#sum numbers 1-100 or 1 to any number n
#while loop: while condition is true execute block of code
# then output numbers

#Prototype 1: 1-10

# i = 1
# Sum = 0 #sum that we update
# while i <= 10:
#     Sum = Sum + i #adds i to our sum each time
#     print 'Sum =',Sum
#     i = i+1 #increases by 1
# print "done with loops"

#For any number N

n=raw_input('Up to what number shall we sum up?')
n=int(n)
i = 1
Sum = 0
while i <= n:
    Sum = Sum + i
    i = i+1
print 'Sum =',Sum

