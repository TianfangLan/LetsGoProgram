package lan.learn;

import java.util.Scanner;

public class MaxMin1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        while (true){
            System.out.println("Please enter a number");
            boolean isInt = scanner.hasNextInt();
            if (isInt) {
                int currentNumber = scanner.nextInt();
                if(currentNumber > max){
                    max = currentNumber;
                }
                if(currentNumber < min){
                    min = currentNumber;
                }
            } else {
                System.out.println("The max number you have is: " + max);
                System.out.println("The min number you have is: " + min);
                break;
            }
            scanner.nextLine();
        }
        scanner.close();
    }
}
