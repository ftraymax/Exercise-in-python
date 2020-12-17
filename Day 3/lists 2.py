Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> people['ash', 'bob', 'catherine', 'leah']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    people['ash', 'bob', 'catherine', 'leah']
NameError: name 'people' is not defined
>>> people = ['ash', 'bob', 'catherine', 'leah']
>>> random.shuffle(people)
>>> people
['catherine', 'ash', 'bob', 'leah']
>>> random.shuffle(people)
>>> people
['catherine', 'leah', 'bob', 'ash']
>>> spam = 23
>>> spam+ = 1
SyntaxError: invalid syntax
>>> spam +=  1
>>> spam
24
>>> spam /= 2
>>> spam
12.0
>>> sam = 'hello'
>>> sam += 'world'
>>> sam
'helloworld'
>>> sam = ['ash']
>>> sam *= 2
>>> sam
['ash', 'ash']
>>> spam = ['ash', 'leah', 'scyther', 'oreo']
>>> spam.index('oreo')
3
>>> spam.index('kiki')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    spam.index('kiki')
ValueError: 'kiki' is not in list
>>> sam =['ash', 'leah', 'zelda', 'oreo', 'zelda']
>>> sam.index('zelda')
2
>>> 
KeyboardInterrupt
>>> sam =['ash', 'leah', 'zelda']
>>> sam.append('oreo')
>>> sam
['ash', 'leah', 'zelda', 'oreo']
>>> sam.remove('leah')
>>> sam
['ash', 'zelda', 'oreo']
>>> sam.insert(2, 'astro')
>>> sam
['ash', 'zelda', 'astro', 'oreo']
>>> sam['cat', 'dog' ,'cat', 'oreo']
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    sam['cat', 'dog' ,'cat', 'oreo']
TypeError: list indices must be integers or slices, not tuple
>>> sam = ['cat', 'dog' ,'cat', 'oreo']
>>> sam.remove('cat')
>>> sam
['dog', 'cat', 'oreo']
>>> sam = [2,-4,3.12,-234,0,65,345354]
>>> sam.sort()
>>> sam
[-234, -4, 0, 2, 3.12, 65, 345354]
>>> sam['ash', 'a
    
SyntaxError: EOL while scanning string literal
>>> sam['ash', 'leah', 'catherine', 'setsune']
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    sam['ash', 'leah', 'catherine', 'setsune']
TypeError: list indices must be integers or slices, not tuple
>>> sam = ['ash', 'leah', 'catherine', 'setsune']
>>> sam.sort(reverse=True)
>>> sam
['setsune', 'leah', 'catherine', 'ash']
>>> sam = ['ash', 'leah', 'catherine', 'setsune']
>>> sam.sort(reverse=False)
>>> sam
['ash', 'catherine', 'leah', 'setsune']
>>> sam = ['Ash', 'ash', 'Bob', 'Bijoy']
>>> sam.sort()
>>> sam
['Ash', 'Bijoy', 'Bob', 'ash']
>>> sam = ['a', 'z', 'A' ,'Z']
>>> sam.sort(key=str.lower)
>>> sam
['a', 'A', 'z', 'Z']
>>> sam = ['ash', 'leah', 'setsune']
>>> sam.reverse()
>>> sam
['setsune', 'leah', 'ash']
>>> name = 'Hathim'
>>> name[2]
't'
>>> name[-4]
't'
>>> name[1:5]
'athi'
>>> 'Ha' in name
True
>>> 'ha' in name
False
>>> 'h' not in name
False
>>> for i in name:
	print('---'+i+'---')

	
---H---
---a---
---t---
---h---
---i---
---m---

>>> name = 'oreo the dog'
>>> new = name[0:5] + 'a' + name[8:12]
>>> name
'oreo the dog'
>>> new
'oreo a dog'
>>> egg =[1,2,3]
>>> egg
[1, 2, 3]
>>> egg = [4,5,6]
>>> egg
[4, 5, 6]
>>> del egg[0]
>>> del egg[0]
>>> del egg[0]
>>> egg
[]
>>> egg.append(0)
>>> egg.append(2)
>>> egg.append(3)
>>> egg
[0, 2, 3]
>>> egg = ('hello, 23, 9)
       
SyntaxError: EOL while scanning string literal
>>> egg = ('hello', 23,9)
>>> egg[1]
23
>>> egg[0:2]
('hello', 23)
>>> len (egg)
3
>>> egg = ('hello', 23,9)
>>> egg[1] = 90
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    egg[1] = 90
TypeError: 'tuple' object does not support item assignment
>>> tuple(['Alice', 'sony', 23])
('Alice', 'sony', 23)
>>> list(('alice', 'bob', 23))
['alice', 'bob', 23]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> tuple['hello']
tuple['hello']
>>> spam =23
>>> spam = henry
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    spam = henry
NameError: name 'henry' is not defined
>>> sam = 23
>>> henry = sam
>>> sam =2323
>>> sam
2323
>>> henry
23
>>> sam = [0,1,2,3,4]
>>> cheese = sam
>>> cheese[0] = 'hola'
>>> sam
['hola', 1, 2, 3, 4]
>>> cheese
['hola', 1, 2, 3, 4]
>>> id('ram')
1284241683312
>>> id(23)
1284203965424
>>> sam ='hello'
>>> id(sam)
1284241683120
>>> sam += "world'
SyntaxError: EOL while scanning string literal
>>> sam += 'world'
>>> sam
'helloworld'
>>> id(sam)
1284241384560
>>> ram = ['cat', 'dog']
>>> id(ram)
1284241489408
>>> ram.append('sam')
>>> ram
['cat', 'dog', 'sam']
>>> id(ram)
1284241489408
>>> import copy
>>> spam = ['a' , 'b', 'c', 'd']
>>> id(spam)
1284240809344
>>> cheese = copy.copy(spam)
>>> id(cheese)
1284241777472
>>> cheese[1] = 23
>>> spam
['a', 'b', 'c', 'd']
>>> cheese
['a', 23, 'c', 'd']
>>> 