from random import randint
from colorama import Fore as fore, Back as back, Style as sty
def Help(room):
    while True:
        i = 0
        print '''
            Welcome to my text game! What can I help you with today?
            [E] : Exit Help
            [1] : What the heck is going on?
            [2] : What does Watch do?
            [3] : What does Enter do?
            [4] : What does Overwatch do?'''
        if room in [1,3,7,9]:
            print '''            [5] : What does Set Trap do?'''
            i = 1
        n = raw_input('> ')
        if n.lower() == 'e':
            break
        elif n.lower() == '1':
            print 'Description of game.'
            raw_input('Press enter to continue..')
            pass
        elif n.lower() == '2':
            print 'Description of Watch'
            raw_input('Press enter to continue..')
            pass
        elif n.lower() == '3':
            print 'description of Enter.'
            raw_input('Press enter to continue..')
            pass
        elif n.lower() == '4':
            print 'description of Overwatch.'
            raw_input('Press enter to continue..')
            pass
        elif n.lower() == '5' and i == 1:
            print 'Description of Set Trap.'
            raw_input('Press enter to continue..')
            pass
        # else:
        #     pass

def watch(room):
    results = ['room position', 'hi']
    print 'Which door?'
    x = raw_input('> ').lower()
    if x == 'help':
        Help(room)
    if room == 1:
        if x == 'bottom':
            results[0] = 1
            return results
        elif x == 'right':
            results[0] = 2
            return results
        elif x == 'left' or x == 'bottom':
            print 'There is no door there.'
            results[0] = 0
            return results
        else:
            print 'Hmm, that\'s not right..'
            results[0] = 0
            return results
    if room == 2:
        if x == "left":
            results[0] = 4
            return results
        elif x == 'bottom':
            results[0] = 1
            return results
        elif x == 'right':
            results[0] = 2
            return results
        elif x == 'top':
            print 'There is no door there.'
            results[0] = 0
            return results
        else:
            print 'Hmm, that\'s not right..'
            results[0] = 0
            return results
    if room == 3:
        if x == 'left':
            results[0] = 4
            return results
        elif x == 'bottom':
            results[0] = 1
            return results
        elif x == 'top' or x == 'right':
            print 'There is no door there.'
            results[0] = 0
            return results
        else:
            print 'Hmm, that\'s not right..'
            results[0] = 0
            return results
    if room == 4:
        if x == 'bottom':
            results[0] = 1
            return results
        elif x == 'right':
            results[0] = 2
            return results
        elif x == 'top':
            results[0] = 3
            return results
        elif x == 'bottom':
            print 'There\'s no door there.'
            results[0] = 0
            return results
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
            return results
    if room == 5:
        if x == 'bottom':
            results[0] = 1
            return results
        elif x == 'right':
            results[0] = 2
            return results
        elif x == 'top':
            results[0] = 3
            return results
        elif x == 'left':
            results[0] = 4
            return results
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
            return results
    if room == 6:
        if x == 'bottom':
            results[0] = 1
            return results
        elif x == 'top':
            results[0] = 3
            return results
        elif x == 'left':
            results[0] = 4
            return results
        elif x == 'right':
            print 'There\'s no door there.'
            results[0] = 0
            return results
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
            return results
    if room == 7:
        if x == 'right':
            results[0] = 2
            return results
        elif x == 'top':
            results[0] = 3
            return results
        elif x == 'left' or x == 'bottom':
            print 'There\'s no door there.'
            results[0] = 0
            return results
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
            return results
    if room == 8:
        if x == 'right':
            results[0] = 2
            return results
        elif x == 'top':
            results[0] = 3
            return results
        elif x == 'left':
            results[0] = 4
            return results
        elif x == 'bottom':
            print 'There\'s no door there.'
            results[0] = 0
            return results
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
            return results
    if room == 9:
        if x == 'top':
            results[0] = 3
            return results
        elif x == 'left':
            results[0] = 4
            return results
        elif x == 'right' or x == 'bottom':
            print 'There\'s no door there.'
            results[0] = 0
            return results
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
            return results


