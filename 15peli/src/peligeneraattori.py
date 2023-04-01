from random import shuffle

class Peligeneraattori:
    """
    Halltsee pelikentän generointia ja siihen liittyviä funktioita
    Attributes:
        joukko:
                lista numeroita 0-15
    """
    def __init__(self):
        self._ruudukonkoko = 4
        self._ruutuumaara = 2**self._ruudukonkoko
        self._joukko = [*range(0,self._ruutuumaara,1)]

    def validioi_ruudukkosyote(self, s_ruudukko):
        """tarkistaa että syötetty ruudukko on oikeassa muodossa
        ja palauttaa sen matriisina"""
        if s_ruudukko == "":
            m_ruudukko = self.generoi_ruudukko()
        else:
            l_ruudukko = list(s_ruudukko.split(","))
            l_ruudukko = int(l_ruudukko)
            if len(l_ruudukko) != 16 or not set(l_ruudukko).issubset(self._joukko) :
                m_ruudukko = self.generoi_ruudukko()
            else:
                m_ruudukko = self.muunna_matriiisiksi(l_ruudukko)
        return m_ruudukko
    
    def generoi_ruudukko(self):
        """Generoi satunnaisen ruudukon ja palauttaa sen matriisimna"""

        l_ruudukko = self._joukko
        shuffle(l_ruudukko)
        m_ruudukko = self.muunna_matriiisiksi(l_ruudukko)
        return m_ruudukko

    def muunna_matriiisiksi(self, l_ruudukko):
        """Muuntaa listan matriisiksi
            returns
                uusi_ruudukko:
                        ruudukko matriisimuodossa"""
        
        m_ruudukko=[]
        while l_ruudukko != []:
            m_ruudukko.append(l_ruudukko[:self._ruudukonkoko])
            l_ruudukko = l_ruudukko[self._ruudukonkoko:]
        return m_ruudukko
    

