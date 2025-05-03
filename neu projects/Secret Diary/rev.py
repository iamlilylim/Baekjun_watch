from datetime import date
today = date.today()
PW = 'ta'

pas = input("What's the Magic Word?")
#print('Deburg-----', pas)
if pas == PW:
    print("Your Diary is Open📃")
    b = input("Today I feel ")
    dr = input("Because")

    with open('logue.txt','a',encoding='utf-8')as d:
        d.write(b+'\n'+dr+'\n'+'This is written on'+str(today))

    print("Your diary is updated🔐",'on',today)

else:
    print("Access denied. Try again")
