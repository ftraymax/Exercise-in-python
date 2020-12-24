Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pathlib import Path
>>> Path('spam','bacon','eggs')
WindowsPath('spam/bacon/eggs')
>>> 'c:\\spam\\eggs.png'
'c:\\spam\\eggs.png'
>>> '//'.join(['folder1', 'folder 2', 'folder 3', 'file.png'])
'folder1//folder 2//folder 3//file.png'
>>> import os
>>> os.path.join('folder1', 'folder 2', 'folder 3', 'file.png')
'folder1\\folder 2\\folder 3\\file.png'
>>> os.sep
'\\'
>>> os.getcwd()
'C:\\Users\\senth\\AppData\\Local\\Programs\\Python\\Python39'
>>> from pathlib import Path
>>> myfiles = ['account.txt','detail.csv','invite.docx']
>>> for filename in myfiles:
	print(Path(r'C:\Users\senth',filename))

	
C:\Users\senth\account.txt
C:\Users\senth\detail.csv
C:\Users\senth\invite.docx
>>> os.getcwd()
'C:\\Users\\senth\\AppData\\Local\\Programs\\Python\\Python39'
>>> os.chdir('c:\\')
>>> os.getcwd()
'c:\\'
>>> Path('spam')/'eggs'/'ham'
WindowsPath('spam/eggs/ham')
>>> Path('spam')/Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')
>>> Path'spam'/'eggs'/'ham'
SyntaxError: invalid syntax
>>> Path('cheese')/Path('bread','eggs')
WindowsPath('cheese/bread/eggs')
>>> homefolder = r'C:\Users\ram'
>>> subfolder = 'hello'
>>> homefolder+ '\\' +subfolder
'C:\\Users\\ram\\hello'
>>> '\\'.join([homefolder, subfolder])
'C:\\Users\\ram\\hello'
>>> homefolder = Path('C:\\users\ram')
>>> subfolder = ('spam')
>>> subfolder = Path('spam')
>>> homefolder / subfolder
WindowsPath('C:/users\ram/spam')
>>> str(homefolder/subfolder)
'C:\\users\ram\\spam'
>>> Path.home()
WindowsPath('C:/Users/senth')
>>> os.makedirs('C:\\user\\senth\\homie')
>>> path.cwd()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    path.cwd()
NameError: name 'path' is not defined
>>> Path.cwd()
WindowsPath('c:/')
>>> Path.cwd().is_absolute()
True
>>> Path('spam/bacon/egg').is_absolute()
False
>>> Path('my/relative/path')
WindowsPath('my/relative/path')
>>> Path.cwd()/Path('my/relative/path')
WindowsPath('c:/my/relative/path')
>>> Path.home()/Path('my/relative/path')
WindowsPath('C:/Users/senth/my/relative/path')
>>> os.path.abspath('.')
'c:\\'
>>> os.path.abspath('.\\Scripts')
'c:\\Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True
>>> os.path.relpath('C:\\Windows','C:\\')
'Windows'
>>> os.path.relpath('C:\\Windows','C:\\spam\\ham')
'..\\..\\Windows'
>>> p = Path('C:/Users/ram/scyther.txt')
>>> p.anchor
'C:\\'
>>> p.stem
'scyther'
>>> p.name
'scyther.txt'
>>> p.suffix
'.txt'
>>> p.drive
'C:'
>>> p.parent
WindowsPath('C:/Users/ram')
>>> Path.cwd()
WindowsPath('c:/')
