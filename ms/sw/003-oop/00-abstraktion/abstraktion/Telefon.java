
public class Telefon {
    public String marke;
    public String modell;
    public String farbe;
    public double gewicht;
    public double laenge;
    public double breite;
    public double hoehe;
    public int bauJahr;

    public void anrufen() {
        System.out.println("Ich rufe an ...");
    }

    public void smsSenden() {
        System.out.println("Ich sende eine SMS ...");
    }

    public void fotografieren() {
        System.out.println("Ich mache ein Foto ...");
    }

    public void auflegen() {
        System.out.println("Ich lege auf ...");
    }

    public void lautstaerkeAendern() {
        System.out.println("Ich erhöhe die Lautstärke ...");
    }

    public void detailsAnzeigen() {
        System.out.println("============");
        System.out.println("Marke: " + marke);
        System.out.println("Modell: " + modell);
        System.out.println("Farbe: " + farbe);
        System.out.println("============");
        System.out.println("Gewicht: " + gewicht + " g");
        System.out.println("Länge: " + laenge + " mm");
        System.out.println("Breite: " + breite + " mm");
        System.out.println("Höhe: " + hoehe + " mm");
        System.out.println("============");
        
        System.out.println("Baujahr: " + bauJahr);
    }

    public void anrufBeantworten() {
        System.out.println("Ich beantworte den Anruf ...");
    }

    public void browserOeffnen() {
        System.out.println("Ich öffne den Browser ...");
    }
    public void whatsappOeffnen() {
        System.out.println("Ich öffne WhatsApp ...");
    }

}
