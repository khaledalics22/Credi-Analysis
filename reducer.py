#!/home/khalid/miniconda3/bin/python

import sys

weights = {}
count = 0
for line in sys.stdin:
    count += 1
    wi, val = line.strip().split('\t', 1)
    try:
        weights[wi] += float(val)
    except:
        weights[wi] = float(val)

for w, val in weights.items():
    print(f'{w}\t{val/count}')
