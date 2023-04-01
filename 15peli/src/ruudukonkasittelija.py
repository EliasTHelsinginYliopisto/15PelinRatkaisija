"""ei ulkoisia kirjastoja"""

class Ruudukonkasittelija:
    """Luokka joka käsittelee peliruudukon siirtoja"""

    def __init__(self):
        """konstruktori"""

    def tee_siirto(self, ruudukko, siirto):
        """metodi siitää ruudukkua annettuun suuntaan
        args:
            n_s:
                "nollan sijainti" ruudukkomatriisissa"""

        n_s = self.etsi_nolla(ruudukko)
        try:
            if siirto == "Up":
                ruudukko[n_s[0]][n_s[1]] = ruudukko[n_s[0]+1][n_s[1]]
                ruudukko[n_s[0]+1][n_s[1]] = 0
            elif siirto == "Down" and n_s [0] > 0:
                ruudukko[n_s[0]][n_s[1]] = ruudukko[n_s[0]-1][n_s[1]]
                ruudukko[n_s[0]-1][n_s[1]] = 0
            elif siirto == "Left":
                ruudukko[n_s[0]][n_s[1]] = ruudukko[n_s[0]][n_s[1]+1]
                ruudukko[n_s[0]][n_s[1]+1] = 0
            elif siirto == "Right" and n_s[1] > 0:
                ruudukko[n_s[0]][n_s[1]] = ruudukko[n_s[0]][n_s[1]-1]
                ruudukko[n_s[0]][n_s[1]-1] = 0

            return ruudukko

        except IndexError:
            return ruudukko

    def etsi_nolla(self, ruudukko):
        """Etsii nollan paikan matriisista"""

        nollasijainti = [0,0]
        for i in range(0,4):
            for j in range(0,4):
                if ruudukko[i][j] == 0:
                    nollasijainti[0] = i
                    nollasijainti[1] = j
        return nollasijainti
