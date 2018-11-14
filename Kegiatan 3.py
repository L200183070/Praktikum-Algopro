Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama ='Aulia Septianingrum Revyana Nurcahyani'
>>> NIM ='L200183070'
>>> X ='1' + NIM[7:0]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'> #because of the string being converted into an integer, the result is an integer
>>> type(b)
<class 'int'> #because of the string being converted into an integer, the result is an integer
>>> a/b
0.02631578947368421 #class float because the result is pecahan
>>> a//b
0  #class int because the result is integer
>>> 10 * (a-999)
-9980 #class int because the result is integer
>>> b ** 2
1444 ##class int because the result is integer
>>> a%b
1 #class int because a divived b the reselt is 1, 1 is integer
>>> c = 12.5
>>> type(c)
<class 'float'> #because the result number is decimal or comma
>>> a/c
0.08 #class float because the result number is decimal or comma
>>> a//c
0.0 #class float because the result number is decimal or comma
>>> a%c
1.0 #class float because the result number is decimal or comma
>>> c > b
False #claas bool and b is greater than c
>>> type(c>b)
<class 'bool'> #class bool because boolean is a data type that only has two values, true and false or 0 or 1
>>> a > b and b > c
False #class bool because a not greater than b and b not greater than c
>>> a > 1100 or b < 10
False #because a is 1 and b is 38 and according to logic it is False
