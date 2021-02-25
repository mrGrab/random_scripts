#!/usr/bin/env python3

import sys
import os

path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
file = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
for item in sorted(file, key=len):
	print ("%s: %s" % (len(item), item))
