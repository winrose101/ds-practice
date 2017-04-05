Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> shopping_list = []
>>> shopping_list
[]
>>> shopping_list.append("milk")
>>> shopping_list.append("eggs")
>>> shopping_list.append("spam")
>>> shopping_list
['milk', 'eggs', 'spam']
>>> shopping_list.append(4)
>>> shopping_list
['milk', 'eggs', 'spam', 4]
>>> shopping_list.append(True)
>>> shopping_list
['milk', 'eggs', 'spam', 4, True]
>>> shopping_list = ["milk", "eggs", "spam"]
>>> shoping_list
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    shoping_list
NameError: name 'shoping_list' is not defined
>>> shopping_list
['milk', 'eggs', 'spam']
>>> shopping_list.remove("eggs")
>>> shopping_list
['milk', 'spam']
>>> shopping_list.append("bread")
>>> shopping_list.append("cheese")
>>> shopping_list
['milk', 'spam', 'bread', 'cheese']
>>> for item in shopping_list:
	print (item)

	
milk
spam
bread
cheese
>>> shopping_list
['milk', 'spam', 'bread', 'cheese']
>>> if "milk" in shopping_list:
	print ("Yum!")

	
Yum!
>>> if "eggs" not in shopping_list:
	print ("No!!!")

	
No!!!
>>> if "eggs" not in shopping_list:
	print ("Yawa!")
	shopping_list.append("eggs")

	
Yawa!
>>> shooping_list
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    shooping_list
NameError: name 'shooping_list' is not defined
>>> shopping_list
['milk', 'spam', 'bread', 'cheese', 'eggs']
>>> 
