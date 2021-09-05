package lan.learn;

public class VipCustomer {
    private String name;
    private String emailAddress;
    private double limit;

    public VipCustomer(String name, String emailAddress, double limit) {
        this.name = name;
        this.emailAddress = emailAddress;
        this.limit = limit;
    }

    public VipCustomer() {
        this("Unknown", "Default email", 0);
    }

    public VipCustomer(String name, String emailAddress) {
        this(name, emailAddress, 0);
    }

    public String getName() {
        return name;
    }

    public String getEmailAddress() {
        return emailAddress;
    }

    public double getLimit() {
        return limit;
    }
}
