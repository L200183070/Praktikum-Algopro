## kegiatan 1 , Make Program
##a= {'NIM':'L200183070', 'Name' : 'Aulia Septianingrum R.N'
##    ,'Address':'Jayapura,Papua','Post_Code' : '123456',
##    'City':'Jayapura','Province' : 'Papua','Nasionality' : 'WNI'}
##
##def NIM():
##    print(a['NIM'])
##def Name():
##    print(a['Name'])
##def Address():
##    print(a['Address'])
##def Post_Code():
##    print(a['Post_Code'])
##def City():
##    print(a['City'])
##def Province():
##    print (a['Province'])
##def Nasionality():
##    print (a['Nasionality'])
##
##def b():
##    print('''Options avalaible:
##b display this help
##1 display NIM
##2 display Name
##3 display Address
##4 display Post Code
##5 display City
##6 display Province
##7 display Nasionality
##c Exit ''')
##b()
##
##while True :
##    m = input('Your Choice:')
##    if m == "b" :
##        b()
##    elif m == "1":
##        NIM()
##    elif m == "2":
##        Name()
##    elif m == "3":
##        Address()
##    elif m == "4":
##        Post_Code()
##    elif m == "5":
##        City()
##    elif m == "6":
##         Province()
##    elif m == "7":
##        Nasionality()
##    elif m == "c":
##        print('Exit')
##        break
##    else:
##        print('invalid')


##kegiatan 2, make function
def temperature_conversion(C = 0,F = 0):
    if C != 0:
        F = int(9 / 5 * C + 32)
        print('Temperature', C,'Celcius equal to', F,'Farenheit')
    elif F !=0:
        C = int(5 / 9 * (F - 32))
        print('Temperature', F,'Farenheit equal to', C,'Celcius')
    elif F !=0 and C != 0:
        F = int(9 / 5 * C + 32)
        print('Temperature', C,'Celcius equal to', F,'Farenheit')
    else:
        F = int(9 / 5 * C + 32)
        print('Temperature', C,'Celcius equal to', F,'Farenheit')
        
    




