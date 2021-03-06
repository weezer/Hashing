#!/usr/bin/env python

from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 10000000
NODES = 100

node_stats = [0 for _ in range(NODES)]


def _hash(val):
    return unpack_from("I", md5(str(val)).digest())[0]

ring = []
hash2node = {}

for i in range(NODES):
    h = _hash(i)
    ring.append(h)
    hash2node[h] = i

ring.sort()

for item in range(ITEMS):
    h = _hash(item)
    n = bisect_left(ring, h) % NODES
    node_stats[hash2node[ring[n]]] += 1

_average = ITEMS // NODES
_max = max(node_stats)
_min = min(node_stats)

print "Average: " + str(_average)
print "Max: " + str(_max)
print "Min: " + str(_min)