#!/usr/bin/env python


from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 10000000
NODES = 100
NEW_NODES = 101
V_NODES = 1000

count = 0

ring =[]
new_ring = []
hash2node = {}


def _hash(val):
    return unpack_from("I", md5(str(val)).digest())[0]

for i in range(NODES):
    for j in range(V_NODES):
        h = _hash(str(i) + "0" + str(j))
        ring.append(h)
        hash2node[h] = i
ring.sort()

for i in range(NEW_NODES):
    for j in range(V_NODES):
        h = _hash(str(i) + "0" + str(j))
        new_ring.append(h)
        hash2node[h] = i
new_ring.sort()

for item in range(ITEMS):
    hased_item = _hash(item)
    node_num = bisect_left(ring, hased_item) % (NODES * V_NODES)
    new_node_num = bisect_left(new_ring, hased_item) % (NEW_NODES * V_NODES)
    if hash2node[ring[node_num]] != hash2node[new_ring[new_node_num]]:
        count += 1

print "mismatch when add one node in 100 nodes: " + str(count) + " RATIO: " + str(count/(ITEMS * 1.0))