def enter(room, enemyroom, enemyposition, trapstatus_rm1, trapstatus_rm3, trapstatus_rm7, trapstatus_rm9):
    results = ['Previous Room', 'New Room', 'entrance', 'trapped?', 'sound alert']
    print 'Which door?'
    x = raw_input('> ').lower()
    if x == 'help':
        Help(room)
        #enter(room, enemyroom, enemyposition, trapstatus_rm1, trapstatus_rm3, trapstatus_rm7, trapstatus_rm9)
        results = ['restart']
        return results
    if room == 1:
        if x == 'bottom':
            results[0] = room
            results[1] = 4
            results[2] = 3
        elif x == 'right':
            results[0] = room
            results[1] = 2
            results[2] = 4
        elif x == 'left' or x == 'bottom':
            print 'You can\'t walk through walls!'
            results[0] = 0
        else:
            print 'Hmm, that\'s not right..'
            results[0] = 0
    elif room == 2:
        if x == "left":
            results[0] = room
            results[1] = 1
            results[2] = 2
        elif x == 'bottom':
            results[0] = room
            results[1] = 5
            results[2] = 3
        elif x == 'right':
            results[0] = room
            results[1] = 3
            results[2] = 4
        elif x == 'top':
            print 'You can\'t walk through walls!'
            results[0] = 0
            return results
        else:
            print 'Hmm, that\'s not right..'
            results[0] = 0
            return results
    elif room == 3:
        if x == 'bottom':
            results[0] = room
            results[1] = 6
            results[2] = 3
        elif x == 'left':
            results[0] = room
            results[1] = 2
            results[2] = 2
        elif x == 'top' or x == 'bottom':
            print 'You can\'t walk through walls!'
            results[0] = 0
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
    elif room == 4:
        if x == 'bottom':
            results[0] = room
            results[1] = 7
            results[2] = 3
        elif x == 'right':
            results[0] = room
            results[1] = 5
            results[2] = 4
        elif x == 'top':
            results[0] = room
            results[1] = 1
            results[2] = 1
        elif x == 'left':
            print 'You can\'t walk through walls!'
            results[0] = 0
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
    elif room == 5:
        if x == 'bottom':
            results[0] = room
            results[1] = 8
            results[2] = 3
        elif x == 'right':
            results[0] = room
            results[1] = 6
            results[2] = 4
        elif x == 'top':
            results[0] = room
            results[1] = 2
            results[2] = 1
        elif x == 'left':
            results[0] = room
            results[1] = 4
            results[2] = 2
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
    elif room == 6:
        if x == 'bottom':
            results[0] = room
            results[1] = 9
            results[2] = 3
        elif x == 'top':
            results[0] = room
            results[1] = 3
            results[2] = 1
        elif x == 'left':
            results[0] = room
            results[1] = 5
            results[2] = 2
        elif x == 'right':
            print 'You can\'t walk through walls!'
            results[0] = 0
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
    elif room == 7:
        if x == 'right':
            results[0] = room
            results[1] = 8
            results[2] = 4
        elif x == 'top':
            results[0] = room
            results[1] = 4
            results[2] = 1
        elif x == 'bottom' or x == 'left':
            print 'You can\'t walk through walls!'
            results[0] = 0
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
    elif room == 8:
        if x == 'right':
            results[0] = room
            results[1] = 9
            results[2] = 4
        elif x == 'top':
            results[0] = room
            results[1] = 5
            results[2] = 1
        elif x == 'left':
            results[0] = room
            results[1] = 7
            results[2] = 2
        elif x == 'bottom':
            print 'You can\'t walk through walls!'
            results[0] = 0
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
    elif room == 9:
        if x == 'top':
            results[0] = room
            results[1] = 6
            results[2] = 1
        elif x == 'left':
            results[0] = room
            results[1] = 8
            results[2] = 2
        elif x == 'bottom' or x == 'right':
            print 'You can\'t walk through walls!'
            results[0] = 0
        else:
            print 'Hmm that\'s not right..'
            results[0] = 0
    else:
        results[0] = 0
        return results
    if results[1] == 1:
        if trapstatus_rm1 == 1:
            results[3] = 'yes'
        elif trapstatus_rm1 == 2:
            results[3] = 'enemy yes'
        else:
            pass
    if results[1] == 3:
        if trapstatus_rm3 == 1:
            results[3] = 'yes'
        elif trapstatus_rm3 == 2:
            results[3] = 'enemy yes'
        else:
            pass
    if results[1] == 7:
        if trapstatus_rm7 == 1:
            results[3] = 'yes'
        elif trapstatus_rm7 == 2:
            results[3] = 'enemy yes'
        else:
            pass
    if results[1] == 9:
        if trapstatus_rm9 == 1:
            results[3] = 'yes'
        elif trapstatus_rm9 == 2:
            results[3] = 'enemy yes'
        else:
            pass
    return results

