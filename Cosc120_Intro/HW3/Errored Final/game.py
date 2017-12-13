import gmod1, pylab, sys, time
from random import randint
from colorama import Fore as fore, Back as back, Style as sty
#box = pylab.figure(1) # couldn't output strings
from time import sleep
def typing1(text):
    for i in text:
        sys.stdout.write(fore.GREEN + back.BLACK + sty.BRIGHT + i)
        sleep(.05)

def typing2(text):
    for i in text:
        sys.stdout.write(fore.WHITE + back.BLACK + i)
        sleep(.05)
typing1('Please step into...\n')
sleep(3)
print 'THE DOJO!'
sleep(2)
typing1('by: Richard Flores\n')
sleep(1)
raw_input('Press Enter to begin..')
save = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
savefilehandle = open('save.txt','r')
savei = 0
for line in savefilehandle:
    if savei == 2:
        break
    save[savei] == line
    savei += 1
savefilehandle.close()
prevlosses = save[0]
prevwins = save[1]
while True:
    print '''
    [1] : New Game
    [2] : Load Last Save'''
    print 'Loses:,', prevlosses, '| Wins:', prevwins
    try:
        gamestart = int(raw_input('> '))
        if gamestart == 1 or gamestart == 2:
            break
        else:
            pass
    except ValueError:
        pass
if gamestart == 2:
    savehandle = open('save.txt', 'r')
    savei = 0
    for line in savehandle:
        if savei <= 1:
            savei += 1
            pass
        save[savei] = line
        savei += 1
    savehandle.close()
    name = 'Name'
    AIname = 'Anti-' + name
    vitals = save[2]
    AIvitals = save[3]
    room = save[4]
    AIroom = save[5]
    prevroom = save[6]
    AIprevroom = save[7]
    position = save[8]
    AIposition = save[9]
    traps = save[10]
    traphouses = save[11]
    sound_alert = save[12]
    AIsound_alert = save[13]
    sound_notification = save[14]
    status = save[15]
    AIstatus = save[16]
    death = save[17]
    kill = save[18]
    turn = save[19]
    trset = save[20]
    counterOW = save[21]
    AIcounterOW = save[22]
    trapcountdown = save[23]
    error = 0
    saved = 0
else:
    typing2('Actually before we begin, let me explain the mechanics!\n')
    typing2('You will move room to room, trying to stealthily kill the other ninja.\n')
    typing2('You kill each other by WATCHING a door, ENTERING a door, SETTING TRAPS, or entering OVERWATCH.\n')
    typing2('WATCHING a door will have you set up at a door in your room to ambush the enemy.\n')
    typing2('ENTERING a door will have you enter the room where you again choose a position to wait for the enemy.\n')
    typing2('SETTING TRAPS will cause your enemy to be stuck for 2 turns. Traps can only be set in corner rooms.\n')
    typing2('Entering OVERWATCH will cause you to watch all the doors for the enemy, but with a chance of failure.\n'
            'Be warned, consecutively doing this will increase the chance of failure until you move to a new room.\n'
            'The rooms a distributed as a 3-by-3 building with adjacent rooms connected, not counting diagnoly.\n'
            'You can check your location by calling on the map and checking where you are. Your room number will\n'
            'be shown at the begining of every turn.\n'
            'That\'s about it. Don\'t die.\n')
    raw_input('Press Enter to continue..')
    name = 'Name'
    AIname = 'Anti-'+ name
    vitals = 1
    AIvitals = 1
    room = 8
    AIroom = 2
    prevroom = 8
    AIprevroom = 2
    position = 0
    AIposition = 0
    traps = ['room1', 'room3', 'room7', 'room 9'] # trap1, trap2, trap3, trap4
    traphouses = [1, 3, 7, 9]
    sound_alert = 0
    AIsound_alert = 0
    sound_notification = 0
    status = 0
    AIstatus = 0
    death = 0
    kill = 0
    turn = 0
    trset = 0
    counterOW = 0
    AIcounterOW = 0
    trapcountdown = ['inactive','inactive','inactive','inactive']
    error = 0
    saves = 0
    typing1('"Welcome Genji."\n')
    raw_input('..')
    typing1('"The time has come to prove you are the strongest in the clan yet again."\n')
    raw_input('..')
    typing1('"This time it is your brother, Hanzo, who has challenged you."\n')
    raw_input('..')
    typing1('"You both live by the laws of the clan. And both knew of this possibility when joining."\n')
    typing1('"But enough talk, you know what to do.Enter the dojo."\n')
    typing2('You enter. The doors shut behind.')
