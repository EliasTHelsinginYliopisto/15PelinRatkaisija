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
    class Pelikasittelija{
    }
    class Siirtokasittelja{
    }
    class Algoritmi{
    }

    Paavalikko <-- UI
    Pelinakyma <-- UI
    Pelinakyma --> Pelikasittelija
    Pelikasittelija -->  Peligeneraattori
    Pelikasittelija --> Siirtokasittelja
    Pelikasittelija --> Algoritmi
    Algoritmi --> Siirtokasittelja
    Algoritmi --> Tilasto
```
## Sekvenssikaaviot
Sekvenssikaavio missä käyttäjä käynnistää pelin tyhjällä syötteellä, tekee yhden siirron ja palaa päävalikkoon. <br>
Nuolettomat yhteydet kuvaavat luokan luomista.
```mermaid
sequenceDiagram 
    participant UI
    participant Paavalikko
    participant Pelinakyma
    participant Pelikasittelija
    participant Peligeneraattori
    note over UI: Sovellus käynnistyy
    UI->Paavalikko: Paavalikko(juuri, aloitus_kasittelija)
    UI->>+Paavalikko: nakyma.pakkaa()
    note over Paavalikko,UI: Painetaan "aloita" nappia
    Paavalikko->>UI: aloituskasittelija("")
    UI ->> Paavalikko: nakyma.tuhoa()
    Paavalikko ->> Paavalikko: kehys.destroy()
    Paavalikko -->>- UI: None
    UI -> Pelinakyma: Pelinakyma(juuri, "", palaa_paavalikkoon)
    Pelinakyma -> Pelikasittelija: Pelikasittelija("",4)
    Pelikasittelija -> Siirtokasittelija: Siirtokasittelija(4)
    Pelikasittelija -> Peligeneraattori: Peligeneraattori(4)
    Pelikasittelija -> Algoritmi: Algoritmi()
    Pelikasittelija ->>+ Peligeneraattori: generaattori.validioi_ruudukkosyote(" ")
    Peligeneraattori -->>- Pelikasittelija: [[2,7,5,11]...]
    UI ->>+ Pelinakyma: nakyma.pakkaa()
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_ruudukko()
    Pelikasittelija -->- Pelinakyma: [[2,7,...]]
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_ruudukko()
    Pelikasittelija -->- Pelinakyma: [[2,7,...]]    
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_siirrot()
    Pelikasittelija -->- Pelinakyma: 0
    Pelinakyma ->>+ Pelikasittelija: kasittelija.etsi_seuraava()
    Pelikasittelija -->- Pelinakyma: False
    note over Pelinakyma,Pelikasittelija: tehdään siirto ylös
    Pelinakyma ->>+ Pelikasittelija: kasittelia.tee_ssirto('Up')
    Pelikasittelija ->>+ Siirtokasittelija: siirtaja.tee_siirto([[2,7,...]], "Up")
    Siirtokasittelija -->>- Pelikasittelija: True
    Pelikasittelija -->>- Pelinakyma: True
    Pelinakyma -->+ Pelikasittelija: kasittelija.hae_ruudukko()
    Pelikasittelija -->- Pelinakyma: [[2,7,...]]    
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_siirrot()
    Pelikasittelija -->- Pelinakyma: 1
    Pelinakyma ->>+ Pelikasittelija: kasittelija.etsi_seuraava()
    Pelikasittelija -->- Pelinakyma: False
    note over Pelinakyma,UI: Palataan päävalikkoon
    Pelinakyma ->> UI: paavalikkokasittelija()
    UI ->> Pelinakyma: nakyma.tuhoa()
    Pelinakyma ->> Pelinakyma: kehys.destroy()
    Pelinakyma -->- UI: None
    UI->Paavalikko: Paavalikko(juuri, aloitus_kasittelija)
    UI->>+Paavalikko: nakyma.pakkaa()
```
Sekvenssikaavio ratkaisualgoritmin toteutuksesta
```mermaid
sequenceDiagram 
    Pelinakyma ->>+ Pelikasittelija: kasittelija.ratkaise()
    Pelikasittelija ->>+ Algoritmi: algoritmi.ida_star([[2,7,5,11],...])
    loop Ida star haku
    Algoritmi -> Tilasto: Tilasto(42)
    Algoritmi -> Siirtokasittelija: Siirtokasittelija(4)
    loop Rekursiivinen osio
    Algoritmi ->>+ Tilasto: tilasto.tulosta()
    Tilasto -->>- Algoritmi: None
    Algoritmi ->>+ Siirtokasittelija: kasittelija.tee_siirto([[2,7,...]], "Up")
    Siirtokasittelija -->>- Algoritmi: True 
    end
    Algoritmi ->>+ Tilasto: tilasto.syvennos(54,56)
    Tilasto -->>- Algoritmi: None
    end
    Algoritmi ->>+ Tilasto: tilasto.ratkaisu(["Up", "Up"...])
    Tilasto -->>- Algoritmi: None
    Algoritmi -->>- Pelikasittelija: ["Up","Up","Down","Down"...]
    Pelikasittelija -->>- Pelinakyma: True
    Pelinakyma -->+ Pelikasittelija: kasittelija.hae_ruudukko()
    Pelikasittelija -->- Pelinakyma: [[2,7,...]]    
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_siirrot()
    Pelikasittelija -->- Pelinakyma: 1
    Pelinakyma ->>+ Pelikasittelija: kasittelija.etsi_seuraava()
    Pelikasittelija -->- Pelinakyma: [1,2]
