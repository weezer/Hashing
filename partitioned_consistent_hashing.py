#!/usr/bin/env python


from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 10000000
NODES = 100

PARTITION_POWER = 12

node_stats = [0 for i in range(NODES)]
ring = []
part2node = {}


def _hash(val):
    return unpack_from("I", md5(str(val)).digest())[0]

for part in