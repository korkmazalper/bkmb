# Loesungen
```java
package zahlenespruefen;
import java.util.Scanner;

public class Zahleneigenschaften {
    public static void main(String[] args) throws Exception {
        int zahl=getTheNumber();
        String theTypeOfTheNumber= isPositive(zahl);		
        String evenOrNot= isEven(zahl);
        System.out.println("Die Zahl ist " + theTypeOfTheNumber + " und " + evenOrNot + ".");
    }
    
    public static String isEven(int x) {
    	return x%2 == 0 ? "even":"odd";
    }
    
    public static int getTheNumber() throws Exception {
    	Scanner sc = new Scanner(System.in);
        System.out.print("Bitte geben Sie eine ganze Zahl ein: ");
        if (!sc.hasNextInt()) {
            System.out.println("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.");
            sc.close();
            throw new Exception("Ungültige Eingabe !! ");        
        }
        int zahl = sc.nextInt();
        sc.close();
        return zahl;
    }
    public static String isPositive(int x) {
    	String signAsText;
        if (x > 0) {
            signAsText = "positiv";
        } else if (x < 0) {
            signAsText = "negativ";
        } else {
            signAsText = "gleich null";
        }
        return signAsText;
    }
}
```

## SRP nicht umgesetzt

```java
import java.util.Scanner;

public class Gehaltsberechnung {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Bitte geben Sie Ihr Bruttogehalt ein: ");
        double brutto = sc.nextDouble();

        System.out.print("Bitte geben Sie den Steuersatz in % ein: ");
        double steuerSatz = sc.nextDouble();

        System.out.print("Bitte geben Sie die Sozialabgaben in % ein: ");
        double sozialSatz = sc.nextDouble();

        double steuerBetrag = brutto * (steuerSatz / 100);
        double sozialBetrag = brutto * (sozialSatz / 100);
        double netto = brutto - steuerBetrag - sozialBetrag;

        System.out.println("Bruttogehalt: " + brutto + " €");
        System.out.println("Steuer: " + steuerBetrag + " €");
        System.out.println("Sozialabgaben: " + sozialBetrag + " €");
        System.out.println("Nettogehalt: " + netto + " €");

        sc.close();
    }
}

```