def coder(m, k,c):
    new_k=[]
    for z in range(0, len(k)):                # 将密匙全转化成小写
        if (ord(k[z]) >= 65 and ord(k[z]) <= 90):
            new_k.append(chr(ord(k[z]) + 32))
        else:
            new_k.append(k[z])

    int_k = []                                # 将密匙转化成对应的整形
    for n in range(0, len(new_k)):
        int_k.append(ord(new_k[n]) - 97)
    new_m=[]
    for i in range(0, len(m)):
        if (ord(m[i]) >= 65 and ord(m[i]) <= 90):  # 将明文全转化成小写
            new_m.append( chr(ord(m[i]) + 32))
        else:
            new_m.append(m[i])
    int_m = []
    for i in range(0, len(new_m)):                 # 将明文转化为对应的整形
        int_m.append(ord(new_m[i]) - 97)

    for i in range(0, len(new_m)):
        s = i % len(new_k)
        c.append(str((int_k[i] + int_m[i]) % 26 + 97))
    for i in range(0,len(c)):
        print(chr(int((c[i]))))