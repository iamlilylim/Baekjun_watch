import json
import os
import random

LUNCH = 'lunch.json'
if os.path.exists(LUNCH):
    with open(LUNCH,'r', encoding = 'utf-8') as f:
        lunch = json.load(f)

else:
    lunch = ['salad', 'asai ball', 'greek yogurt', 'fruit ball']

lunch = ['salad', 'asai ball', 'greek yogurt', 'fruit ball']

print("What's the lunch today?🫐🍱")
print('lists:',lunch)
add = input('Tell me what you want to add! if you just press "enter," you have the original lists')
if add:
    lunch.append(add)
    with open(LUNCH, 'w', encoding='utf-8') as f:
        json.dump(lunch, f, ensure_ascii= False, indent = 2)

    print(f"{add} is added")

menu = random.choice(lunch)

#print('Deburg------', menu)
print(f"What do you think of ⭐️{menu}⭐ for lunch today?☺️")
