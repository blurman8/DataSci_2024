import re
my_regex = re.compile("[0-9]+", re.I)

import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

import matplotlib.pyplot as plt

#explicitly and use them without qualification
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

match = 10
from re import * # uh oh, re has a match function
print (match) # "<function re.match>"