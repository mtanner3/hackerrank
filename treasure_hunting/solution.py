
import math
def distance(x1,y1,x2,y2):
    a = x1-x2
    b = y1-y2
    return math.sqrt(a*a + b*b)

bx,by = map(float,raw_input().strip().split())
ax,ay = map(float,raw_input().strip().split())

intx = (by + (ax/ay)*bx) / (ay/ax + ax/ay)
inty = (ay/ax)*intx
#print "%f %f" % (intx, inty)

adist = distance(ax, ay, 0,0)#,ax,ay)
intdist1 = distance(intx, inty,0,0)#,intx,inty)
k = intdist1 / adist
print "%0.12f" % k

intdist2 = distance(bx, by, intx, inty)#, bx, by)

v = intdist2 / adist
print "%0.12f" % v
