import vigenere_coder
import vigenere_decoder
value=" "
value=input("coder or decoder")
if(value=="coder"):
    m=input("请输入明文")
    k=input("请输入密匙")
    c=[]                                              # 将密文放入c中
    vigenere_coder.coder(m,k,c)
    x=input("按任何键继续")

elif(value=="decoder"):
    c=input("请输入密文")
    k=input("请输入密匙")
    m=[]
    vigenere_decoder.decoder(c,k,m)
    x=input("按任何键继续")
    def coder(m,k):
        for z in range(0,len(k)):                     # 将密匙全转化成小写
            if (int(k[z]) >= 65 and int(k[z]) <= 90):
                k[z]=str(int(k[z])+32)

        int_k=[]                                      #将密匙转化成对应的整形
        for n in range(0,len(k)):
            int_k.append(int(k[n])-97)

        for i in range(0,len(m)):
            if(int(m[i])>=65 and int(m[i])<=90):     # 将明文全转化成小写
                m[i]=str(int(m[i])+32)
        int_m=[]
        for i in range(0,len(m)):                    # 将明文转化为对应的整形
            int_m.append(int(m[i])-97)

        for i in range(0,len(m)):
            s=i % len(k)
            c.append(str((int_k[s]+int_m[i])%26+97))
        print(c)













