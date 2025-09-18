
```java
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
```
```java
package tiere;

public class Fisch  extends Tier{

	public String lebenIn;
	
	public void schwimmen() {
		
	}
	//getter und setter methode
}

```
```java
package tiere;

public class SaugeTier  extends Tier{
	public String fellFarbe;
	
	public void zeigeLaufen() {
		
	}
	
	//getter und setter methode

}
```
```java
package tiere;

public class Vogel extends Tier {
	public int maxFlugHoehe;
	public void zeigeZiel() {
		//....
```
