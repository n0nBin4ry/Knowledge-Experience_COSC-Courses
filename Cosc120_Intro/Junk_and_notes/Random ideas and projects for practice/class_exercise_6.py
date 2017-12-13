import sys, random as rm
from time import sleep
from colorama import Fore as fore, Back as back, Style as sty
def typing(text):
    for i in text:
        sys.stdout.write(fore.GREEN + back.BLACK + sty.BRIGHT + i)
        sleep(.05)
def choice(text):
    for i in text:
        sys.stdout.write(fore.WHITE + back.BLACK + sty.BRIGHT)
typing("You awaken in a dark room lit by candlelight.\n")
sleep(1)
typing("There is a broken bat, a potato with a suspicious arua around it, and a small rusty kitchen knife on a table.\n")
typing('You hear a voice.\n')
typing('Voice:"Who are you? Grab your item."')
print '[1]: Broken Bat, [2]: Potato, [3]: Rusty Knife'
cclass = ''
while True:
    try:
        cclass = int(raw_input('> '))
    except ValueError:  # if its not an integer then an error will appear and ask for their input again
        pass
    if 1 <= cclass <= 3:
        break
    else:
        pass
if cclass == 1:
    cclass = 'Brute'
    weapon = 'Broken Bat'
    hp = 50
    atk = 4
    df = 4
    spd = 0
    weapon = "Broken Bat"
    #weapons
    print "Ah you prefer pure assurance of a (kinda) sturdy stick to protect you. You must be the Brute."
if cclass == 2:
    cclass = 'Mage'
    weapon = 'Smelly Potato'
    hp = 30
    atk = 6
    df = 2
    spd = 3
    print "Oh someone actually chose the potato? I mean, ah yes you saw through the stench and found.. um that it was" \
          " magic or something. You must be the.. the um.. Mage. Yeah."
if cclass == 3:
    cclass = 'Rogue'
    weapon = 'Rusty Knife'
    hp = 40
    atk = 3
    df = 2
    spd = 5
    print "You prefered the light, sharp, pointy thing even though you don't know where it's been. Moving fast and " \
          "dangerously, you must be the Rogue."
capc = cclass.upper()
print 'Voice: "AH %s!' %capc, 'Welcome, welcome. What have you been up to? I\'m good. Where are the other two? You guys are.."'
print "The voice is cut off by a loud explosion in the room behind you."
print '???: "Oh crap."'
print 'BOOM!! A huge hole was now blown into the back of the room now.'
print 'Two heroic-looking adventurers clad in intriguing armor and non-cruddy weapons run in from the hole. They look weakened and afraid.'
print 'Voice: "Holy crap, are you guys okay? You\'re late!.. Wait where\'d you get that cool gear?'
print 'Hero 1: "No time to explain it\'s..'
print 'A hook flies around the hero\'s chest and pulls them back into the hole. You hear begging, then laughter as a ' \
      'cannon goes off followed by a scream and a thud.'
print 'A deep, almost inhuman, voice comes from the hole.'
print '???: "It?! Well I am a montser I guess.. Ah more fresh meat. Call me Roadhog, I\'ll be killing you this evening.'
print 'Voice: "Um well.. I think I hear someone else starting their quest. Gotta go. Good luck."'
print 'The second hero prepares themself for a fight. They turn back to you.'
print 'Hero 2: "Let\'s go, %s! That thing got our partner!'
print '[1]: Fight, [2]: Run'
# # while True:
# #     try:
# #         dec1 = int(raw_input("> "))
# #     except ValueError:
# #         pass
# #     if 1 <= dec1 <= 2:
# #         break
# #     else:
# #         pass
# # if dec1 == 1:
# #     def Roadhog(hp,atk,df,spd):
# #
