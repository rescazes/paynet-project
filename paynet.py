k_ketliklar = ["0000","1111", "2222", "3333", "4444",
               "5555", "6666", "7777", "8888", "9999"]
paynet_tarixi = {}
sotilgan_nomerlar = []
paynet_xazna = 0
nomer_xazna = 0
menyu = """
    Paynetimizga xush kelibsiz!

	1) Paynetdan foydalanish
	2) Nomer sotib olish
	3) Paynet tarixi
	4) Paynet va nomer xaznasi
	5) Sotilgan nomerlar
	0) Chiqish
"""
operatorlar = ["99", "97", "95", "94", "93", "91", "90",
               "88", "77", "71", "55", "50", "33", "20"]

while True:
    print(menyu)
    menyu_tanlash = int(input("\tMenyulardan birini tanlang: "))

    if menyu_tanlash == 1:
        while True:
            nomer = input("\n\tNomeringizni kiritng: ")
            if len(nomer) == 13 and nomer[0:4:] == "+998" and nomer[4:6:] in operatorlar:
                pul = int(input("\tQancha pul tashlamoqchisiz: "))
                uslug = (pul // 100)
                pul -= uslug
                paynet_xazna += uslug
                paynet_tarixi.update({nomer : pul})
                print("\n\tPul to'landi!")
                break
            else:
                print("\n\tNomeringiz xato kiritildi!")
    elif menyu_tanlash == 2:
        while True:
            nomer_t = input("\n\tQanday raqam sotib olmoqchisiz, kiriting: ")
            if nomer_t not in sotilgan_nomerlar:
                if len(nomer_t) == 13 and nomer_t[0:4:] == "+998" and nomer_t[4:6:] in operatorlar:
                    if nomer_t not in sotilgan_nomerlar and nomer_t[6:10:] in k_ketliklar or nomer_t[9:13:] in k_ketliklar:
                        print(f"""
        {nomer_t} bu nomer mavjud, narxi 400.000 so'm!
                                   
        1) Sotib olish
        0) Ortga qaytish
                               """)
                        sorash = int(input("\tSotib olishni xohlaysizmi: "))

                        if sorash == 1:
                            sotilgan_nomerlar.append(nomer_t)
                            nomer_xazna += 400000
                            print("\n\tNomer sotib olindi")
                            break
                        else:
                            print("\n\tAsosiy menyu")
                            break
                    else:
                        print(f"""
    {nomer_t} bu nomer mavjud, narxi 100.000 so'm!
    
    1) Sotib olish
    0) Ortga qaytish
                                                   """)
                        sorash = int(input("\tSotib olishni xohlaysizmi: "))

                        if sorash == 1:
                            sotilgan_nomerlar.append(nomer_t)
                            nomer_xazna += 100000
                            print("\n\tNomer sotib olindi")
                            break
                        else:
                            print("\n\tAsosiy menyu")
                            break
                else:
                    print("\n\tNomer xato kiritildi!")
            else:
                print("\n\tBu nomer sotilgan!")
    elif menyu_tanlash == 3:
        print(f"\n\tPaynet tarixi {paynet_tarixi}")
    elif menyu_tanlash == 4:
        print(f"\n\tPaynet xaznasidagi summa: {paynet_xazna} so'm!")
        print(f"\tNomer xaznasidagi summa: {nomer_xazna} so'm!")
    elif menyu_tanlash == 5:
        print(f"\n\t{sotilgan_nomerlar}")
    elif menyu_tanlash == 0:
        print("\n\tTashrifingiz uchun rahmat!")
        break
    else:
        print("\n\tBunday menyu mavjud emas!")




