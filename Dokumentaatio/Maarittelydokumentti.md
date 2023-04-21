# Määrittelydokumentti

## Projektin kieli
Toteutan projektin Pythonilla, en hallitse muita ohjelmointikieliä vertaisarviointia varten

## Projektin algoritmit ja tietorakenteet
Ratkaisualgoritmi toteutetaan IDA* algoritmillä

Heurestikkana käytetään walking distance-heurestiikkaa heurestiikka laskee jokaisen ruudun etäisyyden optimaalisesta sijainnistaan ja lisää heurstiikan arviota kahdella jokaiseen konfliktiin nähden
* konfliktilla tarkoitetaan että jos kaksi tai useampi ruutu on oikealla rivillä/sarakkeella, mutta ovat väärässä järjestyksessä, järjestyksen korjaaminen vie vähintään kaksi siirtoa

## Projektin tavoite ja algoritmin perustelu
Projektin tarkoituksena on luoda ratkaisualgoritmi 15-pelille.

valitsin IDA* algoritmin koska sitä suositeltiin materiaalissa ja se vaikuttaa olevan hyvin sovellettavissa projektia varten, vastaavia projekteja on myös luotu useampia kyseisellä algoritmillä.

## Ohjelman syötteet ja niiden käyttö
Ohjelmalle toteutetaan graafinen käyttöliittymä

### Syötteet:
* 15-pelin tilan syöttö
* 15-pelin generointi
* 15-pelin pelaaminen

### Tulosteet:
* Algoritmin simulaatio käyttöliittymässä (ratkaisu askel kerrallaan)
* Tulos siitä onnistuiko algoritmi pelin ratkaisemisessa
* Tilastoja algoritmin toteutuksesta (solmut, siirtojen määrä, kulunut aika, jne)

## Aika- ja tilavaativuudet 
Tavoitteena olisi mahdollisimman tehokas algoritmi/heurestiikka ajan ja/tai tilan käytön suhteen. 
* IDA* algoritmiä käytettäessä tilaa ei vaadita paljon ollenkaan
* aikavaatimus on tällä hetkellä O(n^k), missä k on haun syvennyksien määrä 

## Lähteet

* Tiralabra-kurssimateriaali ja esimerkkiprojektit
* Ohjelmistotekniikka 2023
* https://michael.kim/blog/puzzle
* https://www.youtube.com/watch?v=g0phuZDM6Mg
* http://kociemba.org/themen/fifteen/fifteensolver.html (vain nettisivu)
* https://en.wikipedia.org/wiki/Iterative_deepening_A*
* https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/

## Opinto-ohjelma
Tietojenkäsittelytieteen kandidaatti (TKT)

## Projektin kieli
Suomi.