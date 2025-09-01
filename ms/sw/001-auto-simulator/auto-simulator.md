# Driving Simulation Lab
## Szenario:

Wir möchten eine Fahrsimulation erstellen. Der Benutzer soll auf dem Bildschirm ein Armaturenbrett (Dashboard) sehen und dort den Motor ein- oder ausschalten, den Gang wechseln, das Auto beschleunigen oder bremsen können.
## Anforderungen:
Schreiben Sie ein Java-Programm, das die folgenden Funktionen umsetzt:

### Armaturenbrett (Dashboard)

Zeigen Sie die aktuelle Geschwindigkeit (speed), den Motorstatus (isEngineOn) und den Gang (gear) an.

Bieten Sie ein Menü mit folgenden Optionen an:

+ Motor ein-/ausschalten

+ Gang wechseln (P, D, R)

+ Beschleunigen

+ Bremsen

+ Beenden

### Motorsteuerung

- Der Benutzer soll den Motor ein- und ausschalten können.

- Wenn der Motor ausgeschaltet ist, darf weder beschleunigt noch gebremst werden.

### Gangwechsel

- Der Benutzer kann zwischen den Gängen P, D und R wählen.

- Im Gang P darf keine Beschleunigung möglich sein.

### Beschleunigen (Accelerate)

- Wenn der Motor läuft und der Gang D oder R ist, soll die Geschwindigkeit um 10 km/h erhöht werden.

- Wenn die Bedingungen nicht erfüllt sind, soll eine entsprechende Fehlermeldung erscheinen.

### Bremsen (Brake)

- Wenn der Motor läuft und die Geschwindigkeit > 5 ist, soll die Geschwindigkeit um 5 km/h reduziert werden.

- Andernfalls soll eine Meldung erscheinen, dass Bremsen nicht möglich ist.

### Beenden (Exit)

Wenn der Benutzer die Option 5 wählt, soll die Simulation ordentlich beendet werden.

## Hinweise 💡

- Verwenden Sie die Klasse Scanner, um Benutzereingaben einzulesen.

- Nutzen Sie switch-case, um die Menüauswahl zu verarbeiten.

- Verwenden Sie static Variablen (z. B. speed, gear, isEngineOn), um den Zustand des Autos zu speichern.

- Mit if-else können Sie die Regeln für Beschleunigen und Bremsen prüfen.