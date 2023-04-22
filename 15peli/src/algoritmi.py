"""
Ruudukonkäsittelijää kutsutaan IDA* uusia solmuja luodessa
Deepcopy kopioi matriisin rekursiivista algoritmia varten
"""
from copy import deepcopy
from ruudukonkasittelija import Ruudukonkasittelija
from tilasto import Tilasto

class Algoritmi:
    """
    Sisältää pelin ratkaisualgoritmin 
    ja heurestikkaa laskevat metodit
    Attributes:
        komennot:
            Komennot joilla ruudukonkäsittelijän tee_siirto() metodia
            kutsutaan. Huomaa että vastakkaiset komennot ovat kahden
            indeksin etäisyydessä toisistaan. Tätä käytetään 
            kiellettyjen komentojen määrittämisessä
        kasittelija:
            ruudukonkäsittelijä-luokka
        solmut:
            ratkaisijan luomien solmujen määrä
        tilasto:
            tilasto-luokka
        paamaara:
            pelin lopputila
    """

    def __init__(self):
        """luokan konstruktori"""

        self.komennot = ["Up", "Left", "Down", "Right"]
        self.kasittelija = Ruudukonkasittelija()
        self.solmut = 0
        self.tilasto = None
        self.paamaara = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

    def manhattaninetaisyydet(self, matriisi):
        """Laskee manhattanin etäisyys-heurestiikan
            Returns:
                etaisyys:
                    jokaisen ruudun manhattanin etäisyys 
                    oikeasta paikastaan"""
        etaisyys = 0
        for i in range(4):
            for j in range(4):
                numero = matriisi[i][j]
                if numero != 0:
                    etaisyys += abs(i-(numero-1)//4)
                    etaisyys += abs(j-(numero-1)%4)
        return etaisyys

    def konfliktit(self, matriisi):
        """Laskee konfliktejen määrän
        Args:
            rivilla:
                ruudut jotka ovat oikeilla paikoillaan tällä tivillä
            sarakkeella:
                ruudut jotka ovat oikealla paikallaan tällä 
                sarakkeella
            numero_r:
                seuraava numero tällä rivillä
            numero_s:
                seuraava numero tällä sarakkeella
        Returns:
            maara:
                konfliktejen määrä"""

        maara = 0
        for i in range(4):
            rivilla = []
            sarakkeella = []

            for j in range(4):
                numero_r = matriisi[i][j]
                numero_s = matriisi[j][i]

                if (numero_r-1)//4 == i and numero_r != 0:
                    if len(rivilla) > 0:
                        for numero in rivilla:
                            if numero > numero_r:
                                maara += 1
                    rivilla.append(numero_r)

                if (numero_s-1)%4 == i and numero_s != 0:
                    if len(sarakkeella) > 0:
                        for numero in sarakkeella:
                            if numero > numero_s:
                                maara += 1
                    sarakkeella.append(numero_s)

        return maara

    def ida_star(self, matriisi):
        """IDA* algoritmin päämetodi
        Args: 
            kynnys:
                Laskettu heurestiikka. jos ratkaisua ei löydy 
                heurestiikalla, kynnystä nostetaan löydetyksi 
                pienimmäksi arvioksi
        Returns:
            arvio:
                Senhetkinen arvio oikean ratkaisun syvyydestä.
                jos arvio <= 0, ratkaisu on löydetty ja arvion 
                itseisarvo on vaadittujen askelten määrä"""

        kynnys = self.manhattaninetaisyydet(matriisi) + (self.konfliktit(matriisi)*2)

        self.tilasto = Tilasto(kynnys)

        while True:

            reitti = ["start"]
            matriisi_kopio = deepcopy(matriisi)

            arvio = self.ida_star_rekursio(matriisi_kopio, 0, kynnys, reitti)

            if arvio <= 0:
                reitti = reitti[1:]
                self.tilasto.ratkaisu(reitti)
                return reitti

            self.tilasto.syvennos(kynnys, arvio)
            kynnys = arvio

    def ida_star_rekursio(self, matriisi, syvyys, kynnys, reitti):
        """IDA* agoritmin rekirsiivinen metodi
        Args:
            matriisi:
                ruudukon tila tässä rekursiivisessa askeleessa
            kynnys:
                raja haun yhteisille siirroille
            kielletty_k
                komento joka siirtäisi matriisin edelliseen tilaan
                ja kyseisestä syystä ohitetaan
        Returns
            arvio:
                heurestinen arvio jäljellä olevien siirtojen määrästä
            syvyys:
                haun tämänhetkinen syvyys
            pienin_arvio:
                pienin arvio joka on rekursiivisesti löydetty
                aluksi asetettu mahdottoman suureksi"""

        self.tilasto.tulosta()

        if matriisi == self.paamaara:
            return -syvyys

        arvio = syvyys + self.manhattaninetaisyydet(matriisi) + (self.konfliktit(matriisi)*2)
        if arvio > kynnys:
            return arvio

        pienin_arvio = 999
        edellinen_k = reitti[-1]

        for i in range(4):

            if self.komennot[i-2] == edellinen_k:
                continue

            siirto = self.kasittelija.tee_siirto(matriisi, self.komennot[i])

            if siirto:
                reitti.append(self.komennot[i])

                arvio = self.ida_star_rekursio(matriisi, syvyys+1, kynnys, reitti)

                if arvio <= 0:
                    return arvio

                self.kasittelija.tee_siirto(matriisi, self.komennot[i-2])

                reitti.pop()

                if arvio < pienin_arvio:
                    pienin_arvio = arvio

        return pienin_arvio
