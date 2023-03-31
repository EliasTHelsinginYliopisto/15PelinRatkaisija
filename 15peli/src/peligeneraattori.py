from random import shuffle

class Peligeneraattori:
    """
    Halltsee pelikentän generointia ja siihen liittyviä funktioita
    Attributes:
        joukko:
                lista numeroita 0-15
    """
    def __init__(self):
        self._joukko = [*range(0,16,1)]

    def validioi_ruudukkosyote(self, ruudukko):
        """tarkistaa että syötetty ruudukko on oikeassa muodossa
        ja palauttaa sen matriisina"""
        if ruudukko == "":
            ruudukko = self.generoi_ruudukko()
        else:
            ruudukko = list(ruudukko.split(","))
            ruudukko = int(ruudukko)
            if len(ruudukko) != 16 or not set(ruudukko).issubset(self._joukko) :
                ruudukko = self.generoi_ruudukko()
            else:
                ruudukko = self.muunna_matriiisiksi(ruudukko)
        return ruudukko
    
    def generoi_ruudukko(self):
        """Generoi satunnaisen ruudukon ja palauttaa sen matriisimna"""

        ruudukko = self._joukko
        shuffle(ruudukko)
        ruudukko = self.muunna_matriiisiksi(ruudukko)
        return ruudukko

    def muunna_matriiisiksi(self, ruudukko):
        """Muuntaa listan matriisiksi
            returns
                uusi_ruudukko:
                        ruudukko matriisimuodossa"""
        
        uusi_ruudukko=[]
        while ruudukko != []:
            uusi_ruudukko.append(ruudukko[:4])
            ruudukko = ruudukko[4:]
        return uusi_ruudukko