# template
    # if room == :
    #     if x == 'bottom':
    #         results[0] = 1
    #         return results
    #     elif x == 'right':
    #         results[0] = 2
    #         return results
    #     elif x == 'top':
    #         results[0] = 3
    #         return results
    #     elif x == 'left':
    #         results[0] = 4
    #         return results
    #     elif x ==:
    #         print 'There\'s no door there.'
    #         results[0] = 0
    #         return results
    #     else:
    #         print 'Hmm that\'s not right..'
    #         results[0] = 0
    #         return results


#Template 2
# if x == 'bottom':
#     results[0] = room
#     results[1] =
#     results[2] = 3
# elif x == 'right':
#     results[0] = room
#     results[1] =
#     results[2] = 4
# elif x == 'top':
#     results[0] = room
#     results[1] =
#     results[2] = 1
# elif x == 'left':
#     results[0] = room
#     results[1] =
#     results[2] = 2
# elif x ==:
#     print 'You can\'t walk through walls!'
#     results[0] = 0
# else:
#     print 'Hmm that\'s not right..'
#     results[0] = 0

def set_trap(room, traphouses, traps, char, name):
    if room in traphouses:
        for i in range(len(traphouses)):
            if room == traphouses[i]:
                x = i
                break
        if char == 'Anti-' + name:
            traps[x] = 1
            #print 'AI set trap'
        else:
            traps[x] = 2
            print 'The trap is set. Happy hunting.'
        return [traps, x]
    else:
        print "Hmm that's not right.."
        return [traps]


#AI
def AIwatch(room): #similar, to watch, but automated and no prints
    results = ['room position', 'hi']
    if room == 1:
        x = randint(0,1)
        if x == 0: # 'bottom':
            results[0] = 1
            return results
        elif x == 1: # 'right':
            results[0] = 2
            return results
    if room == 2:
        x = randint(0,2)
        if x == 0: # "left":
            results[0] = 4
            return results
        elif x == 1: # 'bottom':
            results[0] = 1
            return results
        elif x == 2: # 'right':
            results[0] = 2
            return results
    if room == 3:
        x = randint(0,1)
        if x == 0: # 'left':
            results[0] = 4
            return results
        elif x == 1: # 'bottom':
            results[0] = 1
            return results
    if room == 4:
        x = randint(0,2)
        if x == 0: # 'bottom':
            results[0] = 1
            return results
        elif x == 1: # 'right':
            results[0] = 2
            return results
        elif x == 2: # 'top':
            results[0] = 3
            return results
    if room == 5:
        x = randint(0,3)
        if x == 0: # 'bottom':
            results[0] = 1
            return results
        elif x == 1: # 'right':
            results[0] = 2
            return results
        elif x == 2: # 'top':
            results[0] = 3
            return results
        elif x == 3: # 'left':
            results[0] = 4
            return results
    if room == 6:
        x = randint(0,2)
        if x == 0: #  'bottom':
            results[0] = 1
            return results
        elif x == 1: # 'top':
            results[0] = 3
            return results
        elif x == 2: # 'left':
            results[0] = 4
            return results
    if room == 7:
        x = randint(0,1)
        if x == 0: # 'right':
            results[0] = 2
            return results
        elif x == 1: # 'top':
            results[0] = 3
            return results
    if room == 8:
        x = randint(0,2)
        if x == 0: # 'right':
            results[0] = 2
            return results
        elif x == 1: # 'top':
            results[0] = 3
            return results
        elif x == 2: # 'left':
            results[0] = 4
            return results
    if room == 9:
        x = randint(0,1)
        if x == 0: # 'top':
            results[0] = 3
            return results
        elif x == 1: # 'left':
            results[0] = 4
            return results