```

Edelliset kaaviot yhdessä
```mermaid
sequenceDiagram 
    participant UI
    participant Paavalikko
    participant Pelinakyma
    participant Pelikasittelija
    participant Peligeneraattori
    UI->Paavalikko: Paavalikko(juuri, aloitus_kasittelija)
    UI->>+Paavalikko: nakyma.pakkaa()
    Paavalikko->>UI: aloituskasittelija("")
    UI ->> Paavalikko: nakyma.tuhoa()
    Paavalikko ->> Paavalikko: kehys.destroy()
    Paavalikko -->>- UI: None
    UI -> Pelinakyma: Pelinakyma(juuri, "", palaa_paavalikkoon)
    Pelinakyma -> Pelikasittelija: Pelikasittelija("",4)
    Pelikasittelija -> Siirtokasittelija: Siirtokasittelija(4)
    Pelikasittelija -> Peligeneraattori: Peligeneraattori(4)
    Pelikasittelija -> Algoritmi: Algoritmi()
    Pelikasittelija ->>+ Peligeneraattori: generaattori.validioi_ruudukkosyote(" ")
    Peligeneraattori -->>- Pelikasittelija: [[2,7,5,11]...]
    UI ->>+ Pelinakyma: nakyma.pakkaa()
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_ruudukko()
    Pelikasittelija -->- Pelinakyma: [[2,7,...]]
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_ruudukko()
    Pelikasittelija -->- Pelinakyma: [[2,7,...]]    
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_siirrot()
    Pelikasittelija -->- Pelinakyma: 0
    Pelinakyma ->>+ Pelikasittelija: kasittelija.etsi_seuraava()
    Pelikasittelija -->- Pelinakyma: False
    Pelinakyma ->>+ Pelikasittelija: kasittelia.tee_ssirto('Up')
    Pelikasittelija ->>+ Siirtokasittelija: siirtaja.tee_siirto([[2,7,...]], "Up")
    Siirtokasittelija -->>- Pelikasittelija: True
    Pelikasittelija -->>- Pelinakyma: True
    Pelinakyma -->+ Pelikasittelija: kasittelija.hae_ruudukko()
    Pelikasittelija -->- Pelinakyma: [[2,7,...]]    
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_siirrot()
    Pelikasittelija -->- Pelinakyma: 1
    Pelinakyma ->>+ Pelikasittelija: kasittelija.etsi_seuraava()
    Pelikasittelija -->- Pelinakyma: False
    Pelinakyma ->>+ Pelikasittelija: kasittelija.ratkaise()
    Pelikasittelija ->>+ Algoritmi: algoritmi.ida_star([[2,7,5,11],...])
    loop Ida star haku
    Algoritmi -> Tilasto: Tilasto(42)
    Algoritmi -> Siirtokasittelija: Siirtokasittelija(4)
    loop Rekursiivinen osio
    Algoritmi ->>+ Tilasto: tilasto.tulosta()
    Tilasto -->>- Algoritmi: None
    Algoritmi ->>+ Siirtokasittelija: kasittelija.tee_siirto([[2,7,...]], "Up")
    Siirtokasittelija -->>- Algoritmi: True 
    end
    Algoritmi ->>+ Tilasto: tilasto.syvennos(54,56)
    Tilasto -->>- Algoritmi: None
    end
    Algoritmi ->>+ Tilasto: tilasto.ratkaisu(["Up", "Up"...])
    Tilasto -->>- Algoritmi: None
    Algoritmi -->>- Pelikasittelija: ["Up","Up","Down","Down"...]
    Pelikasittelija -->>- Pelinakyma: True
    Pelinakyma -->+ Pelikasittelija: kasittelija.hae_ruudukko()
    Pelikasittelija -->- Pelinakyma: [[2,7,...]]    
    Pelinakyma ->>+ Pelikasittelija: kasittelija.hae_siirrot()
    Pelikasittelija -->- Pelinakyma: 1
    Pelinakyma ->>+ Pelikasittelija: kasittelija.etsi_seuraava()
    Pelikasittelija -->- Pelinakyma: [1,2]
    Pelinakyma ->> UI: paavalikkokasittelija()
    UI ->> Pelinakyma: nakyma.tuhoa()
    Pelinakyma ->> Pelinakyma: kehys.destroy()
    Pelinakyma -->- UI: None 
    UI->Paavalikko: Paavalikko(juuri, aloitus_kasittelija)
    UI->>+Paavalikko: nakyma.pakkaa()
