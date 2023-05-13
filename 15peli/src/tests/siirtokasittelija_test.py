#pylint: skip-file
import unittest
from siirtokasittelija import Siirtokasittelija

class TestSiirtokasittelija(unittest.TestCase):
    def setUp(self):
        self.kasittelija = Siirtokasittelija(pituus=4)

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
        self.kasittelija.tee_siirto(ruudukko2,siirto="Down")
        self.assertNotEqual(ruudukko1, ruudukko2)
        self.kasittelija.tee_siirto(ruudukko2,siirto="Up")
        self.assertEqual(ruudukko1, ruudukko2)
        self.kasittelija.tee_siirto(ruudukko2,siirto="Left")
        self.assertNotEqual(ruudukko1, ruudukko2)
        self.kasittelija.tee_siirto(ruudukko2,siirto="Right")
        self.assertEqual(ruudukko1, ruudukko2)

    def test_kaikki_suunnat_toimivat(self):
        ruudukko2 = [
            [1,1,1,1],
            [1,1,0,1],
            [1,1,1,1],
            [1,1,1,1]
        ]
        siirto1 = self.kasittelija.tee_siirto(ruudukko2,siirto="Up")
        siirto2 = self.kasittelija.tee_siirto(ruudukko2,siirto="Down")
        siirto3 = self.kasittelija.tee_siirto(ruudukko2,siirto="Left")
        siirto4 = self.kasittelija.tee_siirto(ruudukko2,siirto="Right")
        self.assertEqual(siirto1, True)
        self.assertEqual(siirto2, True)
        self.assertEqual(siirto3, True)
        self.assertEqual(siirto4, True)

    def test_siirrot_kielletaan(self):
        ruudukko2 = [
            [0,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]
        ]
        ruudukko1 = [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,0]
        ]
        siirto1 = self.kasittelija.tee_siirto(ruudukko1,siirto="Up")
        siirto3 = self.kasittelija.tee_siirto(ruudukko1,siirto="Left")
        self.kasittelija.n_s = None
        siirto2 = self.kasittelija.tee_siirto(ruudukko2,siirto="Down")
        siirto4 = self.kasittelija.tee_siirto(ruudukko2,siirto="Right")
        self.assertEqual(siirto1, False)
        self.assertEqual(siirto2, False)
        self.assertEqual(siirto3, False)
        self.assertEqual(siirto4, False)

