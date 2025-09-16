package stuhl;

public class StuhlInMoebelHaus {
	private double preis;
	private String material;
	private String hersteller;
	private int lagerBestand;
	
	
		
	public StuhlInMoebelHaus(double preis, String material, String hersteller, int lagerBestand) {
		this.preis = setPreis(preis);
		this.material = material;
		this.hersteller = hersteller;
		this.lagerBestand = lagerBestand;
	}

	public double getPreis() {
		return preis;
	}
	public double setPreis(double preis) {
		if(preis>0) 
			return preis;
		System.out.println("Der preis must positive sein..!");
		return 0;
		
	}
	public String getMaterial() {
		return material;
	}
	public void setMaterial(String material) {
		this.material = material;
	}
	public String getHersteller() {
		return hersteller;
	}
	public void setHersteller(String hersteller) {
		this.hersteller = hersteller;
	}
	public int getLagerBestand() {
		return lagerBestand;
	}
	public void setLagerBestand(int lagerBestand) {
		this.lagerBestand = lagerBestand;
	}
	
	@Override
	public String toString() {
		return "StuhlInMoebelHaus [preis=" + preis + ", material=" + material + ", hersteller=" + hersteller
				+ ", lagerBestand=" + lagerBestand + "]";
	}
	
	public void verkaufen(int menge) {
		if(menge<lagerBestand) {
			lagerBestand-=menge;
		}
		System.out.println("wurde "+ menge + " Stühle verkauft.");
	}
	

}