def AIenter(room, enemyroom, enemyposition, trapstatus_rm1, trapstatus_rm3, trapstatus_rm7, trapstatus_rm9):
    results = ['Previous Room', 'New Room', 'entrance', 'trapped?', 'sound alert']
    if room == 1:
        x = randint(0,1)
        if x == 0: # 'bottom':
            results[0] = room
            results[1] = 4
            results[2] = 3
        elif x == 1: # 'right':
            results[0] = room
            results[1] = 2
            results[2] = 4
    elif room == 2:
        x = randint(0,2)
        if x == 0: # "left":
            results[0] = room
            results[1] = 1
            results[2] = 2
        elif x == 1: # 'bottom':
            results[0] = room
            results[1] = 5
            results[2] = 3
        elif x == 2: # 'right':
            results[0] = room
            results[1] = 3
            results[2] = 4
    elif room == 3:
        x = randint(0,1)
        if x == 0: # 'bottom':
            results[0] = room
            results[1] = 6
            results[2] = 3
        elif x == 1: # 'left':
            results[0] = room
            results[1] = 2
            results[2] = 2
    elif room == 4:
        x = randint(0,2)
        if x == 0: # 'bottom':
            results[0] = room
            results[1] = 7
            results[2] = 3
        elif x == 1: #'right':
            results[0] = room
            results[1] = 5
            results[2] = 4
        elif x == 2: # 'top':
            results[0] = room
            results[1] = 1
            results[2] = 1
    elif room == 5:
        x = randint(0,3)
        if x == 0: # 'bottom':
            results[0] = room
            results[1] = 8
            results[2] = 3
        elif x == 1: # 'right':
            results[0] = room
            results[1] = 6
            results[2] = 4
        elif x == 2: # 'top':
            results[0] = room
            results[1] = 2
            results[2] = 1
        elif x == 3: # 'left':
            results[0] = room
            results[1] = 4
            results[2] = 2
    elif room == 6:
        x = randint(0,2)
        if x == 0: # 'bottom':
            results[0] = room
            results[1] = 9
            results[2] = 3
        elif x == 1: # 'top':
            results[0] = room
            results[1] = 3
            results[2] = 1
        elif x == 2: # 'left':
            results[0] = room
            results[1] = 5
            results[2] = 2
    elif room == 7:
        x = randint(0,1)
        if x == 0: # 'right':
            results[0] = room
            results[1] = 8
            results[2] = 4
        elif x == 1: # 'top':
            results[0] = room
            results[1] = 4
            results[2] = 1
    elif room == 8:
        x = randint(0,2)
        if x == 0: # 'right':
            results[0] = room
            results[1] = 9
            results[2] = 4
        elif x == 1: # 'top':
            results[0] = room
            results[1] = 5
            results[2] = 1
        elif x == 2: # 'left':
            results[0] = room
            results[1] = 7
            results[2] = 2
    elif room == 9:
        x = randint(0,1)
        if x == 0: # 'top':
            results[0] = room
            results[1] = 6
            results[2] = 1
        elif x == 1: # 'left':
            results[0] = room
            results[1] = 8
            results[2] = 2
    else:
        results[0] = 0
        return results
    if results[1] == 1:
        if trapstatus_rm1 == 1:
            results[3] = 'yes'
        elif trapstatus_rm1 == 2:
            results[3] = 'enemy yes'
        else:
            pass
    if results[1] == 3:
        if trapstatus_rm3 == 1:
            results[3] = 'yes'
        elif trapstatus_rm3 == 2:
            results[3] = 'enemy yes'
        else:
            pass
    if results[1] == 7:
        if trapstatus_rm7 == 1:
            results[3] = 'yes'
        elif trapstatus_rm7 == 2:
            results[3] = 'enemy yes'
        else:
            pass
    if results[1] == 9:
        if trapstatus_rm9 == 1:
            results[3] = 'yes'
        elif trapstatus_rm9 == 2:
            results[3] = 'enemy yes'
        else:
            pass
    return results
