def decoder(c,k,m):
    new_k=[]
    for i in range(0,len(k)):
        if(ord(k[i])>=65 and ord(k[i])<=90): #将密匙全转化为小写
            new_k.append(chr(ord(k[i])+32))
        else:
            new_k.append(k[i])
    int_k=[]
    for i in range(0,len(k)):                #将密匙转化为整形
        int_k.append(ord(new_k[i])-97)
    new_c=[]
    for i in range(0,len(c)):
        if(ord(c[i])>=65 and ord(c[i])<=90): #将密文全转化为小写
            new_c.append(chr(ord(c[i])+32))
        else:
            new_c.append(c[i])
    int_c=[]
    for i in range(0,len(c)):                #将密匙转化为整形
        int_c.append(ord(new_c[i])-97)
    for i in range(0,len(c)):
        s=i % len(k)
        m.append(chr(int_c[i]-int_k[s]+97))
    for i in range(0, len(m)):
        print(chr(ord((m[i]))))


