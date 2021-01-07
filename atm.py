def hesap(a):
    #verilen  tutarda kaç adet 100 tl olduğu
    b=int(a/100)
    print("100 Lira :",b)
    #100 katlarını çıkarınca kalan kısım
    c=a-(100*b)
    d=int(c/50)
    print("50  Lira :",d)
    #50 nin katlarını çıkarınca kalan kısım
    e=c-(d*50)
    f=int(e/20)
    print("20  Lira :",f)
    #20 nin katlarını cıkarınca kalan kısım
    g=e-(f*20)
    h=int(g/10)
    print("10  Lira :",h)
    #10 un katlarını çıkarınca kalan kısım
    j=g-(h*10)
    l=int(j/5)
    print("5   Lira :",l)
    #10 un katlarını çıkarınca kalan kısım
    z=j-(l*5)
    x=int(z/1)
    print("1   Lira :",x)
    #5 in katlarını çıkarınca kalan kısım
    p=z-(x*1)
    v=int(p/0.5)
    print("50 Kuruş :",v)
    #1 in katlarını çıkarınca kalan kısım
    n=p-(v*0.5)
    m=int(n/0.25)
    print("25 Kuruş :",m)
    #0.5 katlarını çıkarınca kalan kısım
    ö=n-(m*0.25)
    ç=int(ö/0.10)
    print("10 Kuruş :",ç)
    #0.1 katlarını çıkarınca kalan kısım
    u=ö-(ç*0.10)
    ı=int(u/0.05)
    print("5 Kuruş  :",ı)


harcama=float(input("Lütfen yapılan alışveriş tutarını giriniz(TL):"))

if harcama>1000.0:
    print("Bütçeniz müsait değil.")
else:
    if harcama % 5 != 0.0:
        print("5 kuruşun katlarını girmelisiniz")
    else :
        paraUstu=float(input("Lütfen yapılan ödeme tutarını giriniz(TL):"))
        if paraUstu % 5 != 0.0:
            print("5 kuruşun katlarını girmelisiniz")
        else:
            a =float(paraUstu-harcama)
            if harcama>paraUstu:
                print("Eksik Ödeme.")
            else:
                print("Ödenen Tutar (lira) ",paraUstu)
                print("Alışveriş tutarı (lira) ",harcama)
                print("PARA ÜSTÜ: ",a,"TL")
                hesap(a)
            


    
   





