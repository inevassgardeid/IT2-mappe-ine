assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting

try: 
    assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilmelding
except: 
    print("Hei på deg!")


# try:
#     hoyde = int(input("hoyde: "))
#     bredde = int(input("bredde: "))
# except:
#     print("hoyde og bredde må være heltall")

# areal = hoyde*bredde

# print(f"areal: {areal}")


def areal(hoyde, bredde):
    return hoyde*bredde
def omkrets(hoyde, bredde):
    return hoyde + hoyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14



print("koden er ferdig")