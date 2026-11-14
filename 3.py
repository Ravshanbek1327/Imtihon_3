def qator_ol(sorov):
    qator = input(sorov)
    while qator.strip() == "":
        qator = input()
    return qator


mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

nom = qator_ol("Mahsulot nomi: ").strip()
yangi_narx = int(qator_ol("Yangi narx: ").strip())

if nom in mahsulotlar:
    mahsulotlar[nom] = yangi_narx
    print("Narx yangilandi.")
    print(mahsulotlar)
else:
    print("Mahsulot topilmadi.")