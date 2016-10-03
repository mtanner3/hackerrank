
from collections import defaultdict

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
DEBUG = True

usize, numqueries = map(int, raw_input().strip().split())
U = []
for idx in xrange(usize):
    U.append(0)
for idx in xrange(numqueries):
    query = raw_input().strip()
    if DEBUG: print "=" * 5
    if DEBUG: print "initial U: ",U
    if DEBUG: print "query: ",query
    pieces = query.split()
    qtype = pieces[0]
    if qtype == "1":
        val = int(pieces[1])
        position_arr = list(pieces[2])
        posidx = 0
        for position in position_arr:
            if position == "1":
                U[posidx] = val
            posidx += 1
    elif qtype == "2":
        val = int(pieces[1])
        position_arr = list(pieces[2])
        posidx = 0
        for position in position_arr:
            if position == "1":
                U[posidx] = val ^ U[posidx]
            posidx += 1
    elif qtype == "3":
        position_arr = list(pieces[1])
        posidx = 0
        for position in position_arr:
            if position == "1":
                #sys.stdout.write("%s" % U[posidx])
                print U[posidx]
            posidx += 1
        #print ""
    if DEBUG: print "final U: ",U

