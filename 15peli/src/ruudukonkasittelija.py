class Ruudukonkasittelija:
    """Luokka joka käsittelee peliruudukon siirtoja"""

    def __init__(self):
        pass
    
    def tee_siirto(self, ruudukko, siirto):
        ns = self.etsi_nolla(ruudukko)
        try:
            if siirto == "Up":
                ruudukko[ns[0]][ns[1]] = ruudukko[ns[0]+1][ns[1]] 
                ruudukko[ns[0]+1][ns[1]] = 0
            elif siirto == "Down" and ns [0] > 0:
                ruudukko[ns[0]][ns[1]] = ruudukko[ns[0]-1][ns[1]] 
                ruudukko[ns[0]-1][ns[1]] = 0
            elif siirto == "Left":
                ruudukko[ns[0]][ns[1]] = ruudukko[ns[0]][ns[1]+1] 
                ruudukko[ns[0]][ns[1]+1] = 0
            elif siirto == "Right" and ns[1] > 0:
                ruudukko[ns[0]][ns[1]] = ruudukko[ns[0]][ns[1]-1] 
                ruudukko[ns[0]][ns[1]-1] = 0

            return ruudukko
        
        except:
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
