'''
주제: 학생들이 직접 메뉴 만들어 그 중에서 점심마다 한 개를 랜덤으로 추천
필요 기술: random, input, list
확장 가능: 메뉴 추가/삭제, JSON으로 저장, GUI변환?
'''

import random
import json
import os



JSONDB = 'menus.jason'
# JSON 파일에서 메뉴불러오기
if os.path.exists(JSONDB):
    with open(JSONDB, 'r', encoding = 'utf-8') as f: # 유니코드, 이  instant를 f로 한다.
        menus = json.load(f)

else:
    menus = ['김밥', '떡볶이', '햄버거', '라면', '쌀국수', '치킨']


#메뉴 리스트 만들기
menus = ['김밥', '떡볶이', '햄버거', '라면', '쌀국수', '치킨']
print("오늘 뭐 먹지?🍕🥙🍔")
print('메뉴 목록:', menus)

#사용자가 메뉴를 입력해서 추가 한다
add = input("Add what you want to have(just 'enter' doesn't work.):")
if add:
    menus.append(add)
    with open(JSONDB, 'w', encoding = 'utf-8') as f:
        json.dump(menus,f, ensure_ascii = False, indent = 2)
    print(f"'{add}' is added!")

#메뉴 중 하나를 랜덤으로 추천
choice = random.choice(menus)

#print('Debug --- choice value is ', choice)

print(f"\n\n Lunch of the day is... {choice}😝")
