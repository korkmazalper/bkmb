# Java SE

## Aufgabe 1 - Zahleneigenschaften prüfen

- Schreibe ein Java-Programm, das eine ganze Zahl von der Konsole einliest. Verwende dazu die Klasse ``Scanner``
- Das Programm soll folgende Schritte ausführen:

- Eingabe:

- Fordere den Benutzer auf, eine ganze Zahl einzugeben.

- Lies die Zahl in einer Variablen ein.

- Prüfungen mit if-else-Strukturen:

--> Bestimme, ob die eingegebene Zahl positiv, negativ oder gleich null ist.

--> Bestimme, ob die Zahl gerade oder ungerade ist.

Ausgabe:

Gib die Ergebnisse in vollständigen Sätzen auf der Konsole aus.

Beispiel: „Die Zahl ist positiv und gerade.“

## Single Responsibility Principle (SRP) - Prinzip der einzigen Verantwortung

Das Single Responsibility Principle ist eines der SOLID-Prinzipien der objektorientierten Programmierung.
Es besagt:

``Eine Einheit (Klasse/Modul/Methode) sollte nur eine einzige Verantwortung haben.``

Das bedeutet, dass eine Klasse nur für eine bestimmte Aufgabe oder Funktionalität zuständig sein soll. Wenn sich eine Anforderung im Programm ändert, sollte es dadurch möglichst nur eine Klasse betreffen.

## Aufgabe 2 Gehaltsberechnung

Schreibe ein Java-Programm zur Berechnung des Nettogehalts eines Mitarbeiters.

**Anforderungen:**

Eingabe (mit Scanner):

Monatliches Bruttogehalt (double)

Steuersatz in Prozent (double)

Sozialabgaben in Prozent (double)

**Berechnung:**

Steuerbetrag = Bruttogehalt × (Steuersatz / 100)

Sozialabgaben = Bruttogehalt × (Sozialabgaben / 100)

Nettogehalt = Bruttogehalt – Steuerbetrag – Sozialabgaben

**Ausgabe:**

Bruttogehalt

Steuerbetrag

Sozialabgaben

Nettogehalt

**Beispiel:**
Eingabe: Bruttogehalt = 3000 €, Steuersatz = 20 %, Sozialabgaben = 15 %
Ausgabe:
Steuer: 600 €
Sozialabgaben: 450 €
Nettogehalt: 1950 €