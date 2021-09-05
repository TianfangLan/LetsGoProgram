package lan.learn;

public class Account {
    private String number;
    private double balance;
    private String customerName;
    private String customerEmailAddress;
    private String customerPhoneNumber;

    public Account(){
        this("56789", 2.5, "Default name", "Default address", "default phone");
    }

    public Account(String number, double balance, String customerName,
                   String customerPhoneNumber, String customerEmailAddress){
        this.balance = balance;
        this.number = number;
        this.customerEmailAddress = customerEmailAddress;
        this.customerName = customerName;
        this.customerPhoneNumber = customerPhoneNumber;
    }

    public Account(String customerName, String customerEmailAddress, String customerPhoneNumber) {
        this("99999", 100.55, "Default name", "Default address", "default phone");
    }

    public void deposit(double depositAmount){
        this.balance += depositAmount;
        System.out.println();
        System.out.println("Deposit of " + depositAmount + " processed. Remaining balance = " + this.balance);
    }

    public void withdrawal(double withdrawalAmount){
        if(this.balance - withdrawalAmount < 0){
            System.out.println("only " + this.balance + " available. Withdrawal not processed");
        } else {
            this.balance -= withdrawalAmount;
            System.out.println("Withdrawal of " + withdrawalAmount + " processed. Remaining balance = " + this.balance);
        }
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getCustomerEmailAddress() {
        return customerEmailAddress;
    }

    public void setCustomerEmailAddress(String customerEmailAddress) {
        this.customerEmailAddress = customerEmailAddress;
    }

    public String getCustomerPhoneNumber() {
        return customerPhoneNumber;
    }

    public void setCustomerPhoneNumber(String customerPhoneNumber) {
        this.customerPhoneNumber = customerPhoneNumber;
    }
}
