one_is_less_than_two = 1 < 2 # equals True
true_equals_false = True == False # equals False


print (x) == None # prints True, but is not Pythonic
print (x) is None # prints True, and is Pythonic


s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""


first_char = s and s[0]
safe_x = x or 0


all([True, 1, { 3 }]) # True
all([True, 1, {}]) # False, {} is falsy
any([True, 1, {}]) # True, True is truthy
all([]) # True, no falsy elements in the list
any([]) # False, no truthy elements in the list


