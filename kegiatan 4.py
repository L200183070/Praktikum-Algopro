Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama='Aulia Septianingrum Revyana Nurcahyani'
>>> NIM=1070
>>> Tinggi= 1.25
>>> Berat= 55
>>> TahunLahir= 1999
>>> Aku =(TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'> #Because tuples are sequences and cannot be changed
>>> Aku[0]
1999 #because [0] is the first index tuple element
>>> a = NIM %4; Aku[a]
1.25 #because nim is asummed in variabel , divided by 4 and the result is class float
>>> type(Aku[a])
<class 'float'> #because the number of a is class float
>>> Aku[a:4]
(1.25, 1070) #because will display a end before index 4th, a is 1.25 and and before the 5th index is nim or 1070
>>> type(Aku[4])
<class 'str'> #because element 4th in tuple is nama, and nama is character
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
## because the type is tuple
>>> type(Data)
<class 'list'> #because data can be changed
>>> type(Data[4])
<class 'str'> #because element 4 is Nama and nama is character
>>> Data[4][5]
' '#because in data data 5 and 6 do not exist
>>> Data[4][a:6]
'lia ' #because the 4th index of data is nama, and the between a and 6 is lia
>>> Data[0] = 'ok' ; Data
['ok', 55, 1.25, 1070, 'Aulia Septianingrum Revyana Nurcahyani']
#because the data wants to replace the birth date is an ok word
>>> Data[-a]
1070 #because if you count from behind it is minus and -a is 1070
>>> range(a)
range(0, 2)
>>> #because giving range from 0 until 2 
