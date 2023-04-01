#pylint: skip-file
import unittest
from ruudukonkasittelija import Ruudukonkasittelija

class TestRuudukonkasittelija(unittest.TestCase):
    def setUp(self):
        self.kasittelija = Ruudukonkasittelija()

    def test_siirto_muuttaa_matriisia(self):
        ruudukko1 = [
            [1,1,1,1],
            [1,1,0,1],
            [1,1,1,1],
            [1,1,1,1]
        ]
        ruudukko2 = [
            [1,1,1,1],
            [1,1,0,1],
            [1,1,1,1],
            [1,1,1,1]
        ]
        ruudukko2 = self.kasittelija.tee_siirto(ruudukko2,siirto="Down")
        self.assertNotEqual(ruudukko1, ruudukko2)

    def test_kaikki_suunnat_toimivat(self):
        ruudukko1 = [
            [1,1,1,1],
            [1,1,0,1],
            [1,1,1,1],
            [1,1,1,1]
        ]
        ruudukko2 = [
            [1,1,1,1],
            [1,1,0,1],
            [1,1,1,1],
            [1,1,1,1]
        ]
        ruudukko2 = self.kasittelija.tee_siirto(ruudukko2,siirto="Up")
        ruudukko2 = self.kasittelija.tee_siirto(ruudukko2,siirto="Down")
        ruudukko2 = self.kasittelija.tee_siirto(ruudukko2,siirto="Left")
        ruudukko2 = self.kasittelija.tee_siirto(ruudukko2,siirto="Right")
        self.assertEqual(ruudukko1, ruudukko2)


