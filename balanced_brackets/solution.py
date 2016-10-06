def is_matched(expression):
    openlist = ["(","[","{"]
    charstack = []
    for char in list(expression):
        if char in openlist:
            charstack.append(char)
            continue
        if char not in openlist and len(charstack) == 0:
                return False
        if char == ")":
            if charstack[-1] != "(":
                return False
            charstack.pop()
        elif char == "]":
            if charstack[-1] != "[":
                return False
            charstack.pop()
        elif char == "}":
            if charstack[-1] != "{":
                return False
            charstack.pop()
    return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
