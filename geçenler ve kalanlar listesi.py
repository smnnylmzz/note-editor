def not_hesaplama(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim =liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if(son_not >=90):
        harf = "AA"

    elif(son_not >= 85):
        harf = "BA"

    elif (son_not >= 80):
        harf = "BB"

    elif (son_not >= 75):
        harf = "CB"

    elif (son_not >= 70):
        harf = "CB"

    elif (son_not >= 65):
        harf = "DC"

    elif (son_not >= 60):
        harf = "DD"

    elif (son_not >= 55):
        harf = "FD"

    else:
        harf = "FF"


    return isim + "---------------------------------->" + harf + "\n"


with open("dosya.txt","r", encoding = "utf-8") as file:

    eklenecekler_listesi= []
    for i in file:
        eklenecekler_listesi.append(not_hesaplama(i))

    with open("notlar.txt","w",encoding="utf-8") as file:
        for i in eklenecekler_listesi:
            file.write(i)

    with open("geçenler.txt", "w", encoding="utf-8") as file_geçenler:
        with open("kalanlar.txt", "w", encoding="utf-8") as file_kalanlar:
            for i in eklenecekler_listesi:
                if "FF" in i:
                    file_kalanlar.write(i)
                else:
                    file_geçenler.write(i)
