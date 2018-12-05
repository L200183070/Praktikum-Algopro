##kegiatan 1

file = open('L200183070.txt','w')
file.write('L200183070' +' \n')
file.write('08-09-1999' + '\n')
file.write('Aulia Septianingrum Revyana Nurcahyani'+'\n')
file.close()

##kegiatan 2
file = open('L200183070.txt','w')
file.write('L200183070' +' \n')
file.write('08-09-1999' + '\n')
file.write('Aulia Septianingrum Revyana Nurcahyani'+'\n')
file.close()

data = open('L200183070.txt','r')
NIM = data.readline()
TTL = data.readline()
NAME = data.readline()
data.close()

import shelve
data = shelve.open('Aulia')
data['Data1'] = [NIM,TTL,NAME]
data.close()

data =shelve.open('Aulia')
print(data['Data'][0])
print(data['Data'][1])
print(data['Data'][2])

##kegiatan 3

import shelve
data = open('L200183070.txt','r')
NIM = data.readline()
TTL = data.readline()
NAME = data.readline()
data.close()

data =shelve.open('Aulia')
print(data['Data'][0])
print(data['Data'][1])
print(data['Data'][2])

