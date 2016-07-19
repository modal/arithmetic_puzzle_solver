from __future__ import division
import sys
from itertools import permutations, product
"""
Brute Force Solver for Blog Post
a simple but difficult arithmetic puzzle
http://blog.plover.com/math/17-puzzle.html
"""
##############################################################################
def add(x, y):
    """+"""
    return x + y

def sub(x, y):
    """-"""
    return x-y

def div(x, y):
    """/"""
    return x / y

def mul(x, y):
    """*"""
    return x * y
##############################################################################
def solver(seq=[2,5,6,6], ops=[add, sub, div, mul], target=17):
    cnt=0
    for x, y, w, z in permutations(seq):
        ops_pm = product(ops, repeat=3)
        for op1, op2, op3 in ops_pm:
            cnt+=1
            sol = op3(op2(op1(x, y), w), z)
            if sol == target:
                print sol, "=", x, op1.__doc__, y, op2.__doc__, w, op3.__doc__, z
    print "$$$$$$$$$$$$$$$$$$$$$", cnt

##############################################################################
#TEST CODE

#a = permutations(seq)
#ops_pm = product(ops, repeat=3)

#for x in ops_pm:
#    print x[0].__doc__, x[1].__doc__, x[2].__doc__

#for x in a:
#    print x

#cnt=0
#for val in a:
#    #print ">>> ", val
#    for x in ops:
#        for y in ops:
#            for w in ops:
#                cnt+=1
#                sol = w(y(x(val[0], val[1]), val[2]), val[3])
#                if sol == 17:
#                    print sol, "=",
#                    print val[0], x.__doc__,
#                    print val[1], y.__doc__,
#                    print val[2], w.__doc__,
#                    print val[3]
#print "^^^^^^^^^^^^^^^^^^^^^", cnt
##############################################################################
if __name__ == "__main__":
    seq = [2, 5, 6, 6]
    ops = [add, sub, div, mul]
    solver(seq, ops)
