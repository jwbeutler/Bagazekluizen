def inlezen_beginstations(stations):
    while True:
        beginstation = input('Voer beginstation in: ')
        if beginstation in stations:
            break
    return beginstation

def inlezen_eindstations(stations,beginstation):
    while True:
            eindstation = input('Voer eindstation in: ')
            if eindstation in stations and stations.index(eindstation) > stations.index(beginstation):
                return eindstation
            else:
                print('De trein komt niet in {}'.format(eindstation))

def omroepen_reis(stations,beginstation,eindstation):
    beginstationnummer = stations.index(beginstation) + 1
    eindstationnummer = stations.index(eindstation) + 1
    afstand = eindstationnummer - beginstationnummer
    tussenstops = stations[beginstationnummer:eindstationnummer - 1]
    print('De afstand bedraagt {} station(s)'.format(afstand))
    prijs = afstand * 5
    print('De prijs van het kaartje is {} euro'.format(prijs))
    print('')
    print('Je stapt in de trein in: {}'.format(beginstation))
    print('- {}'.format(tussenstops))
    print('Je stapt de trein uit in: {}'.format(eindstation))



stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstations(stations)
eindstation = inlezen_eindstations(stations,beginstation)
omroepen_reis(stations, beginstation, eindstation)