while True: #overall loop, each round, keeps going till someone is killed
    if saved == 1:
        break
    if vitals == 0 or AIvitals ==0:
        break
    if error == 0:
        for c in range(len(trapcountdown)):
            if trapcountdown[c] != 'inactive':
                trapcountdown[c] -= 1
            if trapcountdown[c] == 0:
                trapcountdown[c] = 'inactive'
        turn += 1
    error = 0
    while True: # loop where player inputs commands and etc
        if status >= 1:
            print 'You seem to be stuck, no actions this turn. Hopefully the enemy isn\'t nearby..'
            status = status - 1
            if status == 0:
                i = 0
                for v in range(len(traphouses)):
                    if v == room:
                        i = v
                traps[i] = 'no'
            break
        print 'Turn:', turn, '| Room:', room
        yo = "What will you do?\n" + '[Watch],[Enter],[Overwatch],[Help],[Map],[Save]'
        if room in traphouses:
            yo = yo + ',[Set Trap]'
        print yo
        ch = raw_input('> ').lower()
        ch1 = ''
        for q in ch:
            if q in 'abcdefghijklmnopqrstuvwxyz':
                ch1 += q
        if ch1 == 'help':
            gmod1.Help(room)
            error = 1
        elif ch1 == 'watch':
            ch2w = gmod1.watch(room)
            if 1 <= ch2w[0] <= 4:
                position = ch2w[0]
                #print position
                #break
            else:
                error = 1
        elif ch1 == 'enter':
            ch2e = gmod1.enter(room, AIroom, AIposition, traps[0], traps[1], traps[2], traps[3])
            #print ch2e
            #print type(ch2e)
            if ch2e[0] == 0:
                error = 1
                pass
            elif ch2e[0] == 'restart':
                error = 1
                break
            else:
                counterOW = 0
                # results = ['Previous Room', 'New Room', 'entrance door', 'trapped?', 'sound alert']
                prevroom = ch2e[0]
                room = ch2e[1]
                entrance = ch2e[2]
                sound_alert = ch2e[4]
                position = 0
                if ch2e[3] == 'yes':
                    status = 2
                    print 'Trapped! Oh you fool.'
                    if room == 1:
                        traps[0] = 'inactive'
                        trapcountdown[0] = 'inactive'
                    if room == 3:
                        traps[1] = 'inactive'
                        trapcountdown[1] = 'inactive'
                    if room == 7:
                        traps[2] = 'inactive'
                        trapcountdown[2] = 'inactive'
                    if room == 9:
                        traps[3] = 'inactive'
                        trapcountdown[3] = 'inactive'
                    #break
                else:
                    if room == AIroom:
                        if AIposition == 5:
                            chance = randint(1, 10)
                            if AIcounterOW == 0:
                                if 1 <= chance <= 7:
                                    vitals = 0
                                    death = 2
                                    break
                                else:
                                    AIvitals = 0
                                    kill = 2
                                    break
                            elif AIcounterOW == 1:
                                if 1 <= chance <= 4:
                                    vitals = 0
                                    death = 2
                                    break
                                else:
                                    AIvitals = 0
                                    kill = 2
                                    break
                            elif AIcounterOW >= 2:
                                if 1 <= chance <= 2:
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
                        elif status >= 1:
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
            ch2t = gmod1.set_trap(room, traphouses, traps, name, name)
            if traps == ch2t:
                error = 1
                break
            traps = ch2t[0]
            trapcountdown[ch2t[1]] = 3
        elif ch1 == 'overwatch':
            position = 5
            counterOW += 1
            print 'You prepare yourself.'
        elif ch1 == 'map':
            print'''
            |1|-|2|-|3|
             |   |   |
            |4|-|5|-|6|
             |   |   |
            |7|-|8|-|9|'''
            raw_input('Press Enter to continue..')
            error = 1
        elif ch1 == 'save':
            while True:
                print 'Save and exit?\nThis will overwrite your last save.\n[0]: No, [1]: Yes'
                try:
                    ch2s = int(raw_input('> '))
                    if ch2s == 0 or ch2s == 1:
                        break
                    else:
                        pass
                except ValueError:
                    pass
            if ch2s == 0:
                error = 1
                break
            else:
                savehandle = open('save.txt','w')
                savei = 0
                for line in savehandle:
                    if savei <= 1:
                        savei += 1
                        pass
                    line = save[savei]
                savehandle.close()
                saved = 1
        else:
            error = 1
        break
    while True: # AI turn, made a loop to help me organize thoughts
        if saved == 1:
            break
        if error != 0:
            break
        if AIstatus >= 1:
            AIstatus = AIstatus - 1
            break
        if AIroom in traphouses:
            for i in range(len(traphouses)):
                if AIroom == traphouses[i]:
                    if traps[i] == 1:
                        AIch == 1
                    else:
                        AIch == 3
        else:
            AIch = randint(0,2)
        if AIch == 0: #watch
            AIch = gmod1.AIwatch(AIroom)
            AIposition = AIch[0]
        elif AIch == 1: # enter
            AIcounterOW = 0
            AIch = gmod1.AIenter(AIroom, room, position, traps[0], traps[1], traps[2], traps[3])
            AIprevroom = AIch[0]
            AIroom = AIch[1]
            entrance = AIch[2]
            sound_alert = AIch[4]
            AIposition = 0
            if AIch[3] == 'enemy yes':
                AIstatus = 2
                if AIroom == 1:
                    traps[0] = 'inactive'
                    trapcountdown[0] = 'inactive'
                if AIroom == 3:
                    traps[1] = 'inactive'
                    trapcountdown[1] = 'inactive'
                if AIroom == 7:
                    traps[2] = 'inactive'
                    trapcountdown[2] = 'inactive'
                if AIroom == 9:
                    traps[3] = 'inactive'
                    trapcountdown[3] = 'inactive'
                # break
            else:
                if room == AIroom:
                    if position == 5:
                        chance = randint(1, 10)
                        if counterOW == 0:
                            if 1 <= chance <= 7:
                                AIvitals = 0
                                kill = 3
                                break
                            else:
                                vitals = 0
                                death = 3
                                break
                        elif counterOW== 1:
                            if 1 <= chance <= 4:
                                AIvitals = 0
                                kill = 3
                                break
                            else:
                                vitals = 0
                                death = 3
                                break
                        elif counterOW >= 2:
                            if 1 <= chance <= 2:
                                AIvitals = 0
                                kill = 3
                                break
                            else:
                                vitals = 0
                                death = 3
                                break
                    elif position == entrance:
                        AIvitals = 0
                        kill = 1
                        break
                    elif position != entrance and position != 5:
                        chance = randint(1, 100)
                        if 1 <= chance <= 75:
                            vitals = 0
                            death = 4
                            break
                        else:
                            AIvitals = 0
                            kill = 4
                            break
                    elif AIstatus >= 1:
                        AIvitals = 0
                        kill = 5
                        break
            AIch2e = gmod1.AIwatch(AIroom)
            AIposition = AIch2e[0]
            if AIposition == 5:
                AIcounterOW += 1
        elif AIch == 2: # overwatch
            AIposition = 5
            AIcounterOW += 1
        elif AIch == 3: #set trap
            AIch2t = gmod1.set_trap(room, traphouses, traps, name, name)
            if traps == AIch2t:
                error = 1
                break
            traps = AIch2t[0]
            trapcountdown[AIch2t[1]] = 3

        break
    save[2] = vitals
    save[3] = AIvitals
    save[4] = room
    save[5] = AIroom
    save[6] = prevroom
    save[7] = AIprevroom
    save[8] = position
    save[9] = AIposition
    save[10] = traps
    save[11] = traphouses
    save[12] = sound_alert
    save[13] = AIsound_alert
    save[14] = sound_notification
    save[15] = status
    save[16] = AIstatus
    save[17] = death
    save[18] = kill
    save[19] = turn
    save[20] = trset
    save[21] = counterOW
    save[22] = AIcounterOW
    save[23] = trapcountdown
