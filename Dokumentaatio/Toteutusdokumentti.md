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