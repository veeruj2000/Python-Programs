Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # list of numbers
>>> list1 = [12, -7, 5, 64, -14]
>>> 
>>> for num in list1:
	if num>=0:
		print(num, end = " ")

	
12 5 64 
>>> # list 2 of numbers
>>> list 2 = [12,14,-95,3]
SyntaxError: invalid syntax
>>> list2 = [12, 14, -95, 3]
>>> for num in list2:
	if num>=0:
		print(num, end = " ")

		
12 14 3 
>>> 
