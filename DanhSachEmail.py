f = open('CONTACT.in','r')
list = f.readlines()
res = []
for i in list:
    i = i.strip().lower()
    if i not in res:
        res.append(i)
res.sort()
for i in res:
    print(i)