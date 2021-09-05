package lan.learn;

import java.util.Scanner;

public class ReadUserInput {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please input your year of birth: ");

        boolean hasNextInt = scanner.hasNextInt();
        if (hasNextInt){
            int yearOfBirth = scanner.nextInt();
            // handle next line character (enter key)
            scanner.nextLine();
            System.out.println("Please input your year of birth: ");
            int aa = scanner.nextInt();
            System.out.println("Please input your name: ");
            String name = scanner.nextLine();
            int age = 2021 - yearOfBirth;
            if (age >= 0 && age <= 160){
                System.out.println("Your age is: " + age + "Your name is: " + name);
            } else{
                System.out.println("Invalid year of birth");
            }
        } else {
            System.out.println("Unable to parse year of birth.");
        }
        scanner.close();
    }
}
