## Testikattavuusraportti
![Raportti](https://github.com/EliasTHelsinginYliopisto/15PelinRatkaisija/blob/main/Dokumentaatio/testikattavuusraportti.png)

Testikattavuus ei sisällä käyttöliittymää (eli luokkia UI, Paavalikko, Pelinakyma) tai Tlasto-luokkaa

## Algoritmin testaus
### Heurestiikka:
- Manhattaninetäisyyttä on testattu etäisyydellä 0 ja 58.
    - Testaus on suppeaa koska heurestiikka on yksinkertainen ja jos jokin menee pieleen se todennäköisesti rikkoo yksinkertaisetkin testit
- Lineaarisia konflikteja on testattu tarkistamalla että konflikti löytyy jokaiselta riviltä ja sarakkeelta, sekä useampi konflikti löytyy jos niitä on useampi samalla rivillä
    - Linaariset konflitit perustuvat näihin havantoihin, siksi niitä on testattu
### IDA* haku:
Koko algoritmin oikeellisuutta testataan kolmella testillä:
- Ensimmäinen testi tarkistaa että ratkaisun pituus oon nolla valmiilla syötteellä
- Toinen testi tarkistaa että ratkaisun pituus on oikea ratkaisussa jossa joudutaan liikkua jokaiseen suuntaan
- Kolmas testi tarkistaa että ratkaisun pituus on oikea ratkaisussa jonka suvyyden tiedetään olevan 35

Testit saattavat vaikutaa suppealta, mutta useampi testi ei mielestäni todistaisi algoritmin oikeellisuutta enempää. Kokemuksen perusteella pieni virhe heurestiikassa sekoittaa koko algoritmin.

## Generaattorin testaus
- On testattu että generaattori hyväksyy oikeanmuotoisen syötteen
- On testattu että generaattori onnistuu generoimaan satunnaisen ruudukon
- On testattu että virheelliset syötteet eivät mene läpi erinlaisilla esimerkeillä
- On testattu että ratkaistaviiden tarkistus on oikeellinen kahdella yksinkertaisella ja monimutkaisella syötteellä
- On myös tarkistettu että generaattori ei generoi ratkaisemattomia pelejä.
    - Tämä testi ei ole täydellinen koska se voi mennä virheellisesti läpi erittäin pienellä todennäköisyydellä, sekä käyttää tarkistukseen metodia joka on testissä testattavana

## Siirtäjän testaus
- On testattu että siirto muokkaa matriisia jokaisella suunnalla 
- On testattu että siirtäjä hyväksyy hyväksyttävät siirrot
- On testattu että siirtäjä ei tee siirtoja peliruudukon ulkopuolelle

## Pelikäsittelijän testaus
Käsitteljä on rajapinta käyttöliittymän ja sovelluksen toimintojen välillä, ja sen testit tarkistavat että metodit välittävät oikeata tietoa

## Testauksen toistaminen

Testit voi suorittaa komennolla:
```
poetry run invoke test
```
Voit laatia testikattavuusraportin
```
poetry run invoke coverage-report
```
Testikattavuusraportti luodaan kohteeseen */15peli/htmlcov/index.html