#!/usr/bin/env python


from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 10000000
NODES = 100
NEW_NODES = 101

count = 0

ring =[]
new_ring = []


def _hash(val):
    return unpack_from("I", md5(str(val)).digest())[0]

for i in range(NODES):
    ring.append(_hash(i))
ring.sort()

for i in range(NEW_NODES):
    new_ring.append(_hash(i))
new_ring.sort()

for item in range(ITEMS):
    hased_item = _hash(item)
    node_num = ring[bisect_left(ring, hased_item) % NODES]
    new_node_num = new_ring[bisect_left(new_ring, hased_item) % NEW_NODES]
    if node_num != new_node_num:
        count += 1

print "mismatch when add one node in 100 nodes: " + str(count) + " RATIO: " + str(count/(ITEMS * 1.0))