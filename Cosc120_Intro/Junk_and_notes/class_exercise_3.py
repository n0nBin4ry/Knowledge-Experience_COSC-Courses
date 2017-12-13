# 1.
#   a.
def fa(x):
    y = (x**2) - 2
    return y
triesa = 0
aa = 0
ba = 2
ca = float(aa-ba)/2
TOLa = 1 * (10**-7)
while abs(fa(ca)) > TOLa:
    triesa += 1
    ca = float(aa - ba) / 2
    if fa(ca) > 0:
        ba = ca
    elif fa(ca) < 0:
        aa = ca
    # print ca
print "It took", triesa, "iterations to find out the squareroot of 2 is", ca

#   b.
def fb(x):
    y = x**3 + (4 * (x**2)) - 10
    return y
triesb = 0
TOLb = 10**(-7)
ab = 1
bb = 2
cb = float(bb - ab) / 2
while abs(fb(cb)) >= TOLb:
    triesb += 1
    cb = float(bb - ab) / 2
    if fb(cb) > 0:
        bb = cb
    elif fb(cb) < 0:
        ab =  cb
    if triesb == 200:
        break
if triesb == 200:
    print "There is no root within 200 iterations"
else:
    print "It took", triesb, "iterations to find the root of f(x) is", cb