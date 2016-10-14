# coding: utf-8
from perfect_hash import PerfectHash


elements = [2, 4, 5, 15, 18, 30]
p = 31

ph = PerfectHash()
ph.make(elements, p)
for q in range(1, p):
    if (ph.membership(q, p)):
        print("{0} is member.".format(q))
