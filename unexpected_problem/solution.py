
s = raw_input().strip()
m = int(raw_input().strip())

answer = None
if len(set(list(s))) == 1:
        answer = m 
else:
    for tlen in xrange(2, len(s)/2):
        #print "tlen = %d" % tlen
        if (float(len(s)) / float(tlen) % 1) > 0:
            #print "tlen %d does not divide into %s" % (tlen, len(s))
            continue
        myset = set()
        lidx = 0
        while lidx < len(s)/2:
            ridx = lidx + tlen
            #print "lidx = %d to ridx = %d" % (lidx, ridx)
            substr = s[lidx:ridx]
            #print substr
            myset.add(substr)
            #print myset
            if len(myset) > 1:
            #    print "more than one... break"
                break
            lidx += tlen
        if len(myset) == 1:
            answer = m / tlen
            #print "cardinality of myset = 1. Solution found: %d" % answer
            #print myset
            break
    if answer is None:
        answer = m / len(s)

print answer % (10**9+7)
