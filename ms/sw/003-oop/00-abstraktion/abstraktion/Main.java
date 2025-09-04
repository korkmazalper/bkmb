public class Main {
    public static void main(String[] args) {
        Telefon telefon = new Telefon();
        telefon.marke = "Samsung";
        telefon.modell = "Galaxy S21";
        telefon.farbe = "Phantom Gray";
        telefon.gewicht = 169;
        telefon.laenge = 151.7;
        telefon.bauJahr = 2021;
        telefon.anrufen();
        telefon.detailsAnzeigen();
        telefon.browserOeffnen();
        
    }
}