```
## Tila- ja aikavaativuus

Ratkaisualgoritmin aikavaatimus on O(n^k), missä k on haun syvennyksien määrä. <br>
Aikavaativuutta on tarkemmin vaikea arvioida heurestiikan ja hakupuussa tehdyn karsinnan seurauksena. <br>
Seuraava osio antaa esimerkkejä tapauksista joiden ratkaisu on huomattavasti nopeampi, vaikka syvennöksiä tehdään enemmän.

Ratkaisualgoritmin tilavaatimus on suhteessa mitätön. Haun aikana aikaisempia tiloja ei talleneta lainkaan, eli käytetty tila ei kasva haun aikana. <br>
Haku tallentaa ainoastaan aiemmat siirrot (lista jonka pituus ei voi olla yli 80 joka on kauin mahdollinen syvyys), sekä haun lähtökohta.

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

### Logaritminen esitys edellisestä datasta
![kaavio](https://github.com/EliasTHelsinginYliopisto/15PelinRatkaisija/blob/main/Dokumentaatio/solmumaarakuvaaja.png)

Kaaviosta huomaa että eksponentiaalisen kasvun määrä vaihtelee ruudukustosta riippuen. 

Seuraavassa taulukossa on samat syötteet, mutta myös ratkaisun muuta tietoa, kuten saadun ratkaisun pituus ja haussa tehtyjen syvennöksien määrä.
Huomioi että haun kesto vaihtelee käytetyn laitteiston mukaan.

| Testattu ruudukko                     | Kesto(s)  | Solmut    | Syvennökset   | Ratkaisun pituus  |
|---------------------------------------|-----------|-----------|---------------|-------------------|
| 5,9,2,3,0,8,4,14,10,12,11,1,15,7,13,6 | 41.065    | 2921787   | 7             | 51                |
| 6,13,7,2,10,4,8,11,12,15,1,14,9,5,0,2 | 14.075    | 1039328   | 7             | 51                |
| 10,9,5,12,2,4,7,8,6,14,11,1,13,15,0,3 | 103.134   | 10002121  | 8             | 47                |
| 4,12,2,3,5,6,7,15,0,8,1,11,10,14,9,13 | 19.123    | 1898836   | 8             | 50                |
| 13,4,12,9,15,1,6,2,8,10,7,14,5,11,0,3 | 34.029    | 3426445   | 7             | 55                |

## Työn puutteet ja parannusehdotukset
- Luokkien riippuvuudet tekevät koodin muokkaamisesta monimutkaista ja hidastaisi jatkokehitystä.
- Projekti on ohjelmoitu Python-kielellä joka on tunnetusti hitaasti suoriutuva
- Algoritmin tehokkuutta voisi parantaa:
    - Vaihtaa käytettyjä datatyyppejä ja selvittää milloin kirjasto, lista, tupla tai jokin muu olisi nopeampi
    - Heurestiikkaa voi parantaa, tunnettuja parempia heurestiikkoja esimerkiksi "pattern database"-heurestiikat voivat olla projektissa käytettyä Walking Distance heurestiikkaa tehokkaampia. <br>
    Kyseiset heurestiikat kuitenkin nimensäkin mukaan käyttävät tietokantoja, joka nostaisi sovelluksen tilavaativuutta
    - Hakupuuta voisi karsia siten, että IDA* haku kävisi vähemmän aikaisempia tiloja läpi, tämäkin usein lisäisi tilavaativuutta
- Sovellus hyväksyy vain 4x4 ruudukot, sovellusta voisi laajentaa hyväksymään pienemmät ja suuremmat ruudukkokoot. Tämä on mahdollista jo suuressa osassa sovellusta ja kovakoodattuna vain käyttöliittymään

## Lähteet

- Tiralabra-kurssimateriaali ja esimerkkiprojektit
- Ohjelmistotekniikka 2023
- https://michael.kim/blog/puzzle
-  https://www.youtube.com/watch?v=g0phuZDM6Mg
- http://kociemba.org/themen/fifteen/fifteensolver.html (vain nettisivu)
-  https://en.wikipedia.org/wiki/Iterative_deepening_A*
- https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
