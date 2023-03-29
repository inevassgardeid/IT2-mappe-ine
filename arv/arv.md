# Arv

## Superklasse
Blir arvet fra
Superklasser skal ikke brukes direkte, men brukes gjennom subklassene.

Eksempel:

```python

 """
    Attributes:
        epost: En string med brukers epost
        fornavn = En string med brukers fornavn
        etternavn = En string med brukers etternavn
"""

class Bruker:
    def __init__(self, epost, fornavn, etternavn):
        self._epost = epost
        self._fornavn = fornavn
        self._etternavn = etternavn

    def logg_inn(self):
        print(f"{self._epost} logget inn")

    def logg_ut(self):
        print(f"{self._epost} logget ut")
```


## Subklasse
Arver fra superklasse
Vi skriver navnet på superklassen i parantes bak navnet på klassen for å gi beskjed om at vi arver fra den. 
Subklasser kan ogsp være superklasser til andre subklasser. Da brukes heller ikke de direkte.

Eksempel på en subklasse som også fungerer som en superklasse:

```python

class Lærer(Bruker):
    """Subklasse for brukere i skolesystemet og superklasse for lærere i skolesystemet. Skal ikke brukes direkte

    Attributes:
        epost: En string med brukers epost
        fornavn = En string med brukers fornavn
        etternavn = En string med brukers etternavn
        lønnskonto = En integer med brukers lønnskonto
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self._lønnskonto = lønnskonto

```

Eksempel på en ren subklasse:

```python
class Faglærer(Lærer):
    """Subklasse for lærere i skolesystemet. Skal brukes direkte

    Attributes:
        epost: En string med lærerens epost
        fornavn = En string med lærerens fornavn
        etternavn = En string med lærerens etternavn
        lønnskonto = En integer med lærerens lønnskonto
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self._kompetanse = []
        self._klasser = []

```