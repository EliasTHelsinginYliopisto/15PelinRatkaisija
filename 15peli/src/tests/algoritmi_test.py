#pylint: skip-file
import unittest
from algoritmi import Algoritmi

class TestAlgoritmi(unittest.TestCase):
    def setUp(self):
        self.algoritmi = Algoritmi()
    
    def test_palauttaa_oikean_etaisyyden_0(self):
        matriisi = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]
            ]
        etaisyys = self.algoritmi.manhattaninetaisyydet(matriisi)
        self.assertEqual(etaisyys, 0)
    
    def test_palauttaa_oikean_etaisyyden_max(self):
        matriisi = [
            [0,15,14,13],
            [12,11,10,9],
            [8,7,6,5],
            [4,3,2,1]
            ]
        etaisyys = self.algoritmi.manhattaninetaisyydet(matriisi)
        self.assertEqual(etaisyys, 58)
    
    def test_ratkaisu_löytyy_valmiilla_pelillä(self):
        matriisi = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]
            ]
        syvyys, reitti = self.algoritmi.ida_star(matriisi)

        self.assertEqual(syvyys, 0)
        self.assertEqual(syvyys+1, len(reitti))
    
    def test_ratkaisu_löytyy_yksinkertaisella_pelillä(self):
        matriisi = [
            [2,3,4,8],
            [1,6,7,12],
            [5,10,11,0],
            [9,13,14,15]
            ]
        syvyys, reitti = self.algoritmi.ida_star(matriisi)

        self.assertEqual(syvyys, 11)
        self.assertEqual(syvyys+1, len(reitti))

    def test_ratkaisu_löytyy_syvyys_35(self):
        matriisi = [
        [1,10,15,4],
        [13,6,3,8],
        [2,9,12,7],
        [14,5,0,11]
        ]
        syvyys, reitti= self.algoritmi.ida_star(matriisi)

        self.assertEqual(syvyys, 35)
        self.assertEqual(syvyys+1, len(reitti))
    
    def test_ei_virhellisiä_konflikteja(self):
        matriisi = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]
            ]
        maara = self.algoritmi.konfliktit(matriisi)

        self.assertEqual(maara, 0)

    def test_konfliktit_loytyvat(self):
        matriisi = [
        [1,10,15,4],
        [13,6,3,8],
        [2,9,12,7],
        [14,5,0,11]
        ]
        maara = self.algoritmi.konfliktit(matriisi)

        self.assertEqual(maara, 2)