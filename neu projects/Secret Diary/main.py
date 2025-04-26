'''
목표: 사용자가 입력한 글을 비밀번호로 저장된 일기로 만듦
사용 기술: file, input, if, string
추가기능: 쓴 날짜 저장(Homework)
'''

#pw setting
PASSWORT = '1234' # 추후에 input으로 바꿔서 update
#사용자에게 비밀번호 입력 받기
user_pw = input('🔐🔐B밀번호를 입력하세요🔐🔐: ')
print('Deburg ------', user_pw)

#비밀번호가 맞는지 확인:
if user_pw ==PASSWORT:
    print('diary opened! write a diary.📖')
    diary = input('what today:')

    #파일에 저장
    with open('diary.txt', 'a', encoding='utf-8') as f:
        f.write(diary + '\n')

    print('your diary is saved❤️')

else:
    print('Wrong passwort. Access denied.')