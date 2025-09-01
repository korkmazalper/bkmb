import java.util.Scanner;

public class DrivingSimulator {

    // Aktueller Gang des Fahrzeugs (P = Park, D = Drive, R = Rückwärts)
    public static String gear = "P";

    // Aktuelle Geschwindigkeit in km/h
    public static int speed = 0;

    // Motorstatus: true = an, false = aus
    public static boolean isEngineOn = false;

    // Scanner für Benutzereingaben
    public static Scanner keyBoard = new Scanner(System.in);

    // Startet die Simulation mit einem Menü
    public static void startSimulation() {
        boolean displayMenu = true;
        while (displayMenu) {
            displayDashboard();   
            int choice = getUserChoice(); 
            processChoice(choice); 
            System.out.println();
        }
    }

    // Zeigt das Dashboard und das Menü an
    public static void displayDashboard() {
        System.out.println("------ Armaturenbrett ------");
        System.out.println("Geschwindigkeit: " + speed);
        System.out.println("Motor: " + (isEngineOn ? "An" : "Aus"));
        System.out.println("Gang: " + gear);
        System.out.println("Menü:");
        System.out.println("1. Motor ein-/ausschalten");
        System.out.println("2. Gang wechseln (P, D, R)");
        System.out.println("3. Beschleunigen");
        System.out.println("4. Bremsen");
        System.out.println("5. Beenden");
    }

    
    public static int getUserChoice() {
        System.out.print("Ihre Auswahl: ");
        return keyBoard.nextInt();
    }

   
    public static void processChoice(int choice) {
        switch (choice) {
            case 1:
                toggleEngine();  
                break;
            case 2:
                changeGear();    
                break;
            case 3:
                accelerate();    
                break;
            case 4:
                brake();         
                break;
            case 5:
                exitSimulation(); 
                break;
            default:
                System.out.println("Ungültige Auswahl. Bitte erneut versuchen.");
        }
    }

    // Schaltet den Motor ein oder aus
    public static void toggleEngine() {
        isEngineOn = isEngineOn ? false : true;
    }

    // Ermöglicht die Eingabe eines neuen Gangs
    public static void changeGear() {
        System.out.println("Gang eingeben (P, D, R):");
        Scanner keyboard = new Scanner(System.in);
        gear = keyboard.next();
    }

    // Erhöht die Geschwindigkeit, falls Motor an ist und Gang != P
    public static void accelerate() {
        if (isEngineOn && !gear.equals("P")) {
            speed += 10;
        } else {
            System.out.println("Beschleunigung nicht möglich!");
        }
    }

    // Verringert die Geschwindigkeit, falls Motor an ist und Geschwindigkeit > 5
    public static void brake() {
        if (isEngineOn && speed > 5) {
            speed -= 5;
        } else {
            System.out.println("Bremsen nicht möglich!");
        }
    }

    // Beendet die Simulation
    public static void exitSimulation() {
        System.out.println("Simulation beendet.");
        System.exit(0);
    }

}
