Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> sam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in sam
False
>>> 'howdy' not in sam
False
>>> 'cat' not in sam
True
>>> sam = ['cat', 'bat', 'rat', 'elephant']
>>> sam[1:3]
['bat', 'rat']
>>> sam[0:-2]
['cat', 'bat']
>>> sam[:2]
['cat', 'bat']
>>> sam[1:]
['bat', 'rat', 'elephant']
>>> sam[:4]
['cat', 'bat', 'rat', 'elephant']
>>> sam[3:]
['elephant']
>>> sam[:]
['cat', 'bat', 'rat', 'elephant']
>>> len(sam)
4
>>> sam + [amigo]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    sam + [amigo]
NameError: name 'amigo' is not defined
>>> sam.append('amigo')
>>> sam
['cat', 'bat', 'rat', 'elephant', 'amigo']
>>> sam1[1] = 'scyther'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sam1[1] = 'scyther'
NameError: name 'sam1' is not defined
>>> sam[1] = 'scyther'
>>> sam
['cat', 'scyther', 'rat', 'elephant', 'amigo']
>>> sam[3] = sam[1]
>>> sam
['cat', 'scyther', 'rat', 'scyther', 'amigo']
>>> sam[-1] = 786
>>> sam
['cat', 'scyther', 'rat', 'scyther', 786]
>>> [1,2,3] + ['a','b','c']
[1, 2, 3, 'a', 'b', 'c']
>>> [1,2,3] + [a,b,c]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    [1,2,3] + [a,b,c]
NameError: name 'a' is not defined
>>> sam = [1,2,3]
>>> sam = sam + ['a','b','c']
>>> sam
[1, 2, 3, 'a', 'b', 'c']
>>> sam * ['a','b','c']
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    sam * ['a','b','c']
TypeError: can't multiply sequence by non-int of type 'list'
>>> sam * 3
[1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c']
>>> sam
[1, 2, 3, 'a', 'b', 'c']
>>> sam = ['aaron', 'bob', 'catherine', 'duke']
>>> del sam[0]
>>> sam
['bob', 'catherine', 'duke']
>>> del sam[0:1]
>>> sam
['catherine', 'duke']
>>>  sam = ['aaron', 'bob', 'catherine', 'duke']
 
SyntaxError: unexpected indent
>>> sam = ['aaron', 'bob', 'catherine', 'duke']
>>> del sam[0:2]
>>> sam
['catherine', 'duke']
>>> 