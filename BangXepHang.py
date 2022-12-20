n = int(input())
s = {"name":[],"dung":[],"submit":[]}
for i in range(n):
    x = str(input())
    s["name"].append(x)
    k , m = map(int,input().split())
    s["dung"].append(k)
    s["submit"].append(m)
for i in range(n):
    for j in range(i+1,n):
        if s["dung"][j] > s["dung"][i]:
            s["name"][i],s["name"][j] = s["name"][j],s["name"][i]
            s["dung"][i],s["dung"][j] = s["dung"][j],s["dung"][i]
            s["submit"][i],s["submit"][j] = s["submit"][j],s["submit"][i]
        elif s["dung"][j] == s["dung"][i]:
            if s["submit"][j] < s["submit"][i]:
                s["name"][i],s["name"][j] = s["name"][j],s["name"][i]
                s["dung"][i],s["dung"][j] = s["dung"][j],s["dung"][i]
                s["submit"][i],s["submit"][j] = s["submit"][j],s["submit"][i]
            elif s["submit"][j] == s["submit"][i]:
                if s["name"][j] < s["name"][i]:
                    s["name"][i],s["name"][j] = s["name"][j],s["name"][i]
                    s["dung"][i],s["dung"][j] = s["dung"][j],s["dung"][i]
                    s["submit"][i],s["submit"][j] = s["submit"][j],s["submit"][i]
for i in range(n):
    print(s["name"][i], s["dung"][i],s["submit"][i],sep=" ")