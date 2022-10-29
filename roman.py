symsLS = ["I", "V", "X", "L", "C", "D", "M", "⊽", "x̄"]


def getVal(sym):
    indx = symsLS.index(sym)
    if indx % 2 == 0: return(int(10**((indx)/2)))
    else: return(int(5*10**((indx-1)/2)))

def numVal(num):
    return(symsLS[[getVal(i) for i in symsLS].index(num)])    

def getVals(syms):
    tot = []
    for i in syms:
        tot.append(getVal(i))
    return(tot)

def sndx(sym): return(symsLS.index(numVal(sym)))
def getSym(val): return(symsLS[getVals(symsLS).index(val)])
def makeLS(str): return([i for i in str])
def reverse(ls): return([ls[-i-1] for i in range(len(ls))])


### Roman to dec!


def negCheck(syms):
    syms = getVals(syms)
    for indx, val in enumerate(syms):
        if indx+1<len(syms) and val < syms[indx+1]:
            diff = sndx(val) - sndx(syms[indx+1])
            if diff == -1 or diff == -2 and sndx(val) % 2 == 0:
                syms[indx] = -val
            else: return(False)
    return(syms)

def rowCheck(syms):
    syms = getVals(syms)
    latest = 0
    row = 0
    for indx, val in enumerate(syms):
        if val == latest:
            row += 1
        else: row = 0 ; latest = val
        if row > 0 and sndx(latest) % 2 != 0:
            return(False)
        elif row > 2:
            return(False)
    return(True)



def check(syms):
    if negCheck(syms) and rowCheck(syms): return(True)
    else: return(False)

def FromRoman(syms: type=str) -> int:
    syms = syms.upper()
    if not check(syms): return(False)
    tot = 0
    for i in negCheck(syms): tot += i
    return(tot)


### Dec to roman!

def rough(num):
    rollN = 1
    Roman = []
    while rollN != len(symsLS)+1:
        if num - getVal(symsLS[-rollN]) >= 0:
            Roman.append(symsLS[-rollN])
            num -= getVal(symsLS[-rollN])
        else: rollN += 1
    return(Roman)

def clean(Roman):
    latest = ""
    row = 0
    rows = []
    for indx, val in enumerate(Roman):
        if val == latest:
            row += 1
        else: row = 0 ; latest = val
        if row > 2:
            rows.append([indx-3, indx+1])
    rms = []
    for i in rows:
        tot = 0
        for n in Roman[i[0]:i[1]]: tot += getVal(n)
        tot += getVal(Roman[i[0]])
        Roman[i[0]:i[0]+2] = [symsLS[sndx(tot)-1], getSym(tot)]
        for i in range(i[0]+2, i[1]):
            rms.append(i)
    neoRoman = ""
    for i in range(len(Roman)):
        if i not in rms: neoRoman += Roman[i]
    return(neoRoman)

def ToRoman(num: type=int) -> str:
    return(clean(rough(num)))


