# not Pythonic
for i in range(len(documents)):
    document = documents[i]
    do_something(i, document)
# also not Pythonic
i = 0
for document in documents:
    do_something(i, document)
    i += 1
 
for i, document in enumerate(documents):
    do_something(i, document)
 
for i in range(len(documents)): do_something(i) # not Pythonic
for i, _ in enumerate(documents): do_something(i) # Pythonic

