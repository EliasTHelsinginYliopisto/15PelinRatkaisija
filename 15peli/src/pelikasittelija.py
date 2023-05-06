"""Peligeneraattori vastaa pelimatriisin
siirtokäsitttelijä vastaa siirtojen tekemisestä
algoritmi vastaa pelin ratkaisusta"""
from peligeneraattori import Peligeneraattori
from siirtokasittelija import Siirtokasittelija
from algoritmi import Algoritmi

class Pelikasittelija:
    """Hallitsee ja ohjaa pelin toimintoja
    Attributes:
        siirtäjä:
            siirtokäsittelijä-luokka
        generaattori:
            peligeneraattori-luokka
        algoritmi:
            algoritmi-luokka
        ruudukko:
            pelitila matriisina
        ratkaisu:
            lista siirroista jotka johtaa ratkaisuun"""

    def __init__(self, ruudukko, koko):
        self._siirtaja = Siirtokasittelija()
        self._generaattori = Peligeneraattori(koko)
        self._algoritmi = Algoritmi()
        self._ruudukko = self._generaattori.validioi_ruudukkosyote(ruudukko)
        self._ratkaisu = []

    def hae_ruudukko(self):
        """get funktio: palauttaa ruudukon"""
        return self._ruudukko

    def tee_siirto(self, komento):
        """tekee siiron ja päivittää ratkaisun tarvittaessa
        Returns:
            True/False:
                true jos on tehty siirto"""
        siirto = self._siirtaja.tee_siirto(self._ruudukko, komento)

        if not siirto:
            return False
        if len(self._ratkaisu) == 0:
            return True
        if komento == self._ratkaisu[0]:
            self._ratkaisu = self._ratkaisu[1:]
            return True

        komennot = ["Up", "Left", "Down", "Right"]
        for i, jono in enumerate(komennot):
            if jono == komento:
                self._ratkaisu.insert(0,komennot[i-2])
        return True

    def ratkaise(self):
        """Jos ratkaisu on löydetty toteuttaa ratkaisun seuraavan siirron
        Muuten tarkistaa onko peli ratkaistavissa ja käynnistää ratkaisualgoritmin
        Returns:
            True/False
                false jos ratkaisu ei etene"""

        if len(self._ratkaisu) > 0:
            self._siirtaja.tee_siirto(self._ruudukko, self._ratkaisu[0])
            self._ratkaisu = self._ratkaisu[1:]
            return True
        if self.tarkista_ratkaistavuus():
            self._ratkaisu = self._algoritmi.ida_star(self._ruudukko)
            return True
        return False

    def etsi_seuraava(self):
        """Etsii ratkaisussa seuraavaksi siirrettävän ruudun kordinaatit
            Returns:
                sijainti:
                    ratkaisussa seuraavaksi siirrettävän ruudun kordinaatit"""
        if len(self._ratkaisu) == 0:
            return False
        komento = self._ratkaisu[0]
        sijainti = self._siirtaja.etsi_nolla(self._ruudukko)
        if komento == "Up":
            sijainti[0] += 1
        elif komento == "Down":
            sijainti[0] -= 1
        elif komento == "Left":
            sijainti[1] += 1
        else:
            sijainti[1] -= 1
        return sijainti

    def tarkista_ratkaistavuus(self):
        """Tarkistaa onko peli ratkaistavissa.
            Jos ei, syy tulostetaan.
        Args:
            lista:
                peliruudukko listamuodossa"""

        lista = []
        for rivi in self._ruudukko:
            for numero in rivi:
                lista.append(numero)

        if not self._generaattori.tarkista_ratkaistavuus(lista):
            print("Pelille ei ole ratkaisua")
            return False

        lista.pop()
        for i, numero in enumerate(lista):
            if i+1 != numero:
                return True
        print("Peli on jo ratkaistu")
        return False
