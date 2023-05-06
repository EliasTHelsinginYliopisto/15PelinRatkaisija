"""shuffle toimintoa käytetään satunnaisen pelin generoinnissa"""
from random import shuffle

class Peligeneraattori:
    """
    Halltsee pelikentän generointia ja siihen liittyviä funktioita
    Attributes:
        joukko:
                lista numeroita 0-15
    """
    def __init__(self, koko):
        self._ruudukonkoko = koko
        self._ruutuumaara = self._ruudukonkoko**2
        self._joukko = [*range(0,self._ruutuumaara,1)]

    def validioi_ruudukkosyote(self, s_ruudukko):
        """tarkistaa että syötetty ruudukko on oikeassa muodossa
        ja palauttaa sen matriisina"""
        if s_ruudukko == "":
            m_ruudukko = self.generoi_ruudukko(ratkaistava=True)
        else:
            l_ruudukko = list(s_ruudukko.split(","))
            l_ruudukko = [int(i) for i in l_ruudukko]
            if len(l_ruudukko) != self._ruutuumaara or not set(l_ruudukko).issubset(self._joukko):
                m_ruudukko = self.generoi_ruudukko(ratkaistava=True)
            else:
                m_ruudukko = self.muunna_matriiisiksi(l_ruudukko)
        return m_ruudukko

    def generoi_ruudukko(self, ratkaistava):
        """Generoi satunnaisen ruudukon ja palauttaa sen matriisimna
        Args:
            ratkaistava:
                Määrittää, pitääkö pelin olla ratkaistavissa"""

        l_ruudukko = self._joukko
        while True:
            shuffle(l_ruudukko)
            if ratkaistava:
                if not self.tarkista_ratkaistavuus(l_ruudukko):
                    continue
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
