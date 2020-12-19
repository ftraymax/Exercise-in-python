Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
>>> cat['size']
'fat'
>>> 'cat has' + cat['color'] + 'fur'
'cat hasgrayfur'
>>> sam = {123:'luggage combination', 23:'password'}
>>> sam[123]
'luggage combination'
>>> sam =['cat','dog','moose']
>>> ram =['dog','cat','moose']
>>> sam == ram
False
>>> bread = {'name':'zoro','species':'cat','age':'8'}
>>> butter = {'species':'cat','age':'8','name':'zoro'}
>>> bread == butter
True
>>> bread = {'name':'zoro','species':'cat'}
>>> bread['looks']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    bread['looks']
KeyError: 'looks'
>>> sam = {'color':'red', 'age':23}
>>> for v in sam.values():
	print(v)

	
red
23
>>> sam = {'color':'red', 'age':23}
>>> for  k in sam.keys():
	print(k)

	
color
age
>>> sam = {'color':'red', 'age':23}
>>> for i in sam.items():
	print(i)

	
('color', 'red')
('age', 23)
>>> sam = {'color':'red', 'age':23}
>>> sam.keys()
dict_keys(['color', 'age'])
>>> list(sam.keys())
['color', 'age']
>>> sam = {'color':'red', 'age':23}
>>> list(sam.keys())
['color', 'age']
>>> sam = {'color':'red', 'age':23}
>>> for k,v in sam.items():
	print('key:' + k +  'Value:' +str(v))

	
key:colorValue:red
key:ageValue:23
>>> spam = {'name':'ram', 'age': 7}
>>> 'name' in spam.keys()
True
>>> 'ram' in spam.values()
True
>>> 'color' not in spam.keys()
True
>>> 'color' in spam
False
>>> 'ram' in spam
False
>>> 'name' in spam
True
>>> picnic = {'banana': 5, 'knife':2}
>>> 'i am bringing' +str(picnic.get('knife',0))+'knife'
'i am bringing2knife'
>>> 'i am bringing ' + str(picnic.get('rose',0))+'rose'
'i am bringing 0rose'
>>> 'i am bringing ' + str(picnic.get('house',1))+'house'
'i am bringing 1house'
>>> sam ={'name':'ram', 'age': 5}
>>> sam.setdefault('color','red')
'red'
>>> spam
{'name': 'ram', 'age': 7}
>>> sam
{'name': 'ram', 'age': 5, 'color': 'red'}
>>> sam.setdefault('color','white')
'red'
>>> sam
{'name': 'ram', 'age': 5, 'color': 'red'}
>>> 
