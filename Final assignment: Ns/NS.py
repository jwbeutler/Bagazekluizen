def standaardprijs(afstandKM):
    standaardprijs = afstandKM*8.0
    if afstandKM <0.0:
        return 0.0
    elif afstandKM>50.0:
        return (afstandKM*6.0+1.5)
    else:
        return standaardprijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    nettoPrijs = standaardprijs(afstandKM)
    if leeftijd <= 12 or leeftijd >= 65:
        if(weekendrit):
            nettoPrijs *= 0.65
        else:
            nettoPrijs *= 0.70
    else:
        if(weekendrit):
            nettoPrijs *= 0.60
    return nettoPrijs

x = int(input('aantal afgelegde kilometers: '))
y = bool(input('is het weekend?'))
z = int(input('Wat is je leeftijd?'))
print(ritprijs(z,y,x))