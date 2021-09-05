package lan.learn;

import java.util.ArrayList;

public class Bank {

    private String name;
    private ArrayList<Branch> branches;

    public Bank(String name) {
        this.name = name;
        branches = new ArrayList<Branch>();
    }

    private Branch findBranch(String name) {
        for (int i = 0; i < branches.size(); i++) {
            Branch branch = branches.get(i);
            if (branch.getName().equals(name)) {
                return branch;
            }
        }
        return null;
    }

    public boolean addBranch(String branch) {
        if (findBranch(branch) == null) {
            branches.add(new Branch(branch));
            return true;
        }
        return false;
    }

    public boolean addCustomer(String branchName, String customerName, double transaction) {
        Branch branch = findBranch(branchName);
        if(branch!=null) {
            return branch.newCustomer(customerName, transaction);
        }
        return false;
    }

    public boolean addCustomerTransaction(String branchName, String customerName, double transaction) {
        Branch branch = findBranch(branchName);
        if (branch == null) {
            return false;
        }
        if (branch.addCustomerTransaction(customerName, transaction)) {
            return true;
        } else {
            return false;
        }
    }

    public boolean listCustomers(String branchName, boolean printTransaction) {
        Branch branch = findBranch(branchName);
        if (branch != null) {
            System.out.println("Customer details for branch " + branch.getName());

            ArrayList<Customer> branchCustomers = branch.getCustomers();
            for (int i = 0; i < branchCustomers.size(); i++) {
                Customer branchCustomer = branchCustomers.get(i);
                System.out.println("Customer: " + branchCustomer.getName() + "[" + (i + 1) + "]");
                if (printTransaction) {
                    System.out.println("Transactions");
                    ArrayList<Double> transactions = branchCustomer.getTransactions();
                    for (int j = 0; j < transactions.size(); j++) {
                        System.out.println("[" + (j + 1) + "]  Amount " + transactions.get(j));
                    }
                }
            }
            return true;
        } else {
            return false;
        }
    }
}
//        Branch branch = findBranch(branchName);
//        if (branch == null) {
//            return false;
//        }
//        System.out.println("Customer details for branch " + branchName);
//        for (int i = 0; i < branch.getCustomers().size(); i++) {
//            Customer customer = branch.getCustomers().get(i);
//            System.out.println("Customer: " + customer.getName() + "[" + (i + 1) + "]");
//            if (printTransaction) {
//                ArrayList<Double> transaction = customer.getTransactions();
//                System.out.println("Transactions");
//                for (int j = 0; j < transaction.size(); j++) {
//                    System.out.println("[" + (j + 1) + "] Amount  " + transaction.get(j));
//                }
//            }
//        }
//        return true;
//    }
//}
