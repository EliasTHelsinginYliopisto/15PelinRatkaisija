# Viiko 4

[Tuntiraportti](https://github.com/EliasTHelsinginYliopisto/15PelinRatkaisija/blob/main/Dokumentaatio/Tuntiraportti.md)

## Mitä tehty tällä viikolla
* Ratkaisualgoritmi on luotu ja sen aikavaatimus on tehostettu tyydyttäväksi 
    * ratkaisee testauksessa käytettyä 35 askeleen ratkaisun 0.6 sekunnissa

## Edistyminen

## Mitä olen oppinut
* olen oppinut soveltamaan IDA* algoritmiä projektiin
* olen kehittänyt ongelmanratkaisutaitojani ohjelmoidessa ja kykyäni ohjelmoida rekursiivisiä algoritmejä

## Ongelmat/Kysymykset/Vaikeudet
* Alkuperäinen ratkaisualgoritmi ei kyennyt ratkaisemaan peliä kohtuullisessa ajassa, algoritmiä on tehostettu seuraavasti:
    * Manhattanin etäisyys-heurestiikka on muutettu Walking distance-heurestiikaksi
    * jos siirto ei muuta peliruudukkoa, siirolle ei toteuteta rekursiota
    * Ratkaisija ei toteuta siirtoja joiden tila on sama kuin edellinen solmu
* Konfliktit laskeva metodi ei ole selkeä
* siirtojen tekeminen on hidasta koska matriisista pitää aina tehdä kopio   


## Mitä seuraavaksi
- Algoritmin liittäminen käyttöliittymään
- Algoritmin testausta
- Metodin luominen, joka tarkistaa onko pelitila ratkaistavissa
- Algoritmin muokkaaminen siten että se palauttaa kuljetun reitin

