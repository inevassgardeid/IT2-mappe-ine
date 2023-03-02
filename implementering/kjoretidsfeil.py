# try:
#     alder = int(input("Alder: "))
#     fødselsår = 2022 - alder
#     print(f"fødselsår: {fødselsår}")
# except:
#     print("feil: alder må være et heltall")

# print("koden fortsetter")

while True:
    try:
        alder = int(input("Alder: "))
        assert alder >= 0
        break
    except:
        print("alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")