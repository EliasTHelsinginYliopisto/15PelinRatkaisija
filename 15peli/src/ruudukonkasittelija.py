"""deepcopy metodia käytetään koska siirtoa tehdessä alkuperäistä
    matriisia ei haluta muuttaa"""

class Ruudukonkasittelija:
    """Luokka joka käsittelee peliruudukon siirtoja"""

    def __init__(self):
        """konstruktori"""

    def tee_siirto(self, ruudukko, siirto):
        """metodi kopioi ruudukon ja palauttaa kopion jolle siirto on toteutettu
        args:
            n_s:
                "nollan sijainti" ruudukkomatriisissa"""
        n_s = self.etsi_nolla(ruudukko)
        if siirto == "Up" and n_s[0] < 3:
            ruudukko[n_s[0]][n_s[1]] = ruudukko[n_s[0]+1][n_s[1]]
            ruudukko[n_s[0]+1][n_s[1]] = 0
            return True
        if siirto == "Down" and n_s[0] > 0:
            ruudukko[n_s[0]][n_s[1]] = ruudukko[n_s[0]-1][n_s[1]]
            ruudukko[n_s[0]-1][n_s[1]] = 0
            return True
        if siirto == "Left" and n_s[1] < 3:
            ruudukko[n_s[0]][n_s[1]] = ruudukko[n_s[0]][n_s[1]+1]
            ruudukko[n_s[0]][n_s[1]+1] = 0
            return True
        if siirto == "Right" and n_s[1] > 0:
            ruudukko[n_s[0]][n_s[1]] = ruudukko[n_s[0]][n_s[1]-1]
            ruudukko[n_s[0]][n_s[1]-1] = 0
            return True

        return False


    def etsi_nolla(self, ruudukko):
        """Etsii nollan paikan matriisista"""

        nollasijainti = [0,0]
        for i in range(0,4):
            for j in range(0,4):
                if ruudukko[i][j] == 0:
                    nollasijainti[0] = i
                    nollasijainti[1] = j
        return nollasijainti
