l = [i for i in input()]
if l.count("0")>0:
    l.remove("0")
    print("".join(l))
else:
    print("".join(l[1:]))