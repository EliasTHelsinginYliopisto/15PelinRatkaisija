
class peligeneraattori:
    """
    Halltsee pelikentän generointia ja siihen liittyviä funktioita
    """

    def validioi_ruudukkosyote(self, ruudukko):
        """muuntaa syötetyn ruudukon merkkijonosta matriisiksi
        Args:
            joukko:
                lista numeroita 0-15
                """


        joukko = [range(0,15,1)]
        if not ruudukko:
            ruudukko = [
            [ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12],
            [13, 14, 15,  0]
            ]
        else:
            ruudukko = list(ruudukko.split(","))
            ruudukko = int(ruudukko)
            if len(ruudukko) != 16 or not set(ruudukko).issubset(joukko) :
                ruudukko = [
                [ 1,  2,  3,  4],
                [ 5,  6,  7,  8],
                [ 9, 10, 11, 12],
                [13, 14, 15,  0]
                ]
            else:
                ruudukko = [
                [ruudukko[0], ruudukko[1], ruudukko[2], ruudukko[3]]
                [ruudukko[4], ruudukko[5], ruudukko[6], ruudukko[7]]
                [ruudukko[8], ruudukko[9], ruudukko[10], ruudukko[11]]
                [ruudukko[12], ruudukko[13], ruudukko[14], ruudukko[15]]
                ]