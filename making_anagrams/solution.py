DEBUG = True

def number_needed(a, b):
    changecnt = 0
    alist = list(a)
    blist = list(b)
    alist.sort()
    blist.sort()
    if DEBUG: print "Orig:"
    if DEBUG: print alist
    if DEBUG: print blist
    while True:
        if len(alist) == 0:
            changecnt += len(blist)
            break
        if len(blist) == 0:
            changecnt += len(alist)
            break

        if DEBUG: print "changes: ", changecnt
        if DEBUG: print "-"*30
        if DEBUG: print "achar/bchar: ", alist[-1], " ", blist[-1]
        if DEBUG: print "alist: ", alist
        if DEBUG: print "blist: ", blist

        if alist[-1] == blist[-1]:
            alist.pop()
            blist.pop()
            continue
            
        changecnt += 1

        if alist[-1] > blist[-1]:
            alist.pop()
        elif blist[-1] > alist[-1]:
            blist.pop()
            
    return changecnt

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

