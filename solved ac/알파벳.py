import string

alp = list(string.ascii_lowercase)

wrd = input()
result = []
for letter in alp:
    if letter in wrd:
        result.append(wrd.index(letter))
    else:
        result.append(-1)
print(result)
