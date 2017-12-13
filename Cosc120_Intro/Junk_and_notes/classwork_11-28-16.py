#Dictionaries (dict)
# similar to lists but indices are not integers
# key-value pair. EX: look up student off their social security number.
# ofther key values: name, phone #, student ID #, address

# collection that allows us to look up info associated to arbitrary keys is called a MAPPING in pthyon.
    # similar to hashes or associative arrays
#EX: Dictionary that stores usernames and passwords
passwd = { 'gene' : 'superprogrammer' , 'turning' : 'genius' , 'bill' : 'monopoly' } # 'key':'value'
print type(passwd)
print passwd
passwd
print passwd['gene'] # key
# returns value of key 'gene'
# <dictionary>[<key>] returns object associated to given key
passwd['bill'] = 'bluescreen'
#changed value of key 'bill'
# DICTIONARIES are MUTABLE
print len(passwd) # returns 3, the number of keys
print passwd.keys() # returns all keys in dictionary
print passwd.values() # returns all values dictionary
print passwd.get('gene') # same as passwd['gene']
print passwd.get('sam','woops') # prints woops if key is not in dictionary: <dictionary>.get(<key>, <default>)
print sorted(passwd) # makes a list of keys, not a sorted dictionary
print passwd
#create a dicitonary of 10 students and grades. update 1/2 of them by 1/2 letter grade