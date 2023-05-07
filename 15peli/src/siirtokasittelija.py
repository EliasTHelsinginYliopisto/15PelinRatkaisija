"""deepcopy metodia käytetään koska siirtoa tehdessä alkuperäistä
    matriisia ei haluta muuttaa"""

class Siirtokasittelija:
    """Luokka joka käsittelee peliruudukon siirtoja"""

    def __init__(self, pituus):
        """konstruktori"""
        self.n_s = None
        self.pituus = pituus
        self.siirot = {"Up":(1,0), "Down":(-1,0), "Left": (0,1), "Right":(0,-1)}

    def tee_siirto(self, ruudukko, siirto):
        """metodi kopioi ruudukon ja palauttaa kopion jolle siirto on toteutettu
        args:
            n_s:
                "nollan sijainti" ruudukkomatriisissa"""
        if not self.n_s:
            self.n_s = self.etsi_nolla(ruudukko)
        n_s = self.n_s
        siirrettava = [n_s[0]+self.siirot[siirto][0],n_s[1]+self.siirot[siirto][1]]

        if 0 <= siirrettava[0] < self.pituus and 0 <= siirrettava[1] < self.pituus:
            ruudukko[n_s[0]][n_s[1]] = ruudukko[siirrettava[0]][siirrettava[1]]
            ruudukko[siirrettava[0]][siirrettava[1]] = 0
            self.n_s = siirrettava
            return True
        return False



    def etsi_nolla(self, ruudukko):
        """Etsii nollan paikan matriisista"""

        nollasijainti = [0,0]
        for i, rivi in enumerate(ruudukko):
            for j, numero in enumerate(rivi):
                if numero == 0:
                    nollasijainti[0] = i
                    nollasijainti[1] = j
        return nollasijainti
