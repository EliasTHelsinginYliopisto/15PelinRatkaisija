"""Tkinter kirjastoa käytetään käytöiittymän rakentamiseen"""
from tkinter import Tk
from paavalikko import Paavalikko
from pelinakyma import Pelinakyma

class UI:
    """
    Hallitsee käyttöliittymän näkymiä
    Attributes:
        juuri:
            tkinterin juurikomponentti
        nakyma:
            mikä näkymä käyttöliittymällä on sillä hetkellä käytössä
    """

    def __init__(self, juuri):
        """Luokan konstruktori"""

        self._juuri = juuri
        self._nakyma = None

    def kaynnista(self):
        """Määrittää mikä näkymä avataan sovelluksen käynnistyessä"""

        self._nayta_paavalikko()

    def _nayta_paavalikko(self):
        """asettaa näkymän päävalikoksi"""

        self._piiloita_nakyma()

        self._nakyma = Paavalikko(
            self._juuri,
            self._aloitus_kasittelija
        )

        self._nakyma.pakkaa()

    def _nayta_pelinakyma(self, ruudukko):
        """asettaa näkymän 15-peliksi"""

        self._piiloita_nakyma()

        self._nakyma = Pelinakyma(
            self._juuri,
            ruudukko,
            self._palaa_paavalikkoon
        )
        self._nakyma.pakkaa()

    def _palaa_paavalikkoon(self):
        """käsittelee siirtymisen päävalikkoon"""
        self._nayta_paavalikko()

    def _piiloita_nakyma(self):
        """tuhoaa senhetkisen näkymän"""

        if self._nakyma:
            self._nakyma.tuhoa()

        self._nakyma = None

    def _aloitus_kasittelija(self, ruudukko):
        """käsittelee pelin käynnistymisen annetuilla asetuksilla"""

        self._nayta_pelinakyma(ruudukko)


ikkuna = Tk()
ikkuna.title("15-peli")

ui = UI(ikkuna)
ui.kaynnista()

ikkuna.mainloop()
