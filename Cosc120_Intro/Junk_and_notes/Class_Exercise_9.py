# password = {'maynard' : '55123' , 'bob' : 'bob123' , 'jim' : 'hiyajim' , 'helen' : 'helen1'}
# print 'So you forgot you username? no problem, just input your password and we\'ll get that to you. Passwords aren\'t ' \
#       'case sensitive.'
# while True:
#     flag = 0
#     value = raw_input('> ')
#     value = value.lower()
#     for i in password: # checks every key in 'password'
#         if password[i] == value: # i = current <key>, and the command <dict>[<key>] returns the single or mult <value> of <key>
#             print 'Your username is: %s' %i
#             break
#         else:
#             flag += 1
#     if flag == len(password):
#         print "I'm sorry but your password doesn't belong to any of our usernames. Try again."
#         pass
#     else:
#         break
###########################################################################################################
# sample of <string>.split()

# words = 'these are 4 words'
# print words.split() # print out: ['these', 'are', '4', 'words']
grades = {}
handle = open('grades.txt','r')
for line in handle:
    split = line.split()
    fname = split[0]
    lname = split[1]
    num = split[2]
    grades[fname + ' ' + lname] = num
handle.close()
print grades
for key in grades:
    if float(grades[key]) >= 100:
        grades[key] = 'A+'
    elif float(grades[key]) >= 90:
        grades[key] = 'A'
    elif float(grades[key]) >= 88:
        grades[key] = 'A-'
    elif float(grades[key]) >= 86:
        grades[key] = 'B+'
    elif float(grades[key]) >= 80:
        grades[key] = 'B'
    elif float(grades[key]) >= 78:
        grades[key] = 'B-'
    elif float(grades[key]) >= 76:
        grades[key] = 'C+'
    elif float(grades[key]) >= 70:
        grades[key] = 'C'
    elif float(grades[key]) >= 68:
        grades[key] = 'C-'
    elif float(grades[key]) >= 60:
        grades[key] = 'D'
    elif float(grades[key]) >= 0:
        grades[key] = 'F'
    else:
        grades[key] = grades[key] + ' Error.'
print grades

handle = open('letter_grades.txt', 'w')
for line in grades:
    handle.write(line + ' ' + grades[line] + '\n')
handle.close()

# done