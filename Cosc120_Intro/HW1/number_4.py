#previous comment: # does not generalize 2/5

ip = raw_input('List the numbers you want to add up, please separate them by commas:') # user inputs numbers
sec = '' # makes an empty string placeholder
Sum = 0 # makes an empty placeholder for the sum

for i in range(len(ip)): # runs loop for length of string ip
    if ip[i]!=',' and i!=len(ip):
        sec = sec + ip[i] # inputs the string section before the next comma into string placeholder 'sec'
    elif ip[i]==',': # when the loop reads a comma from the string it increases 'Sum' by 'sec' and resets 'sec'
        sec = float(sec)
        Sum = Sum + sec
        sec = ''
sec = float(sec)
Sum = Sum + sec # when loop runs through it adds whatever is left in 'sec' onto 'Sum'
print "The sum of the numbers is", Sum