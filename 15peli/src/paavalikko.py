from tkinter import ttk, constants

class Paavalikko:
    """
    Hallistee päävalikkonäkymää
    Attributes:
        juuri:
            tkinterin juurikomponentti
        kehys:
            näkymän osien kehys
        aloituskäsittelijä:
            ylemmän luokan funktio pelin aloittamiselle
        kenttä:
            syöttökenttä pelitilalle
    """

    def __init__(self, juuri, aloituskasittelija):
        """luokan Konstruktori"""

        self._juuri = juuri
        self._kehys = None
        self._aloituskasittelija = aloituskasittelija
        self._kentta = None

        self._alusta()
    
    def pakkaa(self):
        """täyttää kehyksen komponenteilla"""
        self._kehys.pack(fill=constants.X)
    
    def tuhoa(self):
        """Tukoaa kehyksen"""
        self._kehys.destroy()
    
    def _alusta(self):
        """Määrittää valikon komponentit
            Args:
                teksti:
                    valikon otsikko
                aloita_nappi:
                    nappi joka aloittaa pelin
                itsegeneroitu:
                    valinta generoiko sovellus pelin
                ratkaistava:
                    valinta joka varmistaa että peli on ratkaistavissa"""
        self._kehys = ttk.Frame(master=self._juuri)

        teksti = ttk.Label(master=self._kehys, text="15-peli")
        self._kentta = ttk.Entry(
            master=self._kehys)
        aloita_nappi = ttk.Button(
            master = self._kehys, 
            text="Aloita",
            command= self._aloita_peli 
        )
        itsegeneroitu = ttk.Checkbutton(master = self._kehys, text= "Generoi peli")
        ratkaistava = ttk.Checkbutton(master = self._kehys, text= "Generoi ratkaistava")

        teksti.grid(row=0, column=0)
        self._kentta.grid(row=1, column=0)
        aloita_nappi.grid(row=2, column=0)
        itsegeneroitu.grid(row=3, column=0)
        ratkaistava.grid(row=3, column=1)

    def _aloita_peli(self):
        """Metodi joka kutsuu aloituskäsittelijää"""
        self._aloituskasittelija(self._kentta.get())