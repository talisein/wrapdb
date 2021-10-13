#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as infile, open(sys.argv[2], 'w') as outfile:
    outfile.write('{ global:\n')
    for l in infile.read().splitlines():
        outfile.write('{};\n'.format(l))
    outfile.write('local: *; };\n')
