Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> empty-tuple = ()
SyntaxError: can't assign to operator
>>> empty_tuple = ()
>>> empty_tuple
()
>>> one_elem_tuple = 'a',
>>> one_elem_tuple
('a',)
>>> one_elem_tuple = ('a',)
>>> one_elem_tuple
('a',)
>>> s = 'a', 'b', [1, 2, 3]
>>> s
('a', 'b', [1, 2, 3])
>>> # I don't get tuples
>>> #tuples are great performance wise because of their immatability. python will know exactly how much memory to allocate for the data to be stored
>>> # DICTS
>>> vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> vowels
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> {x:x*x for x in (1, 2, 3)}
{1: 1, 2: 4, 3: 9}
>>> # the above is creating dictionaries by comprehensions
>>> dict([(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')])
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> dict(a=1, e=2, i=3, o=4, u=5)
{'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
>>> # the above is if the keys are strings
>>> # but will not work if the keys are numeric
>>> dict([1=a, 2=e, 3=i, 4=o, 5=u])
SyntaxError: invalid syntax
>>> dict(1=a, 2=e, 3=i, 4=o, 5=u)
SyntaxError: keyword can't be an expression
>>> vowels = {1: 'a', 2: 'e', 3:'i', 4:'o', 5: 'u'}
>>> vowels
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> vowels[1]
'a'
>>> vowels[10]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    vowels[10]
KeyError: 10
>>> #because key 10 does not exist in the dictionary
>>> vowels
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> del(vowels[1])
>>> vowels
{2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> del(vowels[10])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    del(vowels[10])
KeyError: 10
>>> keys()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    keys()
NameError: name 'keys' is not defined
>>> # keys() values() iteritems() itervalues() has_key()
>>> #the above are some of the useful built in methods supported by dicts
>>> vowels
{2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> #how to add to a dict?
>>> vowels
{2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> vowels.keys()
dict_keys([2, 3, 4, 5])
>>> vowels.values()
dict_values(['e', 'i', 'o', 'u'])
>>> vowels.iteritems()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    vowels.iteritems()
AttributeError: 'dict' object has no attribute 'iteritems'
>>> for k, v in vowels.iteritems()
SyntaxError: invalid syntax
>>> vowels
{2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> for k, v in vowels.iteritmes()
SyntaxError: invalid syntax
>>> #not as in the tut
>>> #PROBLEM
>>> for v in vowels.itervalues()
SyntaxError: invalid syntax
>>> #not like in tut
>>> #mondoproblemo
>>> 
