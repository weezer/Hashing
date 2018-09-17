#!/usr/bin/env python

from hashlib import md5
from struct import unpack_from

ITEMS = 10000000
NODES = 100

node_stats = [0 for _ in range(NODES)]

for item in range(ITEMS):
    hashed_item = unpack_from("I", md5(str(item)).digest())[0]
    node_num = hashed_item % NODES
    node_stats[node_num] += 1

_average = ITEMS // NODES
_max = max(node_stats)
_min = min(node_stats)

print "Average: " + str(_average)
print "Max: " + str(_max)
print "Min: " + str(_min)
