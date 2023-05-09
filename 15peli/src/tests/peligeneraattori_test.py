#pylint: skip-file
import unittest
import unittest.mock as mock
from peligeneraattori import Peligeneraattori

class TestPeligeneraattori(unittest.TestCase):
    def setUp(self):
        self.generaattori = Peligeneraattori(4)
    
    def test_palauttaa_oikeanlaisen_matriisin(self):
        syotettava_ruudukko = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0"
        saatu_matriisi = self.generaattori.validioi_ruudukkosyote(syotettava_ruudukko)
        oikea_matriisi = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]
            ]
        self.assertEqual(saatu_matriisi, oikea_matriisi)

    def test_generoi_satunnaisen_matriisin(self):
        ei_satunnaninen_matriisi = [
            [0,1,2,3],
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,15]
            ]
        saatu_matriisi = self.generaattori.generoi_ruudukko()
        self.assertNotEqual(ei_satunnaninen_matriisi, saatu_matriisi)
    
    def test_generoi_ruudukon_virheellisella_syotteella(self):
        valegenraattori = self.generaattori.generoi_ruudukko = mock.Mock()

        virhe1 = ""
        virhe2 = "vaikea peli"
        virhe3 = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16"
        virhe4 = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,0"
        validi = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0"
        virhe5 = "a,b,c,d,e,f,g,h,i,j ,k ,l ,m ,n ,o, p"

        self.generaattori.validioi_ruudukkosyote(virhe1)
        self.generaattori.validioi_ruudukkosyote(virhe2)
        self.generaattori.validioi_ruudukkosyote(virhe3)
        self.generaattori.validioi_ruudukkosyote(validi)
        self.generaattori.validioi_ruudukkosyote(virhe4)
        self.generaattori.validioi_ruudukkosyote(virhe5)

        self.assertEqual(len(valegenraattori.mock_calls),5)


    def test_ratkaisuvuuden_tarkistus_onnistuu(self):
        testi_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0] #True
        testi_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,14,0] #False
        testi_3 = [1,10,15,4,13,6,3,8,2,9,12,7,14,5,0,11] #True
        testi_4 = [3,9,1,15,14,11,4,6,13,0,10,12,2,7,8,5] #False

        tulos_1 = self.generaattori.tarkista_ratkaistavuus(testi_1)
        tulos_2 = self.generaattori.tarkista_ratkaistavuus(testi_2)
        tulos_3 = self.generaattori.tarkista_ratkaistavuus(testi_3)
        tulos_4 = self.generaattori.tarkista_ratkaistavuus(testi_4)

        self.assertEqual(tulos_1, True)
        self.assertEqual(tulos_2, False)
        self.assertEqual(tulos_3, True)
        self.assertEqual(tulos_4, False)
    
    def test_ei_generoida_ratkaisemattomia(self):
        vastaus = []
        for i in range(10):
            vastaus = self.generaattori.generoi_ruudukko()
            lista = []
            for rivi in vastaus:
                for numero in rivi:
                    lista.append(numero)
            self.assertEqual(self.generaattori.tarkista_ratkaistavuus(lista), True)