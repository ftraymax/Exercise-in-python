Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> totalSize = 0
>>> import os
>>> import pathlib as Path
>>> for filename in os.listdir('C:\\Windows\\System32'):
	totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32',filename))

	
>>> print(totalSize)
2027732014
>>> p = Path('C:/Users/ram/Desktop')
>>> p.glob('*')
<generator object Path.glob at 0x000001A6F9BDB7B0>
>>> list(p.glob('*'))
[]
>>> list(p.glob('*.txt'))
[]
>>> winDir = Path('C:/Windows')
>>> notexistsdir = Path('C:/This/Folder/does/not/exists')
>>> calFile = Path('C:/Windows/System32/calc.exe')
>>> winDir.exists()
True
>>> winDir.is_dir()
True
>>> notexistsdir.exists()
False
>>> calFile.is_file()
True
>>> calFile.is_dir()
False
>>> p = Path('spam.txt')
>>> p.write_text('Hello, world!')
13
>>> p.read_text()
'Hello, world!'
