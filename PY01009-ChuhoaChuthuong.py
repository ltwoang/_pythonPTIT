s = input()
s1 = 0 #thuong
s2 = 0
for i in s:
    if i.islower() :
        s1 += 1
    else :
        s2 += 1

if s1 >= s2 :
    print(s.lower())
else:
    print(s.upper())