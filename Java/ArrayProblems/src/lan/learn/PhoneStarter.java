package lan.learn;

import java.util.Scanner;

public class PhoneStarter {

    private static Scanner scanner = new Scanner(System.in);
    private static MobilePhone phone = new MobilePhone("647-885-9226");

    public static void main(String[] args) {

        boolean quit = false;
        startPhone();
        printActions();
        while(!quit){
            System.out.println("\nEnter the action: ");
            int action = scanner.nextInt();
            scanner.nextLine();

            switch (action) {
                case 0:
                    System.out.println("\n shutting down");
                    quit = true;
                    break;

                case 1:
                    printContacts();
                    break;

                case 2:
                    addContact();
                    break;

                case 3:
                    updateContact();
                    break;

                case 4:
                    removeContact();
                    break;

                case 5:
                    queryContact();
                    break;

                case 6:
                    printActions();
                    break;

            }
        }
    }

    private static void updateContact() {
        System.out.println("Enter existing contact name: ");
        String name = scanner.nextLine();
        Contact existingContactRecord = phone.queryContact(name);
        if(existingContactRecord == null) {
            System.out.println("Contact not found.");
            return;
        }

        System.out.print("Enter new contact name: ");
        String newName = scanner.nextLine();
        System.out.print("Enter new contact phone number: ");
        String newNumber = scanner.nextLine();
        Contact newContact = Contact.createContact(newName, newNumber);
        if(phone.updateContact(existingContactRecord, newContact)) {
            System.out.println("Successfully updated record");
        } else {
            System.out.println("Error updating record.");
        }
    }


    private static void removeContact() {
        System.out.println("Enter existing contact name: ");
        String name = scanner.nextLine();
        Contact existingContactRecord = phone.queryContact(name);
        if (existingContactRecord == null) {
            System.out.println("Contact not found.");
            return;
        }

        if(phone.removeContact(existingContactRecord)) {
            System.out.println("Successfully deleted");
        } else {
            System.out.println("Error deleting contact");
        }
    }

    private static void queryContact() {
        System.out.println("Enter existing contact name: ");
        String name = scanner.nextLine();
        Contact existingContactRecord = phone.queryContact(name);
        if (existingContactRecord == null) {
            System.out.println("Contact not found.");
            return;
        }

        System.out.println("Name: " + existingContactRecord.getName() + " phone number is " + existingContactRecord.getPhoneNumber());
    }

    public static void addContact(){
        System.out.println("\nplease input name and phone number you want to add");
        System.out.println("name is: ");
        String name = scanner.nextLine();
        System.out.println("phone number is: ");
        String phoneNumber= scanner.nextLine();
        Contact contact = Contact.createContact(name, phoneNumber);
        if (phone.addNewContact(contact) == true) {
            System.out.println("\nThe contact has been added");
        } else {
            System.out.println("\nThe contact has already existed");
        }
    }

    public static void printContacts(){
        phone.printContacts();
    }


    public static void startPhone(){
        System.out.println("Starting phone...");
    }

    public static void printActions(){
        System.out.println("\nAvailable actions:\npress");
        System.out.println("0 - to shutdown\n" +
                "1 - to print contacts\n" +
                "... ");
    }

}
