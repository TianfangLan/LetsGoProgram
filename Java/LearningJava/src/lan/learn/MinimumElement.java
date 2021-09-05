package lan.learn;

import java.util.Scanner;

public class MinimumElement {

    private static int readInteger(){
        Scanner scanner = new Scanner(System.in);
        int returnNumber = scanner.nextInt();
        scanner.close();
        return returnNumber;
    }

    private static int[] readElements(int size){
        Scanner scanner = new Scanner(System.in);
        int[] intArray = new int[size];
        for (int i = 0; i < size; i++){
            intArray[i] = scanner.nextInt();
        }
        scanner.close();
        return intArray;
    }

    private static int findMin(int[] intArray){
        int minInt = Integer.MAX_VALUE;
        for (int i = 0; i < intArray.length; i++){
            if (minInt > intArray[i]){
                minInt = intArray[i];
            }
        }
        return minInt;
    }
}
