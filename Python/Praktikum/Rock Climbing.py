Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'aku'<'Aku'
False
>>> 'aku'=='Aku'
False
>>> 'aku'>'Aku'
True
>>> 
>>> s='rock'
>>> t='climbing'
>>> s>t
True
>>> s<t
False
>>> 'o'in s
True
>>> 'o'in t
False
>>> 5*s
'rockrockrockrockrock'
>>> 5*t
'climbingclimbingclimbingclimbingclimbing'
>>> s+t
'rockclimbing'
>>> t+s
'climbingrock'
>>> ' 'in s
False
>>> ' 'not in s
True
>>> 
>>> len(s+t)
12
