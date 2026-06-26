s = "what is this"
str = s.split()
for x in s:
    if x == " ":
        print()
    else:
        print(x,end = "")