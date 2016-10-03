n, k = [int(x) for x in raw_input().strip().split()]
platelist = []
for pnum in xrange(n):
    pi, di = [int(x) for x in raw_input().strip().split()]
    benefit = pi+di
    platelist.append((benefit, pi, di))
    
platelist.sort()
platelist.reverse()
total = 0
for plate in platelist[:k]:
    total += plate[1]
for plate in platelist[k:]:
    total -= plate[2]

print total
