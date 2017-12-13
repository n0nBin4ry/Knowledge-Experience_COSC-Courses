from random import randint # imports randint function from the random module
n = raw_input("Welcome to the number guessing game! Please choose the highest integer I can go up to:")
n = int(n) # creating range of possible numbers
answer = randint(1,n) # chooses a random number
print "Thank you, now guess to find the integer I chose between 1 and %d." %n
for i in range(20): # gives 20 tries to find number
    while True:
        try:
            m = int(raw_input("What number do you think I chose? You have up to %d tries left." %(20 - i))) #checks to see if input is an integer
            break # if an integer then the while loop ends and continues with the if loop
        except ValueError:  # if its not an integer then an error will appear and ask for their input again
            print "Error. That is not an integer."
    if m == answer: # shows user chose right answer
        print "Correct! You win the grand prize of nothing!"
        break
    elif m > answer and type(m) != type(''): # shows if users' choice is too high, the extra boolean condition is there because somehow a sting is greater than an integer
        print "Too high."
    elif m < answer: # shows if the users' choice is too low
        print "Too low."