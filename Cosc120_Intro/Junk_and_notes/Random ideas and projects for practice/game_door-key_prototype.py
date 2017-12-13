inventory = []
print 'You are in a room.'
print 'There is a key on the ground and a door.'
print 'What do you do?'
print '[1]: Go to door, [2]: Pick up key'
import game_door_pro_mod1 as md1
inventory = []
room1 = 0
Key = "Key"
a = md1.choice1(room1)
# while True:
#     ch1 = 0
#     try:
#         ch1 = int(raw_input('> '))
#     except ValueError:
#         pass
#     if ch1 == 1 or ch1 == 2:
#         x = ch1
#         break
#     else:
#         pass
if a == 1:
    if Key in inventory:
        b = md1.choice2
    else:
        print "The door is locked"
        x = md1.choice1