"""
Ruudukonkäsittelijää kutsutaan IDA* uusia solmuja luodessa
Deepcopy kopioi matriisin rekursiivista algoritmia varten
"""
from copy import deepcopy
from siirtokasittelija import Siirtokasittelija
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
        pituus:
            pelikentän koko. huomaa että koko tarkistetaan aina, 
            4 on vain oletuspituus
    """

    def __init__(self):
        """luokan konstruktori"""

        self.komennot = ["Up", "Left", "Down", "Right"]
        self.kasittelija = None
        self.solmut = 0
        self.tilasto = None
        self.paamaara = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        self.pituus = 4

    def manhattaninetaisyydet(self, matriisi):
        """Laskee manhattanin etäisyys-heurestiikan
            Returns:
                etaisyys:
                    jokaisen ruudun manhattanin etäisyys 
                    oikeasta paikastaan"""
        etaisyys = 0
        for i, rivi in enumerate(matriisi):
            for j, numero in enumerate(rivi):
                if numero != 0:
                    etaisyys += abs(i-(numero-1)//self.pituus)
                    etaisyys += abs(j-(numero-1)%self.pituus)
        return etaisyys

    def konfliktit(self, matriisi):
        """Laskee konfliktejen määrän pelikentässä
        Args:
            rivilla:
                ruudut jotka ovat oikeilla paikoillaan tällä rivillä
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

        for i, rivi in enumerate(matriisi):
            rivilla = []
            sarakkeella = []

            for j, numero in enumerate(rivi):
                numero_r = numero
                numero_s = matriisi[j][i]

                if (numero_r-1)//self.pituus == i and numero_r != 0:
                    if len(rivilla) > 0:
                        maara += self.konfliktit_listassa(rivilla, numero_r)
                    rivilla.append(numero_r)

                if (numero_s-1)%self.pituus == i and numero_s != 0:
                    if len(sarakkeella) > 0:
                        maara += self.konfliktit_listassa(sarakkeella, numero_s)
                    sarakkeella.append(numero_s)

        return maara

    def konfliktit_listassa(self, lista, numero):
        """Laskee konfliktejen määrän annetulla numerolla ja listalla"""
        maara = 0
        for alkio in lista:
            if alkio > numero:
                maara += 1
        return maara

    def alusta_paamaara(self):
        """Selvittää mikä on matriisin ratkaisutila
        Args:
            Lista:
                ratkaisu listamuodossa
        Returns:
            paamaara
                ratkaisutila matriisimuodossa"""
        lista = list(range(1,(self.pituus)**2,1))
        lista.append(0)
        paamaara = []
        while lista:
            paamaara.append(lista[:self.pituus])
            lista = lista[self.pituus:]
        return paamaara

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

        self.pituus = len(matriisi)

        kynnys = self.manhattaninetaisyydet(matriisi) + (self.konfliktit(matriisi)*2)

        self.tilasto = Tilasto(kynnys)
        self.kasittelija = Siirtokasittelija(self.pituus)
        self.paamaara = self.alusta_paamaara()

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
