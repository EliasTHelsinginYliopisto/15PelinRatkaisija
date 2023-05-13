"""shuffle toimintoa käytetään satunnaisen pelin generoinnissa"""
from random import shuffle

class Peligeneraattori:
    """
    Halltsee pelikentän generointia ja siihen liittyviä funktioita
    Attributes:
        ruudukonkoko:
            peliruudukon koko
        ruutumaara:
            ruutujen määrä peliruudukossa
        joukko:
                lista pelin numeroista (4x4 ruudukossa 0-15)
    """
    def __init__(self, koko):
        self._ruudukonkoko = koko
        self._ruutuumaara = self._ruudukonkoko**2
        self._joukko = [*range(0,self._ruutuumaara,1)]

    def validioi_ruudukkosyote(self, s_ruudukko):
        """tarkistaa että syötetty ruudukko on oikeassa muodossa
        ja palauttaa sen matriisina
        args:
            l_ruudukko:
                peliruudukko listamuodossa
        returns:
            m_ruudukko:
                peliruudukko matriisisna"""
        try:
            l_ruudukko = list(s_ruudukko.split(","))
            l_ruudukko = [int(i) for i in l_ruudukko]
        except ValueError:
            m_ruudukko = self.generoi_ruudukko()
            return m_ruudukko

        if not set(l_ruudukko).issubset(self._joukko):
            m_ruudukko = self.generoi_ruudukko()
        elif not set(self._joukko).issubset(l_ruudukko):
            m_ruudukko = self.generoi_ruudukko()
        else:
            m_ruudukko = self.muunna_matriiisiksi(l_ruudukko)
        return m_ruudukko

    def generoi_ruudukko(self):
        """Generoi satunnaisen ruudukon ja palauttaa sen matriisimna
        args:
            l_ruudukko:
                peliruudukko listamuodossa
        returns:
            m_ruudukko:
                peliruudukko matriisisna"""

        l_ruudukko = self._joukko
        while True:
            shuffle(l_ruudukko)
            if not self.tarkista_ratkaistavuus(l_ruudukko):
                continue
            m_ruudukko = self.muunna_matriiisiksi(l_ruudukko)
            return m_ruudukko

    def muunna_matriiisiksi(self, l_ruudukko):
        """Muuntaa listan matriisiksi
        args:
            l_ruudukko:
                peliruudukko listamuodossa
        returns:
            m_ruudukko:
                    ruudukko matriisimuodossa"""

        m_ruudukko=[]
        while l_ruudukko != []:
            m_ruudukko.append(l_ruudukko[:self._ruudukonkoko])
            l_ruudukko = l_ruudukko[self._ruudukonkoko:]
        return m_ruudukko

    def tarkista_ratkaistavuus(self, l_ruudukko):
        """Tarkistaa onko peli ratkaistavissa,
            Jos nolla sijaitsee parillisella rivillä 
            ja konfliktien märä on parillinen tai toistenpäin,
            tila on ratkaistavissa
        Args:
            maara: 
                konfliktien määrä
            n_s:
                nollan sijainti"""
        maara = 0
        n_s = 0
        for i, numero in enumerate(l_ruudukko):
            if numero == 0:
                n_s = i
            for j in range(i):
                if numero < l_ruudukko[j] and numero != 0:
                    maara += 1

        if n_s//4%2 != maara%2:
            return True
        return False
