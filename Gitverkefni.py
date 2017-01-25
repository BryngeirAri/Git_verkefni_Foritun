#Git verkefni Bryngeir Ari Kristinsson
svar = "já"
while svar == "já":
    print("1. Fyrsta verkefnið")
    print("2. Seinna verkefnið")
    print("3. Þriðja verkefnið")
    print("4. Hætta í valmynd")

    val = int(input("Hvað viltu gera?"))
    if val ==1:
        print("Góðan daginn! hérna ætla ég að biðja þig um tvær tölur og leggja þær saman og margfalda fyrir þig")


    if val==2:
        print("Góðan daginn, hérna mun ég biðja þig um nafnið þitt og síðan heilsa þér")


    if val ==3:
        print("Góðan daginn, hérna mun ég biðja þig um texta og mun síðan telja lágu og hástafi hjá þér")
        

    if val ==4:
        break
