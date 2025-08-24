# Repräsentation von Zahlen

## Zahlen in der Informatik
- In der Mathematik werden Zahlen als abstrakte Objekte betrachtet.
- Man unterscheidet Zahlen als Elemente verschiedener Wertemengen:
    - natürlicheZahlen,
    - ganzeZahlen,
    - reelleZahlen,
    - komplexeZahlen,
    - usw.
### Zahlen in der Informatik
- Stellenwertsysteme:
    - Dezimalsystem (Basis 10)
    - Binärsystem (Basis 2)
    - Hexadezimalsystem (Basis 16)
    - Oktalsystem (Basis 8)
#### Dezimalsystem
- Ziffern: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
-  Das Dezimalsystem verwendet als Basis die Zahl 10. Jede Ziffer D an der Stelle i hat den
 Wert $Dx10^i$.
- Jede Ziffer hat eine Position, die den Stellenwert bestimmt.
- Beispiel: $345 = 3x10^2 + 4x10^1 + 5x10^0$

#### Binärsystem/Dualsystem
 Computer-Systeme unterscheiden prinzipiell zwischen zwei elektrischen Zuständen.
- Ziffern: 0, 1
- Das Binärsystem verwendet als Basis die Zahl 2. 
- Jede Ziffer D an der Stelle $i$ hat den Wert $Dx2^i$.

- Jede Ziffer hat eine Position, die den Stellenwert bestimmt.
- Beispiel: $1011_2 = 1x2^3 + 0x2^2 + 1x2^1 + 1x2^0$ 
-  Alle positiven natürlichen Zahlen inklusive der Null können durch Folgen von Symbolen aus der Menge {0,1} repräsentiert werden. Wenn $n$ der Anzahl der Bits entspricht, ist $x_0$ das niederwertigste Bit (Least Significant Bit, LSB) und $x_{n-1}$ das höchstwertigste Bit (Most Significant Bit, MSB).

#### Umstellung von Dezimal- in Binärzahlen

- Bei der Umwandlung von Dualzahlen in Dezimalzahlen werden die Ziffern mit ihren Stellen wertigkeiten ausmultipliziert und die Ergebnisse addiert.

$10100100_2=1x2^7+1x2^5 +1x2^2 = 164_{10}$


## Operationen auf Zahlen
- Operationen eines Rechners werden aber nicht auf Werten, sondern auf Bitfolgen ausgeführt.
- 