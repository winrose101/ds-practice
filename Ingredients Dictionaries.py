Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("Hello World!")
Hello World!
>>> foods ={}
>>> foods["banana"] = "A delicious and tasty treat!"
>>> foods["dirt"] = "Not delicious. Not tasty. DO NOT EAT!"
>>> foods
{'banana': 'A delicious and tasty treat!', 'dirt': 'Not delicious. Not tasty. DO NOT EAT!'}
>>> foods["banana"]
'A delicious and tasty treat!'
>>> foods["dirt"]
'Not delicious. Not tasty. DO NOT EAT!'
>>> foods["cheese"]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    foods["cheese"]
KeyError: 'cheese'
>>> if "cheese" in foods:
	print ("Cheese is one of the known foods!")

	
>>> if "cheese" in foods:
	print ("Cheese is one of the known foods!")

	
>>> if "cheese" in foods:
	print ("Yaay!")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if "cheese" in foods:
	print ("yay")
	else:
		
SyntaxError: invalid syntax
>>> if "cheese" in foods:
	print ("yay")
	print (foods["cheese"])

	
>>> 
>>> if "cheese" not in foods:
	print ("no!")
	print (foods["cheese"])

	
no!
Traceback (most recent call last):
  File "<pyshell#29>", line 3, in <module>
    print (foods["cheese"])
KeyError: 'cheese'
>>> foods [cheese"] = "eggs and spam"
       
SyntaxError: invalid syntax
>>> foods ["cheese"] = "eggs and spam"
>>> foods
{'banana': 'A delicious and tasty treat!', 'dirt': 'Not delicious. Not tasty. DO NOT EAT!', 'cheese': 'eggs and spam'}
>>> if "cheese" in foods:
	print "yay"
	
SyntaxError: Missing parentheses in call to 'print'
>>> if "cheese" in foods:
	print (yay)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 2, in <module>
    print (yay)
NameError: name 'yay' is not defined
>>> if "cheese" in foods:
	print ("yay")

	
yay
>>> foods
{'banana': 'A delicious and tasty treat!', 'dirt': 'Not delicious. Not tasty. DO NOT EAT!', 'cheese': 'eggs and spam'}
>>> del foods["dirt"]
>>> foods
{'banana': 'A delicious and tasty treat!', 'cheese': 'eggs and spam'}
>>> ingredients = {}
>>> ingredients["blt sandwich"] = ["bread", "lettuce", "tomato", "bacon"]
>>> ingredients["blt sandwich"]
['bread', 'lettuce', 'tomato', 'bacon']
>>> del ingredients["bread"]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    del ingredients["bread"]
KeyError: 'bread'
>>> ingredients
{'blt sandwich': ['bread', 'lettuce', 'tomato', 'bacon']}
>>> ingredients["tea"] = ["milk", "water", "sugar", "majani"]
>>> ingredients
{'blt sandwich': ['bread', 'lettuce', 'tomato', 'bacon'], 'tea': ['milk', 'water', 'sugar', 'majani']}
>>> del ingredients["blt sandwich"]
>>> ingredients
{'tea': ['milk', 'water', 'sugar', 'majani']}
>>> ingredients["tea"].remove("majani")
>>> ingredients
{'tea': ['milk', 'water', 'sugar']}
>>> ingredients["tea"].append("masala")
>>> ingredients
{'tea': ['milk', 'water', 'sugar', 'masala']}
>>> ingredients["tea"].append(2, "cocoa")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ingredients["tea"].append(2, "cocoa")
TypeError: append() takes exactly one argument (2 given)
>>> europe = []
>>> germany = {"name": "Germany", "population": 8100}
>>> europe.append(germany)
>>> europe
[{'name': 'Germany', 'population': 8100}]
>>> luxembourg = {"name": "Lux", "pop": 5100}
>>> europe.append("luxembourg")
>>> europe
[{'name': 'Germany', 'population': 8100}, 'luxembourg']
>>> europe.remove("luxembourg")
>>> europe
[{'name': 'Germany', 'population': 8100}]
>>> lux = {"name": "lux", "pop": 5100}
>>> europe.append(lux)
>>> europe
[{'name': 'Germany', 'population': 8100}, {'name': 'lux', 'pop': 5100}]
>>> 
