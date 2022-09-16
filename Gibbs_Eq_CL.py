print("A= Equilibre de Gibbs Donnan")
print("B= potentiel d'équilibre d'un ion")

calcul=input("Que souhaitez vous calculer?")

import math

if calcul=="a" or "A":
    print("Equilibre de Gibbs Donnan")
    print("X1 * Y1 = X2 * Y2")
    inconnue= input("Quelle est la concentration inconnue? (X1 ou X2)")
    if inconnue == "X1":
        Y1= float((input("Y1 =?")))
        X2= float((input("X2=?")))
        Y2= float((input("Y2 =?")))
        inconnue= (X2*Y2)/Y1
        print("X1=")
        print(inconnue)
    elif inconnue=="X2":
        X1 = float((input("X1 =?")))
        Y1 = float((input("Y1 =?")))
        Y2 = float((input("Y2 =?")))
        inconnue= (X1*Y1)/Y2
        print("X2=")
        print(inconnue)

elif calcul=="b" or "B":
    Xi=float(input("Xi=?"))
    Xe=float(input("Xe=?"))
    Valence=int(input("valence?"))
    Condition=input("Temperature")
    if Condition == "20":
        pot=((-Valence)*58)*(math.log((Xi/Xe),10))
        print("E=")
        print(pot)
    elif Condition == "37":
        pot = ((-Valence) * 61) * (math.log((Xi / Xe), 10))
        print("E=")
        print(pot)



