Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = ['a', 'b', 123]
>>> l
['a', 'b', 123]
>>> l[0]
'a'
>>> l[10]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l[10]
IndexError: list index out of range
>>> l =['a', 'b', 123]
>>> l[:]
['a', 'b', 123]
>>> new_l = l[1:]
>>> new_l
['b', 123]
>>> l
['a', 'b', 123]
>>> l = ['a', 'b', 123]
>>> l.append('c')
>>> print (l)
['a', 'b', 123, 'c']
>>> l
['a', 'b', 123, 'c']
>>> l.append(124)
>>> print (l)
['a', 'b', 123, 'c', 124]
>>> l.insert(4, 'd')
>>> print (L)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (L)
NameError: name 'L' is not defined
>>> print (l)
['a', 'b', 123, 'c', 'd', 124]
>>> l
['a', 'b', 123, 'c', 'd', 124]
>>> l.insert(-, 'e')
SyntaxError: invalid syntax
>>> l.insert(-1, 'e')
>>> l
['a', 'b', 123, 'c', 'd', 'e', 124]
>>> print l
SyntaxError: Missing parentheses in call to 'print'
>>> print ('l')
l
>>> print (l)
['a', 'b', 123, 'c', 'd', 'e', 124]
>>> l
['a', 'b', 123, 'c', 'd', 'e', 124]
>>> l.insert(-1, 111)
>>> l
['a', 'b', 123, 'c', 'd', 'e', 111, 124]
>>> l.remove(-1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l.remove(-1)
ValueError: list.remove(x): x not in list
>>> l.remove(111)
>>> l
['a', 'b', 123, 'c', 'd', 'e', 124]
>>> #comment
>>> #retrieving and looking up elements
>>> last_element = l.pop()
>>> 
>>> l
['a', 'b', 123, 'c', 'd', 'e']
>>> last_element = l.pop()
>>> l
['a', 'b', 123, 'c', 'd']
>>> last_element
'e'
>>> last_element
'e'
>>> l
['a', 'b', 123, 'c', 'd']
>>> last_element = l.pop()
>>> last_element
'd'
>>> l
['a', 'b', 123, 'c']
>>> third_element = l.pop(2)
>>> third_element
123
>>> l
['a', 'b', 'c']
>>> #returns the third element, modifying the list ie removing the third element
>>> l.index(0)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    l.index(0)
ValueError: 0 is not in list
>>> l.index('c')
2
>>> l.index('a')
0
>>> l.index('b')
1
>>> l
['a', 'b', 'c']
>>> l.append('d')
>>> l.append('e')
>>> print(l)
['a', 'b', 'c', 'd', 'e']
>>> l.append('a')
>>> l.append('b')
>>> l.append('c')
>>> l.insert(0, 'b')
>>> l
['b', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c']
>>> l.count('a')
2
>>> l.count('b')
3
>>> l.extend(['a', 'b'])
>>> l
['b', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'a', 'b']
>>> l.sort()
>>> l
['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'd', 'e']
>>> l.revere()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l.revere()
AttributeError: 'list' object has no attribute 'revere'
>>> l.reverse()
>>> l
['e', 'd', 'c', 'c', 'b', 'b', 'b', 'b', 'a', 'a', 'a']
>>> #list comprehensions
>>> """list comprehensions"""
'list comprehensions'
>>> """a"""
'a'
>>> #so hashtag is to comment and triple quoatation is to print in python 3
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print('a')
a
>>> #baadaye, on to list comprehensions
>>> l = [1, 2, 3]
>>> l
[1, 2, 3]
>>> new_l = [x*2 for x in l]
>>> new_l
[2, 4, 6]
>>> newest_l =[x**2 for x in l]
>>> newest_l
[1, 4, 9]
>>> even_newer_l = [x**2 in new_l]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    even_newer_l = [x**2 in new_l]
NameError: name 'x' is not defined
>>> even_newer_l = [x**2 for x in new_l]
>>> new_l
[2, 4, 6]
>>> even_newer_l
[4, 16, 36]
>>> import math
>>> sqrt(16)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    sqrt(16)
NameError: name 'sqrt' is not defined
>>> import math*
SyntaxError: invalid syntax
>>> from math import sqrt
>>> sqrt(16)
4.0
>>> better_l = [sqrt(x) for x in even_newer_l)
SyntaxError: invalid syntax
>>> better_l = [sqrt(x) for x in even_newer_l]
>>> even_newer_l
[4, 16, 36]
>>> better_l
[2.0, 4.0, 6.0]
>>> ~#why is it sqrting to float data types instead of integers?
SyntaxError: invalid syntax
>>> #a question mark is invalid syntax?
>>> #apparently not, maybe if it comes after integers?
>>> #still not
>>> #anywho
>>> #SETS
>>> L =[1, 2, 3]
>>> L
[1, 2, 3]
>>> l
[1, 2, 3]
>>> #not case sensitive I see
>>> s = set(l)
>>> s
{1, 2, 3}
>>> l = [1, 2, 3]
>>> l
[1, 2, 3]
>>> s = set(l)
>>> s
{1, 2, 3}
>>> {1, 2, 3}
{1, 2, 3}
>>> # does not match the cose.tutsplus.com tutorial
>>> # inafaa kuwa set([1, 2, 3])
>>> #code not cose
>>> #you cannot go back and edit comments
>>> s ={1, 2, 3}
>>> s
{1, 2, 3}
>>> l = [1, 2, 3]
>>> s = set(l)
>>> 
>>> s
{1, 2, 3}
>>> l =[1, 2, 3, 3]
>>> s = set(l)
>>> s
{1, 2, 3}
>>> #eliminates duplicate values
>>> set([1, [1,2]])
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    set([1, [1,2]])
TypeError: unhashable type: 'list'
>>> #all elements in a set must be hashable
>>> set1 = set([1, 2, 3])
>>> set2 = set([3, 4, 5])
>>> set1
{1, 2, 3}
>>> set2
{3, 4, 5}
>>> set1 | set2
{1, 2, 3, 4, 5}
>>> #dupliicate 3 eliminated
>>> #contd in the union
>>> set1 & set2
{3}
>>> #the above is intersection
>>> set1 - set2
{1, 2}
>>> #difference hii inamaanisha?
>>> set2 - set1
{4, 5}
>>> # what is in the first set that is not in the second set?set1
>>> set1 ^ set2 #symmetric difference
{1, 2, 4, 5}
>>> #set comprehensions
>>> vowels = ['a', 'e', 'i', 'o', 'u']
>>> vowels
['a', 'e', 'i', 'o', 'u']
>>> {x for x in 'maintenance' if x not in vowels}
{'m', 'c', 't', 'n'}
>>> set(['m', 'c', 't', 'n'])
{'m', 'c', 'n', 't'}
>>> frozen = frozenset([1, 2, 2])
>>> frozen
frozenset({1, 2})
>>> #eliminates duplicate vaules, the ([]) creates a set?
>>> frozen = frozenset([1, 2, 3])
>>> frozen
frozenset({1, 2, 3})
>>> #nope, not the curved and squared brackets but the set in frozenset
>>> #hizo zingine zinaitwa curly brackets 
