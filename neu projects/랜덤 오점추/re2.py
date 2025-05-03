import os
import json
import random

LUNCH = 'essen.json'
default_sub = ['matcha', 'yogurt', 'latte', 'milk','soft drink']
if os.path.exists(LUNCH):
    with open(LUNCH,'r',encoding='utf-8') as f:
        drinks = json.load(f)

else:
    drinks = default_sub


print("점심 대신 마실 음료를 골라보자")
print("이런 것들이 있어👉🏻", drinks)



add = input("선택폭에 추가 하고 싶은게 있으면 써봐!")
if add:
    drinks.append(add)
    with open(LUNCH, 'w', encoding='utf-8') as f:
        json.dump(drinks,f,ensure_ascii= False,indent=4)
    print(f"{add}가 추가되었어요")


choice = random.choice(drinks)
print(f"오늘 점심 대신 마실 음료는 {choice}야")