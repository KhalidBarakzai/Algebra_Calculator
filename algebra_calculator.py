#!/usr/bin/python3.8
#Khali081
#Lab Partner: jerome schreiber
def left(e):
    return e[0]


def right(e):
    return e[2]


def op(e):
    return e[1]



def isInside(var,e):
    if type(e) == tuple:
         if var == left(e) or var == right(e):
             return True
         else:
             return isInside(var,left(e)) or isInside(var,right(e))
    else:
        return var == e



def solve(var, q):
    if isInside(var, left(q)):
        return solving(var, q)
    elif isInside(var, right(q)):
        exp = (right(q), op(q), left(q))
        return solving(var, exp)
    else:
        raise ValueError


def solving(var, q):
    if var == left(q):
        return q
    elif isInside(var, left(q)):
        if op(left(q)) == "+":
            return solvingAdd(var,q)
        elif op(left(q)) == "-":
            return solvingSubtract(var,q)
        elif op(left(q)) == "*":
            return solvingMultiply(var,q)
        else:
            return solvingDivide(var,q)


def solvingAdd(var, q):
    if isInside(var, left(left(q))):
        x = (left(left(q)), "=", (right(q), "-", right(left(q))))
        return solving(var,x)  # A=C-B
    elif isInside(var, right(left(q))):
        x2 = (right(left(q)), "=", (right(q), "-", left(left(q))))
        return solving(var,x2) # B=C-A



def solvingSubtract(var, q):
    if isInside(var, left(left(q))):
        x = (left(left(q)), "=", (right(q), "+", right(left(q))))
        return solving(var,x)  # A=C+B
    elif isInside(var, right(left(q))):
        x2 = (right(left(q)), "=", (left(left(q))), "-", right(q))
        return solving(var,x2) # B=C-A



def solvingMultiply(var, q):
    if isInside(var, left(left(q))):
        x = (left(left(q)), "=", (right(q), "/", right(left(q))))
        return solving(var,x)  # A=C*B
    elif isInside(var, right(left(q))):
        x2 = (right(left(q)), "=", (right(q), "/", left(left(q))))
        return solving(var,x2) # B=C*A



def solvingDivide(var, q):
    if isInside(var, left(left(q))):
        x = (left(left(q)), "=", (right(q), "*", right(left(q))))
        return solving(var,x)  # A=C/B
    elif isInside(var, right(left(q))):
        x2 = (right(left(q)), "=", (left(left(q)), "/", right(q)))
        return solving(var,x2) # B=A/C

