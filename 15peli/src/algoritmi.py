from ruudukonkasittelija import Ruudukonkasittelija
class Algoritmi:

    def __init__(self):
        self.komennot = ["Up", "Left", "Down", "Right"]
        self.kasittelija = None
        self.solmut = 0
        self.oikeatpaikat = {
            1:(0,0), 2:(0,1), 3:(0,2), 4:(0,3),
            5:(1,0), 6:(1,1), 7:(1,2), 8:(1,3),
            9:(2,0), 10:(2,1), 11:(2,2), 12:(2,3),
            13:(3,0), 14:(3,1), 15:(3,2), 0:(3,3)
            }
        self.paamaara = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

    def manhattaninetaisyydet(self, matriisi):
        etaisyys = 0
        for i in range(4):
            for j in range(4):
                numero = matriisi[i][j]
                if numero != 0:
                    etaisyys += abs(i-self.oikeatpaikat[numero][0])
                    etaisyys += abs(j-self.oikeatpaikat[numero][1])
        return etaisyys

    def konfliktit(self, matriisi):
        maara = 0
        for i in range(4):
            rivilla = []
            sarakkeella = []

            for j in range(4):
                numero_r = matriisi[i][j]
                numero_s = matriisi[j][i]

                if self.oikeatpaikat[numero_r][0] == i and numero_r != 0:
                    if len(rivilla) > 0:
                        for numero in rivilla:
                            if numero > numero_r:
                                maara += 1
                    rivilla.append(numero_r)

                if self.oikeatpaikat[numero_s][1] == i and numero_s != 0:
                    if len(sarakkeella) > 0:
                        for numero in sarakkeella:
                            if numero > numero_s:
                                maara += 1
                    sarakkeella.append(numero_s)

        return maara

    def ida_star(self, matriisi):
        self.kasittelija = Ruudukonkasittelija()

        kynnys = self.manhattaninetaisyydet(matriisi) + (self.konfliktit(matriisi)*2)

        while True:
            self.solmut = 0
            arvio = self.ida_star_rekursio(matriisi=matriisi, syvyys=0,
                                            kynnys=kynnys, kielletty_k="")

            if arvio <= 0:
                return -arvio, self.solmut

            kynnys = arvio



    def ida_star_rekursio(self, matriisi, syvyys, kynnys, kielletty_k):

        self.solmut += 1

        if matriisi == self.paamaara:
            return -syvyys

        arvio = syvyys + self.manhattaninetaisyydet(matriisi) + (self.konfliktit(matriisi)*2)
        if arvio > kynnys:
            return arvio

        pienin_arvio = 999
        i = -1
        for komento in self.komennot:
            i += 1

            if komento == kielletty_k:
                continue

            seuraava = self.kasittelija.tee_siirto(matriisi, komento)

            if seuraava == matriisi:
                continue

            arvio = self.ida_star_rekursio(seuraava, syvyys+1, kynnys, self.komennot[i-2])

            if arvio < pienin_arvio:
                pienin_arvio = arvio

        return pienin_arvio
