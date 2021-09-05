package lan.learn;

public class DeluxeBurger extends Hamburger{

    public DeluxeBurger() {
        super("DeluxeBurger", "Sausage & Bacon", 19.10, "White");
        System.out.println("added Chips for an extra 3.75");
        System.out.println("added Drink for an extra 1.81");
    }

    @Override
    public void addHamburgerAddition1(String additionName, double additionPrice) {
        System.out.println("Can not add additional item to a deluxe burger");
    }

    @Override
    public void addHamburgerAddition2(String additionName, double additionPrice) {
        System.out.println("Can not add additional item to a deluxe burger");
    }

    @Override
    public void addHamburgerAddition3(String additionName, double additionPrice) {
        System.out.println("Can not add additional item to a deluxe burger");
    }

    @Override
    public void addHamburgerAddition4(String additionName, double additionPrice) {
        System.out.println("Can not add additional item to a deluxe burger");
    }
}
