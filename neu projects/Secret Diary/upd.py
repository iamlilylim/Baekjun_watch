
from datetime import date
today = date.today()
PW = 'ta'

while True:

    pas = input("What's the Magic Word?")
    if pas == PW:
        print("Your Diary is Open📃")
        b = input("Today I feel ")
        dr = input("Because ")
        etc = input("Anything else to mention?")

        with open('logue.txt','a',encoding='utf-8')as d:
            d.write(b+'\n'+dr+'\n'+etc+'\n'+'This is written on'+str(today))

        print("Your diary is updated🔐",'on',today)
        break
    else:
        print("Access denied. Try again")
