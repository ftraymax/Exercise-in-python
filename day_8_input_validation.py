Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> response = input('Enter a number:')
Enter a number:cat
>>> resonse
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    resonse
NameError: name 'resonse' is not defined
>>> response
'cat'
>>> import pyinputplus as pyip
>>> response = pyip.inputInt(prompt='enter a number:')
enter a number:cat
'cat' is not an integer.
enter a number:234
>>> response
234
>>> reponse = pyip.inputNum('enter num:', min=4)
enter num:3
Number must be at minimum 4.
enter num:sd
'sd' is not a number.
enter num:5
>>> response
234
>>> reponse
5
>>> response = pyip.inputNum('enter a number:, greaterThan=4)
			 
SyntaxError: EOL while scanning string literal
>>> response = pyip.inputNum('enter a number:', greaterThan=4)
enter a number:3
Number must be greater than 4.
enter a number:76
>>> response
76
>>> response =pyipinputNum(min=4,lessThan=6)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    response =pyipinputNum(min=4,lessThan=6)
NameError: name 'pyipinputNum' is not defined
>>> response =pyipinputNum('>'min=4,lessThan=6)
SyntaxError: invalid syntax
>>> response =pyipinputNum('>',min=4,lessThan=6)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    response =pyipinputNum('>',min=4,lessThan=6)
NameError: name 'pyipinputNum' is not defined
>>> response =pyip.inputNum(min=4,lessThan=6)

Blank values are not allowed.

Blank values are not allowed.
34
Number must be less than 6.
3
Number must be at minimum 4.
5
>>> response =pyip.inputNum('>',min=4,lessThan=6)
>45
Number must be less than 6.
>-1
Number must be at minimum 4.
>4
>>> response = pyip.inputNum(blank=True)

>>> response
''
>>> response = pyip.inputNum(limit=2)
hello
'hello' is not a number.
=-
'=-' is not a number.
Traceback (most recent call last):
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pysimplevalidate\__init__.py", line 512, in validateNum
    numericValue = int(value)
ValueError: invalid literal for int() with base 10: '=-'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pyinputplus\__init__.py", line 167, in _genericInput
    possibleNewUserInput = validationFunc(
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pyinputplus\__init__.py", line 385, in <lambda>
    validationFunc = lambda value: pysv.validateNum(
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pysimplevalidate\__init__.py", line 514, in validateNum
    _raiseValidationException(_("%r is not a number.") % (_errstr(value)), excMsg)
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pysimplevalidate\__init__.py", line 222, in _raiseValidationException
    raise ValidationException(str(standardExcMsg))
pysimplevalidate.ValidationException: '=-' is not a number.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    response = pyip.inputNum(limit=2)
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pyinputplus\__init__.py", line 398, in inputNum
    return _genericInput(
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pyinputplus\__init__.py", line 188, in _genericInput
    raise limitOrTimeoutException
pyinputplus.RetryLimitException
>>> response = pyip.inputNum(timeout=10)
23
>>> response = pyip.inputNum(timeout=3)
56
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    response = pyip.inputNum(timeout=3)
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pyinputplus\__init__.py", line 398, in inputNum
    return _genericInput(
  File "C:\Users\senth\AppData\Roaming\Python\Python39\site-packages\pyinputplus\__init__.py", line 203, in _genericInput
    raise TimeoutException()
pyinputplus.TimeoutException
>>> response = pyip.inputNum(limit=2, default='you have reached your limit')
sdfsdf
'sdfsdf' is not a number.
fghfgh
'fghfgh' is not a number.
>>> response
'you have reached your limit'
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])
XLII
>>> response
'XLII'
>>> xcvtjk
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    xcvtjk
NameError: name 'xcvtjk' is not defined
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])
asdasdasd
'asdasdasd' is not a number.
fghjhty
'fghjhty' is not a number.
XL
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])
zero
>>> response
'zero'
>>> rsponse = pyip.inputNum(blockRegexes=[r'[02468]$'])
84
This response is invalid.
88
This response is invalid.
90
This response is invalid.
55
>>> rsponse
55
>>> response
'zero'
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar','category'],blockRegexes=[r'cat'])
cat
This response is invalid.
catacomb
This response is invalid.
caterpillar
>>> response
'caterpillar'
>>> 