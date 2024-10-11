list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2) # is [('a', 1), ('b', 2), ('c', 3)]


pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)


zip(('a', 1), ('b', 2), ('c', 3))  # returns [('a','b','c'), ('1','2','3')]


def add(a, b): return a + b
add(1, 2) # returns 3
add([1, 2]) # TypeError!
add(*[1, 2]) # returns 3

