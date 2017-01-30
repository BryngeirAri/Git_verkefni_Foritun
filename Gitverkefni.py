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
        tala1=int(input("Sláðu inn fyrstu töluna"))
        tala2=int(input("Sláðu inn seinnu töluna"))
        summa=tala1+tala2
        margfoldun=tala1*tala2
        print("Svona eru tölunar lagðar saman ", summa)
        print("Svona eru tölurnar margfaldaðar ", margfoldun)



    if val==2:
        print("Góðan daginn, hérna mun ég biðja þig um nafnið þitt og síðan heilsa þér")
        fornafn = input("Hvað er fornafnið þitt?")
        eftirnafn = input("Hvað er eftir nafnið þitt?")
        print("Halló ", fornafn, eftirnafn, "!")

    if val ==3:
        print("Góðan daginn, hérna mun ég biðja þig um texta og mun síðan telja lágu og hástafi hjá þér")
        texti = input("Sláðu inn texta!: ")
        print("Hástafir: ", sum(1 for c in texti if c.isupper()))
        print("Lágstafir: ", sum(1 for c in texti if c.islower()))
        teljari = 0
        for x in range(len(texti)):
            if texti[x].isupper():
                i = x + 1
                if texti[i].islower():
                    teljari = teljari +1
        print("það eru svona margir lágstafir á eftir hástöfum", teljari)

    if val ==4:
        break

