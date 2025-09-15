# Vererbung

## Aufgabe

- Wähle 4 Fahrzeuge aus (z. B. Auto, Fahrrad, Motorrad, Bus, LKW).
- Welche Eigenschaften (Attribute) und Fähigkeiten (Methoden) haben diese Fahrzeuge? [Schreibe sie in Java auf]  
  [Vergiss nicht die Sichtbarkeiten (public, private, protected) sowie Getter und Setter]

| Fahrzeug     | Attribute                                                                                                   | Verhalten (Methoden)                                                                                                    |
| ------------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Auto**     | Marke, Baujahr, Anzahl der Reifen, Farbe, Geschwindigkeitslimit, Anzahl der Türen, Kraftstoffverbrauch      | starten(), bremsen(), anzeigenBasisDetails(), hupen(), anzeigenDetails()                                                |
| **Fahrrad**  | Marke, Baujahr, Anzahl der Reifen, Farbe, Geschwindigkeitslimit, Hat einen Korb (ja/nein), Anzahl der Gänge | starten(), bremsen(), anzeigenBasisDetails(), klingeln(), anzeigenDetails()                                             |
| **Motorrad** | Marke, Baujahr, Anzahl der Reifen, Farbe, Geschwindigkeitslimit, Hat Beifahrer (ja/nein), Motorleistung     | starten(), bremsen(), anzeigenBasisDetails(), gasGeben(), anzeigenDetails()                                             |
| **Bus**      | Marke, Baujahr, Anzahl der Reifen, Farbe, Geschwindigkeitslimit, Anzahl der Sitzplätze, aktuelle Fahrgäste  | starten(), bremsen(), anzeigenBasisDetails(), fahrgastEinsteigen(anzahl), fahrgastAussteigen(anzahl), anzeigenDetails() |

- Welche Eigenschaften und welches Verhalten ist gemeinsam?

## Vererbung

- Wiederverwendbarkeit von Code
- Bessere Strukturierung
- Vermeidung von Redundanzen
- `ist-ein`-Beziehung
- Vererbungshierarchie
- Erweiterbarkeit
- Polymorphie
- Wartbarkeit
- Superklasse (Basisklasse, Elternklasse)
- Subklasse (abgeleitete Klasse, Kindklasse)
