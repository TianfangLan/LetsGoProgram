package lan.learn;

import java.util.ArrayList;

public class Customer {

    private String name;
    private ArrayList<Double> transactions;

    public Customer(String name, double money) {
        this.name = name;
        this.transactions = new ArrayList<Double>();
        transactions.add(money);
    }

    public void addTransaction(double money){
        transactions.add(money);
    }

    public String getName() {
        return name;
    }

    public ArrayList<Double> getTransactions() {
        return transactions;
    }
}
