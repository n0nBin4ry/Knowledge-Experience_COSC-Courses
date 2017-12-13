alpha = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n = raw_input("How many names will you input?")
n = int(n)
names = ['']
place = ''
for i in range(1,n):
    names.append('')
for i in range(n):
    names[i] = raw_input("Input name:")
print names
# for i in range(len(names)-1):
#     for j in range(len(names[i])):
#         if j == len(names[i]):
#             break
#         if alpha.index((names[i])[j]) < alpha.index((names[i+1])[j]):
#             place = names[i]
#             names[i] = names[i-1]
#             names[i-1] = place
# print names
print sorted(names)
#couldve just used sorted()

