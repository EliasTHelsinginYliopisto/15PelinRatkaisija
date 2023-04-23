"""Time-kirjastoa käytetään suorituksen ajastukseen"""
from time import time

class Tilasto:
    """Tilastoi ratkaisualgoritmin suoritusta ja tulostaa tietoa ratkaisun aikana
        Args:
            solmut:
                Haussa luotujen solmujen määrä
            aloitus:
                aloituksen ajankohta
            kulunut:
                kulunut aika
            syvennokset:
                haussa tehtyjen syvennökien määrä"""

    def __init__(self, kynnys):
        self.solmut = 0
        self.aloitus = time()
        self.kulunut = 0
        self.syvennokset = 0

        print("Etsitään paras ratkaisu IDA* algoritmillä")
        print("Haku aloitetaan kynnyksellä", kynnys)
        print("\n\n\n")

    def tulosta(self):
        """haun tila joka tulostetaan jatkuvasti konsoliin"""
        self.solmut += 1
        kulunut = time()-self.aloitus
        if self.kulunut+0.10 < kulunut:
            self.kulunut = kulunut
            print("\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K")
            print("Luodut solmut:", self.solmut)
            print("Kulunut aika:", round(self.kulunut,1),"s")
            print("Tehdyt syvennökset:", self.syvennokset)

    def syvennos(self, kynnys, arvio):
        """Tulostaa haun tilastot syvennöksen tapahtuessa"""
        self.syvennokset += 1
        self.kulunut = time()-self.aloitus
        print("\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K")
        print("Syvennetään hakua, aiempi kynnys:",kynnys,"Uusi kynnys:",arvio)
        print("Solmut:",self.solmut,
                "Kulunut aika:", round(self.kulunut,3),"s")
        print("\n\n\n")

    def ratkaisu(self, reitti):
        """Tulostaa haun tuloksen haun päättyessä"""
        self.kulunut = time()-self.aloitus
        print("\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K\033[1A\x1b[2K")
        print("Ratkaisu löydetty, reitti:")
        print(reitti)
        print("Haun kesto:",round(self.kulunut,3), "s",
             "\nLuodut solmut:", self.solmut,
             "\nSyvennöksien määrä:", self.syvennokset,
             "\nRatkaisun pituus:", len(reitti))
