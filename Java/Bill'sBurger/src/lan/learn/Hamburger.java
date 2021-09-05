package lan.learn;

public class Hamburger {
    private String name;
    private String meat;
    private double price;
    private String breadRollType;

    private String addition1Name;
    private String addition2Name;
    private String addition3Name;
    private String addition4Name;
    private double addition1Price;
    private double addition2Price;
    private double addition3Price;
    private double addition4Price;

    public Hamburger(String name, String meat, double price, String breadRollType) {
        this.name = name;
        this.meat = meat;
        this.price = price;
        this.breadRollType = breadRollType;
        System.out.println(name + " hamburger on a " + breadRollType + " roll with " + meat + " ,price is " + price);
    }

    public void addHamburgerAddition1(String additionName, double additionPrice) {
        addition1Price = additionPrice;
        addition1Name = additionName;
        price += additionPrice;
        System.out.println("added " + additionName + " for an extra " + additionPrice);
    }

    public void addHamburgerAddition2(String additionName, double additionPrice) {
        addition2Price = additionPrice;
        addition2Name = additionName;
        price += additionPrice;
        System.out.println("added " + additionName + " for an extra " + additionPrice);
    }

    public void addHamburgerAddition3(String additionName, double additionPrice) {
        addition3Price = additionPrice;
        addition3Name = additionName;
        price += additionPrice;
        System.out.println("added " + additionName + " for an extra " + additionPrice);
    }

    public void addHamburgerAddition4(String additionName, double additionPrice) {
        addition4Price = additionPrice;
        addition4Name = additionName;
        price += additionPrice;
        System.out.println("added " + additionName + " for an extra " + additionPrice);
    }

    public double itemizeHamburger() {
        return price;
    }

}
