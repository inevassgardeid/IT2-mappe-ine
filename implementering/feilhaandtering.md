# Vern mot kjøretidsfeil og logiske feil i programmer

## kjøretidsfeil

Håndtering av kjøretidsfeil i python gjøres med nøkkelordene try og except.
Python forsøker å kjøre kodeblokken som ligger under `try:`, hvis python får en feilmelding, vil den kjøre kodeblokken som ligger under `except:`.

```python
try:
    alder = int(input("Alder: "))
    fødselsår = 2022 - alder
    print(f"fødselsår: {fødselsår}")
except:
    print("feil: alder må være et heltall")

print("koden fortsetter")
```

### Eksperttips: While-løkke med try-except

```python
while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
```

## Logiske feil i programmer

For å oppdage logiske feil i python-programmer kan vi bruke nøkkelordet `assert for å forsikre oss om at koden gir korrekte resultat.

Eksempel:

```python
assert 10 > 5 # gir ikke feil
assert 10 > 2 # gir feil
```

Eksempel: Test av funksjoner med assert:

```python
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

```

### Eksperttips: Håndtering av kjøretidsfeil og logisk feil

```python
while True:
    try:
        alder = int(input("Alder: "))
        assert alder >= 0
        break
    except:
        print("alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
```