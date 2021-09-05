package lan.learn;

import java.util.ArrayList;

public class MobilePhone {
    private String myNumber;
    private ArrayList<Contact> myContacts;

    public MobilePhone(String myNumber) {
        this.myNumber = myNumber;
        this.myContacts = new ArrayList<Contact>();
    }

    private int findContact(Contact contact) {
        return myContacts.lastIndexOf(contact);

    }

    private int findContact(String name) {
        for (int i = 0; i < myContacts.size(); i++) {
            if (myContacts.get(i).getName().equals(name)) {
                return i;
            }
        }
        return -1;
    }

    public boolean addNewContact(Contact contact) {
        if (findContact(contact.getName()) >= 0) {
            System.out.println("Contact is already on file");
            return false;
        } else {
            myContacts.add(contact);
            return true;
        }
    }

    public boolean updateContact(Contact oldContact, Contact newContact) {
        int position = findContact(oldContact.getName());
        if (position < 0) {
            return false;
        } else if (findContact(newContact.getName()) != -1){
            System.out.println("This name has already exist, cannot update it.");
            return false;
        } else {
            myContacts.set(position, newContact);
            return true;
        }
    }

    public boolean removeContact(Contact contact) {
        int position = findContact(contact.getName());
        if (position >= 0) {
            myContacts.remove(position);
            return true;
        } else {
            return false;
        }
    }


    public Contact queryContact(String name) {
        int position = findContact(name);
        if (position >= 0) {
            return myContacts.get(position);
        } else {
            return null;
        }
    }

    public void printContacts() {
        System.out.println("Contact List:");
        for (int i = 0; i < myContacts.size(); i++) {
            System.out.println((i + 1) + ". " + myContacts.get(i).getName() + " -> " + myContacts.get(i).getPhoneNumber());
        }
    }
}
