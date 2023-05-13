"""tkinter-moduuleja käytetään käyttöliittymän toteutukseen
pelikäsittelijä ohjaa pelin toiminnallisuutta"""
from tkinter import ttk, constants
from pelikasittelija import Pelikasittelija

class Pelinakyma:
    """
    Hallitsee pelinäkymän käyttöliittymää
    Attributes:
        juuri:
            tkinterin juurikomponentti
        kehys:
            kehys näkymän osille(ttk-widgetit)
        pelikentta:
            pelitila käyttöliittymässä
        kasittelija:
            pelikäsittelijä-luokka
        paavalikkokäsittelija
            metodi joka palauttaa käyttöliittymän päävalikkoon"""


    def __init__(self, juuri, ruudukko, paavalikkokasittelija):
        """luokan konstruktori"""
        self._juuri = juuri
        self._kehys = None
        self._pelikentta = []
        self._kasittelija = Pelikasittelija(ruudukko, 4)
        self._paavalikkokasittielija = paavalikkokasittelija
        self._alusta()

    def _alusta(self):
        """Määrittää näkymän komponentit ja komennot
        args:
            laskuri:
                laskuri joka merkitsee tehtyjen siirtojen määrän"""

        self._kehys = ttk.Frame(master=self._juuri)
        self._pelikentta = self.alusta_pelikentta()


        self._laskuri = ttk.Label(master=self._kehys, text="Tehdyt siirrtot: 0")
        self._laskuri.grid(row=1, columnspan=99)

        self._kehys.bind("<Up>", self.tee_siirto)
        self._kehys.bind("<Down>", self.tee_siirto)
        self._kehys.bind("<Left>", self.tee_siirto)
        self._kehys.bind("<Right>", self.tee_siirto)
        self._kehys.bind("<space>", self.ratkaise)
        self._kehys.bind("<BackSpace>", self.siirry_paavalikkoon)

        self.paivita()

    def alusta_pelikentta(self):
        """Määrittää peliruudukon pelinäkymässä pelin alussa
        Args:
            ruudukko:
                pelissä käytettävä ruudukko matriisismuodossa
        Returns:
            pelikenttä:
                määritetty pelitila käyttöliittymässä"""

        ruudukko = self._kasittelija.hae_ruudukko()

        pelikentta = [[None for i in range(len(ruudukko))]
                            for j in range(len(ruudukko))]

        for i, rivi in enumerate(ruudukko):
            for j, numero in enumerate(rivi):
                pelikentta[i][j] = ttk.Label(master=self._kehys,
                                            text=numero,
                                            background="#717171",
                                            relief = "solid",
                                            anchor="center")

                pelikentta[i][j].grid(row = i+2, column = j+1, sticky = "nswe")

        self._kehys.columnconfigure(list(range(len(ruudukko)+2)), minsize=50, weight=1, pad=0)
        self._kehys.rowconfigure(list(range(len(ruudukko)+3)), minsize=50,weight=1, pad = 0)

        return pelikentta

    def paivita(self):
        """päivittää ruudukon käyttöliittymässä
        Args:
            ruudukko:
                pelissä käytettävä ruudukko matriisismuodossa
            siirrot:
                tehtyjen siirtojen määrä
            seuraava:
                ratkaisussa seuraavaksi siirrettävän ruudun kordinaatit"""
        ruudukko = self._kasittelija.hae_ruudukko()
        siirrot = self._kasittelija.hae_siirrot()
        for i, rivi in enumerate(ruudukko):
            for j, numero in enumerate(rivi):
                if numero != 0:
                    self._pelikentta[i][j].config(text = numero,
                                                    background ="#717171")
                else:
                    self._pelikentta[i][j].config(text = "",
                                                    background = "")

        self._laskuri.config(text= f"Tehdyt siirrot: {siirrot}")

        seuraava = self._kasittelija.etsi_seuraava()
        if seuraava:
            self._pelikentta[seuraava[0]][seuraava[1]].config(background = "red")


    def pakkaa(self):
        """täyttää kehyksen komponenteilla"""
        self._kehys.pack(fill=constants.X)
        self._kehys.focus_set()

    def tuhoa(self):
        """tuhoaa kehyksen"""
        self._kehys.destroy()

    def tee_siirto(self, komento):
        """suorittaa siirron ja päivittää taulukon jos siirto onnistuu"""
        siirto = self._kasittelija.tee_siirto(komento.keysym)

        if siirto:
            self.paivita()

    def ratkaise(self, komento = None):
        """kutsuu ratkaisumetodia ja päivittää näkymän jos on ratkaistavaa"""
        onnistui = self._kasittelija.ratkaise()
        if onnistui:
            self.paivita()

    def siirry_paavalikkoon(self, komento = None):
        """Palauttaa näkymän päävalikoksi"""
        self._paavalikkokasittielija()