# print vitals
# print AIvitals
# print death
# print kill
def typing3(text):
    for i in text:
        sys.stdout.write(fore.BLACK + back.RED + i)
        sleep(.05)
if kill == 1:
    typing3('You waited quietly and put a knife in Hanzo\'s back as he entered the room.' )
if kill == 2:
    typing3('Hanzo tried to watch for you, but you were quicker.')
if kill == 3:
    typing3('You were ready for Hanzo, he wasn\'t ready for you.')
if kill == 4:
    typing3('Hanzo thought he had the jump on you. He was dead wrong.')
if kill == 5:
    typing3('Hanzo was stuck in your trap. What a fool!')
if kill == 6:
    typing3("Hanzo didn't even see you coming..")
if kill >= 1:
    typing3("You are still the strongest! .. But was it worth it?")
    prevwins += 1
    savehandle = open('save.txt', 'w')
    savei = 0
    for line in savehandle:
        if savei == 0:
            savei += 1
            pass
        elif savei == 1:
            line = prevwins
            break
    savehandle.close()
if death == 1:
    typing3('Hanzo waited quietly and put a knife in your back as you entered the room.')
if death == 2:
    typing3('Hanzo was ready for you, you weren\'t ready for Hanzo.')
if death == 3:
    typing3('You tried to watch for Hanzo, but he was quicker.')
if death == 4:
    typing3("You didn't even see Hanzo coming..")
if death == 5:
    typing3('You were stuck in your trap. You fool!')
if death == 6:
    typing3('You thought you had the jump on Hanzo. You were dead wrong.')
if death >= 1:
    typing3('Those who live by the blade, die by the blade.')
    prevlosses += 1
    savehandle = open('save.txt','w')
    for line in savehandle:
        line = prevlosses
        break
    savehandle.close()