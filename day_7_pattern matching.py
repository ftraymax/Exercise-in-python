Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> phoneNumRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('the phone number is 123-456-7890')
>>> print('phonenumber found' + mo.group())
phonenumber found123-456-7890
>>> phoneNumRegex =re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('my number is 213-789-3456')
>>> mo.group()
'213-789-3456'
>>> mo.group(1)
'213'
>>> mo.group(2)
'789-3456'
>>> first, second = mo.groups()
>>> print(first)
213
>>> print(second)
789-3456
>>> Regex = re.compile(r'Batman|cat women')
>>> mo1 = Regex.search('Bataman and cat women')
>>> mo1.group()
'cat women'
>>> mo2 = Regex.search('Batman and Catwomen')
>>> mo2.group()
'Batman'
>>> regex = re.compile(r'bat(man|mobile|copter)')
>>> mo = regex.search('batcopter is malfunctioing')
>>> mo.group()
'batcopter'
>>> mo.group(1)
'copter'
>>> mo = regex.search('batcopter is malfunctioing')
>>> mo.group(1)
'copter'
>>> mo1 = regex.search('the adventures of batman')
>>> mo1.group()
'batman'
>>> batregex = re.compile(r'bat(wo)?man')
>>> mo1 = batregex.search('batman vs superman')
>>> mo1.group()
'batman'
>>> mo2 = batregex.search('batwoman vs catwoman')
>>> mo2.group()
'batwoman'
>>> mo1 = phoneregex.search('my number is 123-456-7890')
>>> mo1.group()
'123-456-7890'
>>> mo2 = phoneregex.search('my number is 456-7895')
>>> mo2.group()
'456-7895'
>>> batregex = re.compile('bat(wo)*man')
>>> mo1 = batregex.search('batman vs superman')
>>> mo1.group()
'batman'
>>> mo2 = batregex.search('batwowowowowowoman vs cat wowowowowoman')
>>> mo2.group()
'batwowowowowowoman'
>>> batregex = re.compile('bat(wo)+man')
>>> mo1 = batregex.search('batman vs superman')
>>> mo1.group()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    mo1.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> Regex = re.compile(r'(Ha){3}')
>>> mo1 = Regex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'
>>> greedyRegex = re.compile(r'(ha){3,5}')
>>> mo1 = greedyRegex.search('HaHaHaHaHa')
>>> mo1.group()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    mo1.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo1 = greedyRegex.search('hahahahaha')
>>> mo1.group()
'hahahahaha'
>>> nongreedyRegex = re.compile(r'(ha){3,5}?')
>>> mo1 = nongreedyRegex.search('hahahahaha')
>>> mo1.group()
'hahaha'
>>> phoneRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
>>> mo = phoneRegex.search('Cell: 123-456-7890 Work: 212-345-7657')
>>> mo.group()
'123-456-7890'
>>> phoneRegex.findall('Cell: 123-456-7890 Work: 212-345-7657')
['123-456-7890', '212-345-7657']
>>> Regex = re.compile(r'[aeiouAEIOU]')
>>> Regex.findall('Baseball is overated,LIKE ANY OTHER Soerts')
['a', 'e', 'a', 'i', 'o', 'e', 'a', 'e', 'I', 'E', 'A', 'O', 'E', 'o', 'e']
>>> Regex = re.compile(r'\d+\s\w+')
>>> Regex.findall('12 drummers, 11 pipers, 10 landmines , 6 proximity , 2 catridge, 4 deadsilence, 6 kithab')
['12 drummers', '11 pipers', '10 landmines', '6 proximity', '2 catridge', '4 deadsilence', '6 kithab']
>>> Regex = re.compile(r'\d+\s\w')
>>> Regex.findall('12 drummers, 11 pipers, 10 landmines , 6 proximity , 2 catridge, 4 deadsilence, 6 kithab')
['12 d', '11 p', '10 l', '6 p', '2 c', '4 d', '6 k']
>>> Regex = re.compile(r'\d\s\w')
>>> Regex.findall('12 drummers, 11 pipers, 10 landmines , 6 proximity , 2 catridge, 4 deadsilence, 6 kithab')
['2 d', '1 p', '0 l', '6 p', '2 c', '4 d', '6 k']
>>> regex = re.compile(r'[^aeiouAEIOU]')
>>> regex.findall('Baseball is overated,LIKE ANY OTHER Sports')
['B', 's', 'b', 'l', 'l', ' ', 's', ' ', 'v', 'r', 't', 'd', ',', 'L', 'K', ' ', 'N', 'Y', ' ', 'T', 'H', 'R', ' ', 'S', 'p', 'r', 't', 's']
>>> hello = re.compile(r'^Hello')
>>> hello.search('Hello, world')
<re.Match object; span=(0, 5), match='Hello'>
>>> mo = hello.search('Hello, world')
>>> mo.group()
'Hello'
>>> whole.search('1231343232') == None
True
>>> whole = re.compile(r'^\d+$')
>>> whole.search('1223353435645645')
<re.Match object; span=(0, 16), match='1223353435645645'>
>>> regex = re.compile(r'.at')
>>> regex.findall('The cat in the hat sat on thr flat mat')
['cat', 'hat', 'sat', 'lat', 'mat']
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Dieago Last Name: Maradona')
>>> mo.group(1)
'Dieago'
>>> mo.group(2)
'Maradona'
>>> Regex = re.compile (r'<.*?>')
>>> mo = Regex.search('<To serve man> for dinner.')mo.group()
SyntaxError: invalid syntax
>>> mo = Regex.search('<To serve man> for dinner.')
>>> mo.group()
'<To serve man>'
>>> Regex = re.compile (r'<.*>')
>>> mo = Regex.search('<To serve man> for dinner.')
>>> mo.group()
'<To serve man>'
>>> 
