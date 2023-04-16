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
    Algoritmi ..> Ruudukonkasittelija
```
Luokkakuvaus projektin tämänhetkisestä rakenteesta. Algoritmi ei ole vielä kutsuttavissa käyttöliittymästä