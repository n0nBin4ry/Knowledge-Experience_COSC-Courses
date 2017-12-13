ip = raw_input('List the numbers you want to add up, please separate them by commas:') # user inputs numbers
sec = '' # makes an empty string placeholder
Sum = 0 # makes an empty placeholder for the sum
typo = 0 # placeholder for number of astrix 'typos' in string
for i in range(len(ip)): # runs loop for length of string ip
    if ip[i]!=',' and i!=len(ip) and ip[i]!='*':
        sec = sec + ip[i] # inputs the string section before the next comma into string placeholder 'sec'
    elif ip[i] == '*':
        typo += 1 # was going to just use 'pass' but wasn't sure if we went over that in class yet, so I decided to get a bit creative
    elif ip[i]==',': # when the loop reads a comma from the string it increases 'Sum' by 'sec' and resets 'sec'
        sec = float(sec)
        Sum = Sum + sec
        sec = ''
sec = float(sec)
Sum = Sum + sec # when loop runs through it adds whatever is left in 'sec' onto 'Sum'
print "The sum of the numbers is", Sum
print "Watch your typing. Found %d" %typo, "*'s that didn't belong in the input."