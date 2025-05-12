for i in range(4): # enumerate elements in tuple
   print(i)                     # otherwise print the value

doubles = [x * 2 for x in range(4)]
print(doubles)                       # prints [0, 2, 4, 6]
upper = [c.upper() for c in 'Hello']
print(''.join(upper))                      # prints ['H', 'E', 'L', 'L', 'O']

def add(x,y):
    return x+y

print(add('Hello', 'World'))  # returns 'HelloWorld'
print(add([1, 2], [3, 4]))    # returns [1, 2, 3, 4]

print(add(4,50))
