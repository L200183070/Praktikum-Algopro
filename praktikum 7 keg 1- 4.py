##Kegiatan 1

##D={'Segitiga' : 'L = 0.5 * a * t',
##   'Persegi' : 'L = s ** 2',
##   'PersegiPanjang' : 'L = p * l',
##   'Lingkaran' : 'L = pi * r ** 2',
##   'Jajarangenjang' : 'L = a * t'}
##
##print'''
##No  | Nama Bangun    | Rumus Luas
##----|----------------|------------
## 1  | Segitiga       | %s
## 2  | Persegi        | %s
## 3  | PersegiPannjang| %s
## 4  | Lingkaran      | %s
## 5  | Jajarangenjang | %s
##
##'''%(D['Segitiga'],D['Persegi'],D['PersegiPanjang'],
##     D['Lingkaran'],D['Jajarangenjang'])

##Kegiatan 2
##n = 2
##while n<3:
##    x = input('insert password')
##    if x == 'Aulia':
##        print 'Congratulation , you can log in'
##        break
##    elif x!='Aulia':
##        if n!= 0:
##            print 'sorry, you entered the wrong password.enter the password :'
##            n = n - 1
##        else:
##            print'You have tried 3 times. Your access is denied.'
##            break
   
##Kegiatan 3
        
Waktu =('Morning','Afternoon','Noon','Evening', 'Night')
x = input('Enter your name > ')
pukul = float(input("Now,what time is it?")
if pukul>= 01.00 and pukul<=10.00:
    print('Good', h[0], d)
elif pukul>= 10.01 and pukul<=14.59:
    print('Good', h[1], d)
elif pukul>= 15.00 and pukul<=18.00:
    print('Good', h[2], d)
elif pukul>= 18.01 and pukul<=20.59:
    print('Good', h[3], d)
elif pukul>=21.00 and pukul<=24.59:
    print('Good', h[4], d)
print('------------------------------------------------')

##kegiatan 4
import time
print('the program displays computer time')
a = time.ctime()
sec = -1
while sec != 0:
hour = a[11:13]
minute = a [14:16]
sec = int (a[17:19])
t = 0
while sec!==00:
    print(hour, ':' , minute, ':' , sec)
    sec +=1

              
              
