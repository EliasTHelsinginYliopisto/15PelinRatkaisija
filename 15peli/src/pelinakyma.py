"""tkinter-moduuleja
peligeneraattoria tarvitaan satunnaisen pelin generointiin
ruudukonkäsittelijää tarvitaan siirtojen tekemiseen
algoritmiä tarvitaan ratkaisun löytämiseen"""
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


    def __init__(self, juuri, ruudukko, paavalikkokasittelija):
        """luokan konstruktori"""
        self._juuri = juuri
        self._kehys = None
        self._ruudukko = ruudukko
        self._pelikentta = []
        self._ratkaisu = []
        self.kasittelija = Ruudukonkasittelija()
        self._paavalikkokasittielija = paavalikkokasittelija
        self._alusta()

    def _alusta(self):
        """Määrittää pelinäkymän komponentit
        args:
            Generaattori: pelgeneraattori-luokka"""

        generaattori = Peligeneraattori()
        self._ruudukko = generaattori.validioi_ruudukkosyote(self._ruudukko)
        self._pelikentta = [[None for i in range(len(self._ruudukko))]
                            for j in range(len(self._ruudukko))]

        self._kehys = ttk.Frame(master=self._juuri)

        for i, rivi in enumerate(self._ruudukko):
            for j, numero in enumerate(rivi):
                self._pelikentta[i][j] = ttk.Label(master=self._kehys,
                                                text=numero,
                                                background="#717171",
                                                relief = "solid",
                                                anchor="center")

                self._pelikentta[i][j].grid(row = i+1, column = j+1, sticky = "nswe")

        self._kehys.bind("<Up>", self.tee_siirto)
        self._kehys.bind("<Down>", self.tee_siirto)
        self._kehys.bind("<Left>", self.tee_siirto)
        self._kehys.bind("<Right>", self.tee_siirto)
        self._kehys.bind("<space>", self.ratkaise)
        self._kehys.bind("<BackSpace>", self.siirry_paavalikkoon)

        self._kehys.columnconfigure(list(range(len(self._ruudukko)+2)), minsize=50, weight=1)
        self._kehys.rowconfigure(list(range(len(self._ruudukko)+2)), minsize=50,weight=1)

        self.paivita()

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

        if not siirto:
            return
        if len(self._ratkaisu) == 0:
            self.paivita()
            return
        if komento.keysym == self._ratkaisu[0]:
            self._ratkaisu = self._ratkaisu[1:]
            self.paivita()
            return

        komennot = ["Up", "Left", "Down", "Right"]
        for i, jono in enumerate(komennot):
            if jono == komento.keysym:
                self._ratkaisu.insert(0,komennot[i-2])
        self.paivita()

    def paivita(self):
        """päivittää ruudukon käyttöliittymässä"""
        for i, rivi in enumerate(self._ruudukko):
            for j, numero in enumerate(rivi):
                if numero != 0:
                    self._pelikentta[i][j].config(text = numero,
                                                    background ="#717171")
                else:
                    self._pelikentta[i][j].config(text = "",
                                                    background = "")
        if len(self._ratkaisu) > 0:
            seuraava = self.etsi_seuraava()
            self._pelikentta[seuraava[0]][seuraava[1]].config(background = "red")

    def etsi_seuraava(self):
        """Etsii ratkaisussa seuraavaksi siirrettävän ruudun kordinaatit"""
        komento = self._ratkaisu[0]
        sijainti = self.kasittelija.etsi_nolla(self._ruudukko)
        if komento == "Up":
            sijainti[0] += 1
        elif komento == "Down":
            sijainti[0] -= 1
        elif komento == "Left":
            sijainti[1] += 1
        else:
            sijainti[1] -= 1
        return sijainti

    def ratkaise(self, komento = None):
        """ratkaisee pelin tai toteuttaa ratkaisun seuraavan siirron"""
        if not self.tarkista_ratkaistavuus():
            return

        if len(self._ratkaisu) > 0:
            self.kasittelija.tee_siirto(self._ruudukko, self._ratkaisu[0])
            self._ratkaisu = self._ratkaisu[1:]
        else:
            algoritmi = Algoritmi()
            self._ratkaisu = algoritmi.ida_star(self._ruudukko)

        self.paivita()

    def siirry_paavalikkoon(self, komento = None):
        """Palauttaa näkymän päävalikoksi"""
        self._paavalikkokasittielija()

    def tarkista_ratkaistavuus(self):
        """Tarkistaa onko peli ratkaistavissa.
            Jos ei, syy tulostetaan.
        Args:
            generaattori:
                peligeneraattori-luokka
            lista:
                peliruudukko listamuodossa"""

        generaattori = Peligeneraattori()
        lista = []
        for rivi in self._ruudukko:
            for numero in rivi:
                lista.append(numero)

        if not generaattori.tarkista_ratkaistavuus(lista):
            print("Pelille ei ole ratkaisua")
            return False

        lista.pop()
        for i, numero in enumerate(lista):
            if i+1 != numero:
                return True
        print("Peli on jo ratkaistu")
        return False
