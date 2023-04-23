## Asennus
siiry kansioon */15peli

Lataa riippuvuudet:

1.
```
poetry install
```
2.
```
poetry run invoke build
```
## Käynnistys
Projektissa on invoke käytössä
```
poetry run invoke start
```
## Käyttöohje
* Voit aloittaa pelin painamalla "Aloita"-painiketta
* Voit aloittaa omalla syötteellä kirjoittamalla sen kenttään. Tyhjä ruutu merkitään nollalla

Esimerkki poikeanmuotoisesta kenttäsyötteestä:
```
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0
```
* Pelinäkymässä ruudukkoa siirretään nuolinäppäimillä
* Voit aloittaa ratkaisijan painamalla välilyöntiä
* Kun ratkaisu on löydetty, voit tehdä ratkaisun siirrot painamalla välilyöntiä

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