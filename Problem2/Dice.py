from random import randrange
def Diceroll():
    Droll = randrange(1,7)
    if Droll == 1:
        return "1"
    if Droll == 2:
        return "2"
    if Droll == 3:
        return "3"
    if Droll == 4:
        return "4"
    if Droll == 5:
        return "5"
    if Droll == 6:
        return "6"

def quincunx():
    quincunx = 0
    n = 1000000
    for i in range(n):
        if Diceroll() == "5":
            quincunx +=1
    prob = (quincunx)/(n)
    print("The prob for the quincunx is",prob)


quincunx()
