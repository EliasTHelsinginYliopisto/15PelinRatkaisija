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
            lista siirroista jotka johtaa ratkaisuun
        siirrot:
            tehtyjen siirtojen määrä"""

    def __init__(self, ruudukko, koko):
        self._siirtaja = Siirtokasittelija(koko)
        self._generaattori = Peligeneraattori(koko)
        self._algoritmi = Algoritmi()
        self._ruudukko = self._generaattori.validioi_ruudukkosyote(ruudukko)
        self._ratkaisu = []
        self._siirrot = 0

    def hae_ruudukko(self):
        """get metodi: palauttaa ruudukon"""
        return self._ruudukko

    def hae_siirrot(self):
        """get metodi: palauttaa siirtojen määrän"""
        return self._siirrot

    def lisaa_siirto(self):
        """lisää yhden tehtyjen siirtojen määrään"""
        self._siirrot += 1

    def tee_siirto(self, komento):
        """tekee siiron ja päivittää ratkaisun tarvittaessa
        Komennot:
            lista mahdollisista siirroista
        Returns:
            True/False:
                true jos on tehty siirto"""
        siirto = self._siirtaja.tee_siirto(self._ruudukko, komento)

        if not siirto:
            return False

        self.lisaa_siirto()
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
            self.lisaa_siirto()
            return True
        if self.tarkista_ratkaistavuus():
            self._ratkaisu = self._algoritmi.ida_star(self._ruudukko)
            return True
        return False

    def etsi_seuraava(self):
        """Etsii ratkaisussa seuraavaksi siirrettävän ruudun kordinaatit
            args:
                siirrot:
                    seuraavan siirrettävän ruudun koordinaatit suhteessa tyhjään
            Returns:
                sijainti:
                    ratkaisussa seuraavaksi siirrettävän ruudun kordinaatit"""

        if len(self._ratkaisu) == 0:
            return False
        komento = self._ratkaisu[0]
        sijainti = self._siirtaja.etsi_nolla(self._ruudukko)
        siirot = {"Up":(1,0), "Down":(-1,0), "Left": (0,1), "Right":(0,-1)}
        sijainti = [sijainti[0]+siirot[komento][0],sijainti[1]+siirot[komento][1]]

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
