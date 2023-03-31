from tkinter import ttk, constants
from peligeneraattori import Peligeneraattori

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
        self._ruudukonkoko = 4      #len(self._ruudukko)
        self._pelikentta = [[None for i in range(self._ruudukonkoko)] 
                            for j in range(self._ruudukonkoko)]

        self._alusta()

    def _alusta(self):
        """Määrittää pelinäkymän komponentit
        args:
            Generaattori: pelgeneraattori-luokka"""


        generaattori = Peligeneraattori()
        self._ruudukko = generaattori.validioi_ruudukkosyote(self._ruudukko)

        self._kehys = ttk.Frame(master=self._juuri)

        for i in range(0, self._ruudukonkoko):
            for j in range(self._ruudukonkoko):
                self._pelikentta[i][j] = ttk.Label(master=self._kehys, width=5, text=self._ruudukko[i][j])
                self._pelikentta[i][j].grid(row = i, column = j)
        
    
    def pakkaa(self):
        """täyttää kehyksen komponenteilla"""
        self._kehys.pack(fill=constants.X)
    
    def tuhoa(self):
        """tuhoaa kehyksen"""
        self._kehys.destroy()

