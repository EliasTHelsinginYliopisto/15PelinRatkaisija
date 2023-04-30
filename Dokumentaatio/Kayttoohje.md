## Asennus
1.
siiry kansioon */15peli

2.

Lataa riippuvuudet:

```
poetry install
```
## Käynnistys
Projektissa on invoke käytössä
```
poetry run invoke start
```
## Käyttöohje

### Päävalikko
* Voit aloittaa pelin painamalla "Aloita"-painiketta
* Voit aloittaa omalla syötteellä kirjoittamalla sen kenttään. Tyhjä ruutu merkitään nollalla

Esimerkki poikeanmuotoisesta kenttäsyötteestä:
```
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0
```
* Tyhjä syötekenttä generoi pelin
### Pelinäkymä
* Ruudukkoa siirretään nuolinäppäimillä
* Voit aloittaa ratkaisijan painamalla välilyöntiä
* Kun ratkaisu on löydetty, voit tehdä ratkaisun siirrot painamalla välilyöntiä, tai tekemällä siirrot itse nuolinäppäimillä
* Palaa takaisin päävalikkoon askelpalauttimella

## Testaus
Voit suorittaa testit komennolla:
```
poetry run invoke test
```
Voit laatia testikattavuusraportin
```
poetry run invoke coverage-report
```
Testikattavuusraportti luodaan kohteeseen */15peli/htmlcov/index.html

## Pylint

Käynnistä koodianalyysi:
```
poetry run invoke lint
```