# Vererbung

## Aufgabe

- Wähle 4 Fahrzeuge aus (z. B. Auto, Fahrrad, Motorrad, Bus, LKW).
- Welche Eigenschaften (Attribute) und Fähigkeiten (Methoden) haben diese Fahrzeuge? [Schreibe sie in Java auf]  
  [Vergiss nicht die Sichtbarkeiten (public, private, protected) sowie Getter und Setter]

| Fahrzeug     | Attribute                                                                                                   | Verhalten (Methoden)                                                                                                    |
| ------------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Auto**     | Marke, Baujahr, Anzahl der Reifen, Farbe, Geschwindigkeitslimit, Anzahl der Türen      | starten(), bremsen(), hupen(), anzeigenDetails()                                                |
| **Fahrrad**  | Marke, Baujahr, Anzahl der Reifen, Farbe, Geschwindigkeitslimit, Hat einen Korb (ja/nein), Anzahl der Gänge | starten(), bremsen(), klingeln(), anzeigenDetails()                                             |
| **Motorrad** | Marke, Baujahr, Anzahl der Reifen, Farbe, Geschwindigkeitslimit, Motorleistung     | starten(), bremsen(), gasGeben(), anzeigenDetails()                                             |
| **Bus**      | Marke, Baujahr, Anzahl der Reifen, Farbe, Geschwindigkeitslimit, Anzahl der Sitzplätze, aktuelle Fahrgäste  | starten(), bremsen(), gasGeben() |

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

````java
package tiere;

public class Tier {
	public String name;
	public int alter;
	public int gewicht;
	
	public void bewegen() {
		//.....
	}
	public void fressen(){
		//...
	}
	//getter und setter Methode
	
}
package tiere;

public class Fisch  extends Tier{

	public String lebenIn;
	
	public void schwimmen() {
		
	}
	//getter und setter methode
}
package tiere;

public class SaugeTier  extends Tier{
	public String fellFarbe;
	
	public void zeigeLaufen() {
		
	}
	
	//getter und setter methode

}
package tiere;

public class Vogel extends Tier {
	public int maxFlugHoehe;
	public void zeigeZiel() {
		//....
	}
	//getter und setter methode
}

```
