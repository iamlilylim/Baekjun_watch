site = input()
p = site[7:]
print(p)
q = p[:p.index('.')]
print(q)
pw = q[:3] + str(len(q)) + str(q.count('e')) + "!"
print(pw)