class Bruker:
    """Superklasse for brukere i skolesystemet. Skal ikke brukes direkte

    Attributes:
        epost: En string med brukers epost
        fornavn = En string med brukers fornavn
        etternavn = En string med brukers etternavn
    """
    def __init__(self, epost, fornavn, etternavn):
        self._epost = epost
        self._fornavn = fornavn
        self._etternavn = etternavn
    
    def logg_inn(self):
        print(f"{self._epost} logget inn")
    
    def logg_ut(self):
        print(f"{self._epost} logget ut")

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

class Kontaktlærer(Lærer):
    """Subklasse for lærere i skolesystemet. Skal brukes direkte

    Attributes:
        epost: En string med lærerens epost
        fornavn = En string med lærerens fornavn
        etternavn = En string med lærerens etternavn
        lønnskonto = En integer med lærerens lønnskonto
        klasse = En string med lærerens klasse
        trinn = En integer med lærerens trinn
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self._klasse = klasse
        self._trinn = trinn

class Elev(Bruker):
    """Subklasse for elever i skolesystemet. Skal brukes direkte

    Attributes:
        epost: En string med elevens epost
        fornavn = En string med elevens fornavn
        etternavn = En string med elevens etternavn
        trinn = En integer med elevens klasse
        klasse = En string med elevens klasse
    """
    def __init__(self, epost, fornavn, etternavn, trinn, klasse):
        super().__init__(epost, fornavn, etternavn)
        self._trinn = trinn
        self._klasse = klasse
        self._fag = []


# Denne brukes for testing, betyr at koden innenfor if-setningen 
# kun kjøres hvis vi "trykker play" på denne filen eller kjører denne filen i terminalen
if __name__ == " __main__":
    ravi = Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)
    ravi.logg_inn() 
    ravi.logg_ut()

    camilla = Elev("camilac@kkg.no", "Camilla", "Coward", 2, "STG")
    camilla.logg_inn
    camilla.logg_ut()