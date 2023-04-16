#pylint: skip-file
import unittest
from peligeneraattori import Peligeneraattori

class TestPeligeneraattori(unittest.TestCase):
    def setUp(self):
        self.generaattori = Peligeneraattori()
    
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
    
