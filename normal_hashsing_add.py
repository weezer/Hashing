#!/usr/bin/env python

from hashlib import md5
from struct import unpack_from

ITEMS = 10000000
NODES = 100
NEW_NODES = 101

count = 0

for item in range(ITEMS):
    hased_item = unpack_from("I", md5(str(item)).digest())[0]
    node_num = hased_item % NODES
    new_node_num = hased_item % NEW_NODES
    if node_num != new_node_num:
        count += 1

print "mismatch when add one node in 100 nodes: " + str(count) + " RATIO: " + str(count/(ITEMS * 1.0))