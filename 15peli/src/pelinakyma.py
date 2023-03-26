from tkinter import ttk, constants

class Pelinakyma:
    """
    Hallitsee pelinäkymää
    Attributes_:
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
        """Määrittää pelinäkymän komponentit"""
        self.validioi_ruudukko()

        self._kehys = ttk.Frame(master=self._juuri)

        for i in range(0, self._ruudukonkoko):
            for j in range(self._ruudukonkoko):
                self._pelikentta[i][j] = ttk.Label(master=self._kehys, width=5, text=str("temp")) #self._ruudukko[i][j]
                self._pelikentta[i][j].grid(row = i, column = j)
        
    
    def pakkaa(self):
        """täyttää kehyksen komponenteilla"""
        self._kehys.pack(fill=constants.X)
    
    def tuhoa(self):
        """tuhoaa kehyksen"""
        self._kehys.destroy()

    def validioi_ruudukko(self):
        """muuntaa syötetyn ruudukon merkkijonosta matriisiksi"""
        if not self._ruudukko:
            self._ruudukko = [
            [ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12],
            [13, 14, 15,  0]
            ]