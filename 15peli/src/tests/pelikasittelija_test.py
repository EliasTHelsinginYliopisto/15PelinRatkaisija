#pylint: skip-file
import unittest
import unittest.mock as mock
from pelikasittelija import Pelikasittelija

class TestSiirtokasittelija(unittest.TestCase):
    
    def setUp(self):
        self.kasittelija = Pelikasittelija("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0",4)
    
    def test_getterit_toimivat(self):
        siirrot = 123
        ruudukko = [[1,2],[3,0]]
        self.kasittelija._siirrot = 123
        self.kasittelija._ruudukko = [[1,2],[3,0]]

        self.assertEqual(self.kasittelija.hae_ruudukko(), ruudukko)
        self.assertEqual(self.kasittelija.hae_siirrot(), siirrot)
    
    def test_siirto_kutsutaan_oikein(self):
        valemetodi = mock.Mock()
        self.kasittelija._siirtaja.tee_siirto = valemetodi
        self.kasittelija.tee_siirto("Up")
        valemetodi.assert_called_with([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], "Up")

    def test_ratkaisu_vie_ratkaisuun_kun_ratkaisu(self):
        self.kasittelija._ratkaisu = ["Right","Down"]
        self.kasittelija.ratkaise()
        self.assertEqual(self.kasittelija._ratkaisu, ["Down"])
    
    def test_oikea_siirto_vie_ratkaisuun(self):
        self.kasittelija._ratkaisu = ["Right","Down"]
        self.kasittelija.tee_siirto("Right")
        self.assertEqual(self.kasittelija._ratkaisu, ["Down"])
    
    def test_vaara_siirto_vie_ratkaisusta(self):
        self.kasittelija._ratkaisu = ["Right","Down"]
        self.kasittelija.tee_siirto("Down")
        self.assertEqual(self.kasittelija._ratkaisu[0], "Up")
    
    def test_palauta_false_epaonnistunut_siirto(self):
        onnistui = self.kasittelija.tee_siirto("Up")
        self.assertEqual(onnistui, False)
    
    def test_ratkaisualgoritmi_kutsutaan_oikein(self):
        valeratkaisija = mock.Mock()
        self.kasittelija._ruudukko = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
        self.kasittelija._algoritmi.ida_star = valeratkaisija
        self.kasittelija.ratkaise()
        valeratkaisija.assert_called_with([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]])
    
    def test_ratkaisualgoritmia_ei_kutsuta_turhaan(self):
        valeratkaisija = mock.Mock()
        self.kasittelija._algoritmi.ida_star = valeratkaisija

        self.kasittelija._ruudukko = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        self.kasittelija.ratkaise()
        self.kasittelija._ruudukko = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 15, 14, 0]]
        self.kasittelija.ratkaise()
        valeratkaisija.assert_not_called()
    
    def test_seuraavan_koordinaatit_loytyvat(self):
        self.kasittelija._ruudukko = [[0,1],[2,3]]
        self.kasittelija._ratkaisu = ["Up"]
        vastausup = self.kasittelija.etsi_seuraava()

        self.kasittelija._ratkaisu = ["Down"]
        vastausdown = self.kasittelija.etsi_seuraava()

        self.kasittelija._ratkaisu = ["Left"]
        vastausleft = self.kasittelija.etsi_seuraava()

        self.kasittelija._ratkaisu = ["Right"]
        vastausright = self.kasittelija.etsi_seuraava()

        self.kasittelija._ratkaisu = []
        vastausnone = self.kasittelija.etsi_seuraava()

        self.assertEqual(vastausup, [1,0])
        self.assertEqual(vastausdown, [-1,0])
        self.assertEqual(vastausleft, [0,1])
        self.assertEqual(vastausright, [0,-1])
        self.assertEqual(vastausnone, False)
