# Toteutusdokumentti 

## Luokkakuvaus
```mermaid
classDiagram
    class UI{
    }
    class Paavalikko{
    }
    class Pelinakyma{
    }
    class Peligeneraattori{
    }
    class Ruudukonkasittelija{
    }
    class Algoritmi{
    }

    Paavalikko <-- UI
    Pelinakyma <-- UI
    Pelinakyma ..>  Peligeneraattori
    Pelinakyma ..> Ruudukonkasittelija
    Pelinakyma ..> Algoritmi
    Algoritmi ..> Ruudukonkasittelija
    Algoritmi ..> Tilasto
```
## Sekvenssikaaviot
Sekvenssikaavio valkoissa siirtymisestä
```mermaid
sequenceDiagram 
    participant UI
    participant Paavalikko
    participant Pelinakyma
    UI->>+Paavalikko: self._nakyma.pakkaa()
    Paavalikko->>UI: self.aloituskasittelija("2,7,5,11..")
    UI ->> Paavalikko: self._nakyma.tuhoa
    Paavalikko ->>- Paavalikko: self.kehys.destroy()
    UI ->>+ Pelinakyma: self._nakyma.pakkaa()
    Pelinakyma ->> UI: self.siirry_paavalikkoon()
    UI ->> Pelinakyma: self._nakyma.tuhoa
    Pelinakyma ->>- Pelinakyma: self.kehys.destroy()
```
Sekvenssikaavio ratkaisualgoritmin toteutuksesta
```mermaid
sequenceDiagram 
    participant Pelinakyma
    participant Algoritmi
    participant Tilasto
    participant Ruudukonkasittelija

    Pelinakyma ->>+ Algoritmi: algoritmi.ida_star([[2,7,5,11],...])
    loop Ida star haku
    loop Rekursiivinen osio
    Algoritmi ->> Tilasto: tilasto.tulosta()
    Algoritmi ->>+ Ruudukonkasittelija: kasittelija.tee_siirto([[2,7,...]], "Up")
    Ruudukonkasittelija -->>- Algoritmi: True 
    end
    Algoritmi ->> Tilasto: tilasto.syvennos(54,56)
    end
    Algoritmi ->> Tilasto: tilasto.ratkaisu(["Up", "Up"...])
    Algoritmi -->>- Pelinakyma: ["Up","Up","Down","Down"...]
```
Sekvenssikaavio pelin generoimisesta ja siirron tekemisestä
```mermaid
sequenceDiagram 
    participant Pelinakyma
    participant Peligeneraattori
    participant Ruudukonkasittelija
    Pelinakyma ->>+ Peligeneraattori: generaattori.validioi_ruudukkosyote(" ")
    Peligeneraattori -->>- Pelinakyma: [[2,7,5,11]...]
    Pelinakyma ->>+ Ruudukonkasittelija: kasittelija.tee_siirto([[2,7,...]], "Up")
    Ruudukonkasittelija -->>- Pelinakyma: True
```
## Tila- ja aikavaativuus

Ratkaisualgoritmin aikavaatimus on O(n^k), missä k on haun syvennyksien määrä. <br>
Aikavaativuutta on tarkemmin vaikea arvioida heurestiikan ja hakupuussa tehdyn karsinnan seurauksena. <br>
Seuraava osio antaa esimerkkejä tapauksista joiden ratkaisu on huomattavasti nopeampi, vaikka syvennöksiä tehdään enemmän.

Ratkaisualgoritmin tilavaatimus on mitätön. Haun aikaisempia tiloja, ei talleneta lainkaan. <br>
Tallenetaan vain aiemmat siirrot (lista jonka pituus ei voi olla yli 80 joka on kauin mahdollinen syvyys), sekä haun lähtökohta.

## Suorituskyky
Seuraavassa taulukossa on muutama satunnaisesti generoitu peli, ja suorituksen aikana tullutta dataa. <br>
Ensimmäisessä sarakkessa on pelin syöte, ja lopuissa on haun syvennöksen numero, ja syvennökseen mennessä luotujen solmujen määrä.

| Testattu ruudukko                     |   1   |   2   |   3   |   4   |   5   |   6       |   7       |
|---------------------------------------|-------|-------|-------|-------|-------|-----------|-----------|
| 5,9,2,3,0,8,4,14,10,12,11,1,15,7,13,6 | 5     | 38    | 815   | 7812  | 58349 | 398316    | 2552940   |   
| 6,13,7,2,10,4,8,11,12,15,1,14,9,5,0,2 | 4     | 57    | 623   | 4038  | 25388 | 158308    | 970967    |
| 10,9,5,12,2,4,7,8,6,14,11,1,13,15,0,3 | 11    | 101   | 823   | 5676  | 33558 | 188420    | 999663    |
| 4,12,2,3,5,6,7,15,0,8,1,11,10,14,9,13 | 5     | 43    | 221   | 1330  | 7954  | 48560     | 298406    |
| 13,4,12,9,15,1,6,2,8,10,7,14,5,11,0,3 | 7     | 46    | 508   | 4430  | 34366 | 254685    | 1802658   |

Seuraavassa taulukossa on samat syötteet, mutta myös ratkaisun muuta tietoa, kuten saadun ratkaisun pituus ja haussa tehtyjen syvennöksien määrä.
Huomioi että haun kesto vaihtelee käytetyn laitteiston mukaan.

| Testattu ruudukko                     | Kesto(s)  | Solmut    | Syvennökset   | Ratkaisun pituus  |
|---------------------------------------|-----------|-----------|---------------|-------------------|
| 5,9,2,3,0,8,4,14,10,12,11,1,15,7,13,6 | 41.065    | 2921787   | 7             | 51                |
| 6,13,7,2,10,4,8,11,12,15,1,14,9,5,0,2 | 14.075    | 1039328   | 7             | 51                |
| 10,9,5,12,2,4,7,8,6,14,11,1,13,15,0,3 | 103.134   | 10002121  | 8             | 47                |
| 4,12,2,3,5,6,7,15,0,8,1,11,10,14,9,13 | 19.123    | 1898836   | 8             | 50                |
| 13,4,12,9,15,1,6,2,8,10,7,14,5,11,0,3 | 34.029    | 3426445   | 7             | 55                |

