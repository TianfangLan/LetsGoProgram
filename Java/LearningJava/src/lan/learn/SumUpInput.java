package lan.learn;

import java.util.Scanner;

public class SumUpInput {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        int currentNumber = 1;
        int validNumber;
        while (currentNumber <= 10){
            System.out.println("Enter number #" + currentNumber);
            boolean isInt = scanner.hasNextInt();
            if (isInt){
                validNumber = scanner.nextInt();
                sum += validNumber;
                currentNumber++;
            } else {
                System.out.println("The input is not a valid number.");
            }
            scanner.nextLine(); // handle end of line (enter key)
        }
        System.out.println("The final sum is: " + sum);
        scanner.close();


    }
}
