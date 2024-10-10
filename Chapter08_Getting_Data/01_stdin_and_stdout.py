# egrep.py
import sys, re
# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys.argv[1]
# for every line passed into the script
for line in sys.stdin:
    # if it matches the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)


# line_count.py
import sys
count = 0
for line in sys.stdin:
    count += 1
# print goes to sys.stdout
print (coun)


#>type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
 
#>cat SomeFile.txt | python egrep.py "[0-9]" | python line_count.py


# most_common_words.py
import sys
from collections import Counter
# pass in number of words as first argument
try:
    num_words = int(sys.argv[1])
except:
    print ("usage: most_common_words.py num_words")
    sys.exit(1) # non-zero exit code indicates error
    
counter = Counter(word.lower() # lowercase words
                for line in sys.stdin #
                for word in line.strip().split() # split on spaces
                if word) # skip empty 'words'
for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")


#>type the_bible.txt | python most_common_words.py 10

