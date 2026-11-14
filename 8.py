import json

def qator_ol(sorov):
    qator = input(sorov)
    while qator.strip() == "":
        qator = input()
    return qator


with open("products.json", "r", encoding="utf-8") as fayl:
    mahsulotlar = json.load(fayl)

nom = qator_ol("Mahsulot nomi: ").strip()
yangi_miqdor = int(qator_ol("Yangi miqdor: ").strip())

topildi = False
for mahsulot in mahsulotlar:
    if mahsulot["nom"] == nom:
        mahsulot["miqdor"] = yangi_miqdor
        topildi = True

if topildi:
    with open("products.json", "w", encoding="utf-8") as fayl:
        json.dump(mahsulotlar, fayl, indent=4, ensure_ascii=False)
else:
    print("Mahsulot topilmadi.")