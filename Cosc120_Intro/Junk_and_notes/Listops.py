# for class exercise 6B
#1
def Lsum(L1,L2):
    # type: (object, object) -> object
    if type(L1) == list and type(L2) == list:
        if len(L1) > len(L2):
            i = len(L1)
            j = len(L1) - len(L2)
            LG = L1
            LS = L2
        else:
            i = len(L2)
            j = len(L2) - len(L1)
            LG = L2
            LS = L1
        for x in range(j):
            LS.append(0)
        LSum = LG
        for y in range(i):
            LSum[y] = LG[y] + LS[y]
        return LSum
    else:
        return "Error, both inputs aren't lists"

def Lpow(L,p):
    if type(L) == list and (type(p) == int or type(p) == float):
        for i in range(len(L)):
            L[i] = L[i]**p
        return L
    else:
        return 'Error: the first must be a list, and the second must be an integer or float.'
#2
def Lprod(L1,L2):
    if type(L1) == list and type(L2) == list:
        if len(L1) > len(L2):
            i = len(L1)
            j = len(L1) - len(L2)
            LG = L1
            LS = L2
        else:
            i = len(L2)
            j = len(L2) - len(L1)
            LG = L2
            LS = L1
        for x in range(j):
            LS.append(1)
        LProd = LG
        for y in range(i):
            LProd[y] = LG[y] * LS[y]
        return LProd
    else:
        return "Error, both inputs aren't lists"

def Ldiff(L1,L2):
    if type(L1) == list and type(L2) == list:
        if len(L1) > len(L2):
            i = len(L1)
            j = len(L1) - len(L2)
            k = len(L2)
            LG = L1
            for x in range(i):
                L2.append(0)
        else:
            i = len(L2)
            j = len(L2) - len(L1)
            k = len(L1)
            LG = L2
            for x in range(i):
                L1.append(0)
        LDiff = []
        for y in range(i):
            LDiff.append(0)
        for z in range(i):
            if z > k:
                LDiff[z] = LG[z]
            else:
                LDiff[z] = L1[z] - L2[z]
        return LDiff
    else:
        return "Error, both inputs aren't lists"

def Ldiv(L1,L2):
    if type(L1) == list and type(L2) == list:
        if len(L1) > len(L2):
            i = len(L1)
            j = len(L1) - len(L2)
            k = len(L2)
            LG = L1
            for x in range(i):
                L2.append(0)
        else:
            i = len(L2)
            j = len(L2) - len(L1)
            k = len(L1)
            LG = L2
            for x in range(i):
                L1.append(0)
        LDiv = []
        for y in range(i):
            LDiv.append(1)
        for z in range(i):
            if z > k:
                LDiv[z] = LG[z]
            else:
                LDiv[z] = L1[z] / L2[z]
        return LDiv
    else:
        return "Error, both inputs aren't lists"
