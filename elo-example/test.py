def Elo(Ra, Rb, winner):
    k = 40
    
    if winner == 1:
        Sa = 1
        Sb = 0
    else:
        Sb = 1
        Sa = 0

    Qa = 10**(Ra/400)
    Qb = 10**(Rb/400)

    Ea = Qa / (Qa + Qb)
    Eb = Qb / (Qa + Qb)
    print("Expected score: ", Ea, Eb)

    Rua = Ra + k * (Sa - Ea)
    Rub = Rb + k * (Sb - Eb)
    print("Rating: ", Rua, Rub)

    return(Rua, Rub)

"""
Admittedly bad expample use case of the code provided
Test holds the hypothetical score of four different competing teams
"""

test = {
        "a":1400,
        "b":1400,
        "c":1400,
        "d":1400
        }

"""
User is prompted to select the two competing teams
Along with a numerical representation of the winning team
1 being the first team entered and then any other value being the second
"""

while True:
    print(test)
    a = input()
    b = input()
    w = int(input())

    r = Elo(test[a], test[b], w)
    print(r)
    test[a] = r[0]
    test[b] = r[1]
