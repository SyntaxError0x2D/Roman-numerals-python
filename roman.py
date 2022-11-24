symsLS = ["I", "V", "X", "L", "C", "D", "M"]


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

def FromRoman(syms:type=str or list) -> int:
    if not check(syms): return(False)
    tot = 0
    for i in negCheck(syms): tot += i
    return(tot)


### Dec to roman!

def ToRoman(num:type=int) -> str:
    if num > 3999: return(False)
    pieces = [int(str(num)[i])*10**(len(str(num))-i-1) for i in range(len(str(num)))]
    roman = []
    for indx, val in enumerate(pieces):
        baseNum = int(val/10**(len(pieces)-indx-1))
        if baseNum <= 3:
            val = getSym(10**(len(pieces)-indx-1))*baseNum
        elif baseNum == 4: 
            val = getSym(10**(len(pieces)-indx-1)) + getSym(5*10**(len(pieces)-indx-1))
        elif 9>baseNum>4:
            val = getSym(5*10**(len(pieces)-indx-1)) + (getSym(10**(len(pieces)-indx-1)) * (baseNum-5))
        else:
            val = getSym(10**(len(pieces)-indx-1)) + getSym(10**(len(pieces)-indx))
        roman.append(val)
    return("".join(roman))
