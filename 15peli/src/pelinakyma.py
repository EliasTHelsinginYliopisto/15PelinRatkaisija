"""tkinter-moduuleja"""
from tkinter import ttk, constants
from peligeneraattori import Peligeneraattori
from ruudukonkasittelija import Ruudukonkasittelija
from algoritmi import Algoritmi

class Pelinakyma:
    """
    Hallitsee pelinäkymää
    Attributes:
        juuri:
            tkinterin juurikomponentti
        kehys:
            kehys näkymän osille
        ruudukko: 
            pelitila matriisimuodossa
        ruudukonkoko:
            pelikentän koko
        pelikenttä:
            pelitila käyttöliittymässä"""


    def __init__(self, juuri, ruudukko):
        """luokan konstruktori"""
        self._juuri = juuri
        self._kehys = None
        self._ruudukko = ruudukko
        self._ruudukonkoko = 4
        self._pelikentta = [[None for i in range(self._ruudukonkoko)]
                            for j in range(self._ruudukonkoko)]
        self._ratkaisu = []
        self.kasittelija = Ruudukonkasittelija()
        self._alusta()

    def _alusta(self):
        """Määrittää pelinäkymän komponentit
        args:
            Generaattori: pelgeneraattori-luokka"""


        generaattori = Peligeneraattori()
        self._ruudukko = generaattori.validioi_ruudukkosyote(self._ruudukko)

        self._kehys = ttk.Frame(master=self._juuri)

        for i in range(self._ruudukonkoko):
            for j in range(self._ruudukonkoko):
                if self._ruudukko[i][j] != 0:
                    self._pelikentta[i][j] = ttk.Label(master=self._kehys,
                                                    text=self._ruudukko[i][j],
                                                    background="#717171",
                                                    relief = "solid",
                                                    anchor="center")
                else:
                    self._pelikentta[i][j] = ttk.Label(master=self._kehys,
                                                    text="",
                                                    relief = "solid",
                                                    anchor="center")

                self._pelikentta[i][j].grid(row = i+1, column = j+1, sticky = "nswe")

        self._kehys.bind("<Up>", self.tee_siirto)
        self._kehys.bind("<Down>", self.tee_siirto)
        self._kehys.bind("<Left>", self.tee_siirto)
        self._kehys.bind("<Right>", self.tee_siirto)
        self._kehys.bind("<space>", self.ratkaise)

        self._kehys.columnconfigure(list(range(self._ruudukonkoko+2)), minsize=50, weight=1)
        self._kehys.rowconfigure(list(range(self._ruudukonkoko+2)), minsize=50,weight=1)

    def pakkaa(self):
        """täyttää kehyksen komponenteilla"""
        self._kehys.pack(fill=constants.X)
        self._kehys.focus_set()

    def tuhoa(self):
        """tuhoaa kehyksen"""
        self._kehys.destroy()

    def tee_siirto(self, komento):
        """suorittaa siirron ja päivittää taulukon"""
        siirto = self.kasittelija.tee_siirto(self._ruudukko, komento.keysym)
        if siirto:
            self.paivita()

    def paivita(self):
        """päivittää ruudukon käyttöliittymässä"""
        for i in range(self._ruudukonkoko):
            for j in range(self._ruudukonkoko):
                if self._ruudukko[i][j] != 0:
                    self._pelikentta[i][j].config(text = self._ruudukko[i][j],
                                                    background ="#717171")
                else:
                    self._pelikentta[i][j].config(text = "",
                                                    background = "")

    def ratkaise(self, komento = None):
        """ratkaisee pelin tai toteuttaa ratkaisun seuraavan siirron"""
        if len(self._ratkaisu) > 0:
            self.kasittelija.tee_siirto(self._ruudukko, self._ratkaisu[0])
            self.paivita()
            self._ratkaisu = self._ratkaisu[1:]
        else:
            algoritmi = Algoritmi()
            print(self._ruudukko)
            self._ratkaisu = algoritmi.ida_star(self._ruudukko)
