print("Calcolatore Indici Salute")

mof = int(input("Sei un maschio o una femmina? (1/0): "))
if mof == 1:
    print("Perfetto!")
elif mof == 0:
    print("Perfetto!")
else:
    quit()

age = int(input("Quanti anni hai? "))
if age >= 99:
    quit()
elif age <= 6:
    quit()

hgt = int(input("Inserisci Altezza in cm: "))
if hgt >= 210:           # Altezza non realistica per il 99.9% della popolazione, formula di Lorenz non funziona bene con altezze esagerate
    quit()
elif hgt <= 130:            # Altezza non realistica per il 99.9% della popolazione adulta, formula di Lorenz non funziona bene con altezze troppo piccole
    quit()

wgt = int(input("Inserisci Peso in kg: "))
if wgt >= 200:           # Peso non realistico per il 99.9% della popolazione
   quit()
elif wgt <= 35:            # Peso non realistico per il 99.9% della popolazione
    quit()

m_BMI = wgt / ((hgt / 100) ** 2)          # Dato da salvare perché utile per altre formule
f_BMI = wgt / ((hgt / 100) ** 2)          # Dato da salvare perché utile per altre formule

exrcs = input("Ti alleni durante la settimana? (y/n): ")
if exrcs == "y": 
    print("Perfetto! Continua così!")
elif exrcs == "n":
    print("Ah... Sai che allenarsi anche 2-3 volte alla settimana riduce il rischio cardiovascolare del 20-30%? Pensaci.")
else:
    print('Hai sbagliato, inserisci "y" o "n" la prossima volta.')
    quit()
while True:
    print("Cosa vuoi calcolare?")
    print("Indice di massa corporea (BMI): 1")
    print("Formula per peso ideale: 2")
    print("Metabolismo Basale: 3")
    print("Stima % grasso corporeo: 4")

    ans1 = int(input("Inserisci il Valore che vuoi calcolare: "))

    if mof == 1:
        if ans1 == 1:
            m_BMI = wgt / ((hgt / 100) ** 2)
            print(m_BMI)
            print("Range BMI:")
            print("< 18.5: Sottopeso")
            print("18.5 - 24.9: Normopeso")
            print("25.0 - 29.9: Sovrappeso")
            print(">= 30.0: Obesità")
        elif ans1 == 2:
            m_IBW = hgt - 100 - ((hgt - 150) / 4)
            print(m_IBW)
            print("Range di tolleranza peso forma: ± 5% rispetto al valore calcolato.")
        elif ans1 == 3:
            m_BMR = (10 * wgt) + (6.25 * hgt) - (5 * age) + 5
            print(m_BMR)
            print("Il valore ottenuto rappresenta le calorie minime giornaliere bruciate a riposo.")
            print("Media Maschile: 1600 - 1900 kcal/die")
        elif ans1 == 4:
            m_PBF = (1.20 * m_BMI) + (0.23 * age) - (10.8 * mof) - 5.4
            print(m_PBF)
            print("Range Grasso Uomo:")
            print("< 10%: Molto basso / Essenziale")
            print("10% - 20%: Normale / In forma")
            print("21% - 25%: Moderatamente alto")
            print("> 25%: Grasso elevato / Rischio obesità")
        else:
            quit()

    if mof == 0:
        if ans1 == 1:
            f_BMI = wgt / ((hgt / 100) ** 2)
            print(f_BMI)
            print("Range BMI:")
            print("< 18.5: Sottopeso")
            print("18.5 - 24.9: Normopeso")
            print("25.0 - 29.9: Sovrappeso")
            print(">= 30.0: Obesità")
        elif ans1 == 2:
            f_IBW = hgt - 100 - ((hgt - 150) / 2)
            print(f_IBW)
            print("Range di tolleranza peso forma: ± 5% rispetto al valore calcolato.")
        elif ans1 == 3:
            f_BMR = (10 * wgt) + (6.25 * hgt) - (5 * age) - 161
            print(f_BMR)
            print("Il valore ottenuto rappresenta le calorie minime giornaliere bruciate a riposo.")
            print("Media Femminile: 1200 - 1500 kcal/die")
        elif ans1 == 4:
            f_PBF = (1.20 * f_BMI) + (0.23 * age) - (10.8 * mof) - 5.4
            print(f_PBF)
            print("Range Grasso Donna:")
            print("< 18%: Molto basso / Essenziale")
            print("18% - 28%: Normale / In forma")
            print("29% - 35%: Moderatamente alto")
            print("> 35%: Grasso elevato / Rischio obesità")
        else:
            quit()
    
    loop = input("Vuoi calcolare un altro parametro? (y/n): ")
    if loop != "y":
        print("Va bene! Puoi chiudere l'app")
        break
