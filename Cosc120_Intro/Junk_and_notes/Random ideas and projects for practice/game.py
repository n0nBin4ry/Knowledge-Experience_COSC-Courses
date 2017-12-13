import gmod1
from random import randint
# x = raw_input("> ")
# try:
#     gmod1.Help(x)
# except ValueError:
#     pass # input prototype
name = 'Name'
AIname = 'Anti-'+ name
vitals = 1
AIvitals = 1
room = 8
AIroom = 2
prevroom = 8
AIprevroom = 2
position = 0
AIposition = 1
traps = ['room1', 'room3', 'room7', 'room9']
traphouses = [1, 3, 7, 9]
sound_alert = 0
AIsound_alert = 0
sound_notification = 0
status = 0
AIstatus = 0
death = 0
kill = 0
turn = 1
while True:
    if room == AIroom:
        if AIstatus == 1:
            AIvitals = 0
            kill = 5
    if vitals == 0 or AIvitals == 0:
        break
    if status == 1:
        print 'You seem to be stuck, no actions this turn. Hopefully the enemy isn\'t nearby..'
        status = status - 1
        break
    print turn
    yo = "You will die here.\n" + "What will you do?"
    print yo
    ch = raw_input('> ').lower()
    ch1 = ''
    for q in ch:
        if q in 'abcdefghijklmnopqrstuvwxyz':
            ch1 += q


    if ch1 == 'help':
        gmod1.Help(room)
        pass
    elif ch1 == 'watch':
        ch2w = gmod1.watch(room)
        if 1 <= ch2w[0] <= 4:
            position = ch2w[0]
            print position
            break
        else:
            pass
    elif ch1 == 'enter':
        ch2e = gmod1.enter(room, AIroom, AIposition, traps[0], traps[1], traps[2], traps[3])
        print ch2e
        print type(ch2e)
        if ch2e[0] == 0:
            pass
        else:
            # results = ['Previous Room', 'New Room', 'entrance door', 'trapped?', 'sound alert']
            prevroom = ch2e[0]
            room = ch2e[1]
            entrance = ch2e[2]
            sound_alert = ch2e[4]
            position = 0
            if ch2e[3] == 'yes':
                status = 1
                break
            else:
                if room == AIroom:
                    if AIposition == 5:
                        chance = randint(1, 10)
                        if 1 <= chance <= 7:
                            vitals = 0
                            death = 2
                            break
                        else:
                            AIvitals = 0
                            kill = 2
                            break
                    elif AIposition == entrance:
                        vitals = 0
                        death = 1
                        break
                    elif AIposition != entrance and AIposition != 5:
                        chance = randint(1, 100)
                        if 1 <= chance <= 75:
                            AIvitals = 0
                            kill = 6
                            break
                        else:
                            vitals = 0
                            death = 6
                            break
                    elif status == 1:
                        vitals = 0
                        death = 5
                        break
                print 'Which wall will you take cover at? Or will you go on watch?'
                print '[Left], [Right], [Top], [Bottom], [Overwatch]'
                while True:
                    quick = raw_input('> ').lower()
                    if quick == 'bottom':
                        position = 1
                        break
                    elif quick == 'right':
                        position = 2
                        break
                    elif quick == 'top':
                        position = 3
                        break
                    elif quick == 'left':
                        position = 4
                        break
                    elif quick == 'overwatch':
                        position = 5
                        break
                    elif quick == 'help':
                        print "No help right now. Gotta pick quickly."
                        pass
                    else:
                        pass
    elif ch1 == 'settrap' and room in [1, 3, 7, 9]:
        traps = gmod1.set_trap(room, traphouses, traps, name, name)
    else:
        pass
    turn += 1
print vitals
print AIvitals
print death
print kill