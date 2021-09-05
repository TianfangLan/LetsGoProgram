package lan.learn;

import java.util.Scanner;

public class MaxMin2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int max, min;
        boolean first = true;
        while (true){
            System.out.println("Please enter a number");
            boolean isInt = scanner.hasNextInt();
            if (isInt) {
                int currentNumber = scanner.nextInt();
                if(first);{
                    first = false;
                    max = currentNumber;
                    min = currentNumber;
                }
                if(currentNumber > max){
                    max = currentNumber;
                }
                if(currentNumber < min){
                    min = currentNumber;
                }
            } else {
                break;
            }
            System.out.println("The max number you have is: " + max);
            System.out.println("The min number you have is: " + min);
            scanner.nextLine();
        }
        scanner.close();
    }
}
