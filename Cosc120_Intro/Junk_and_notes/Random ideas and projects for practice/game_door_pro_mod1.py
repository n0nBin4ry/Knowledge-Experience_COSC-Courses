def choice1(ch):
    print 'What do you do?'
    if ch == 0 or ch == 1:
        print '[1]: Go to door, [2]: Pick up key'
    else:
        print '[1]: Go to door'
    while True:
        try:
            ch1 = int(raw_input('> '))
        except ValueError:
            pass
        if ch1 == 1 or ch1 == 2:
            return ch1
            break
        else:
            pass