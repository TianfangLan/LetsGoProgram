package lan.learn;

import java.util.Scanner;

public class SortedArray {
    private static Scanner scanner = new Scanner(System.in);


    public static int[] getIntegers(int capacity) {
        int[] theArray = new int[capacity];
        for (int i = 0; i < capacity; i++) {
            theArray[i] = scanner.nextInt();
        }
        sortIntegers(theArray);
        printArray(theArray);
        return theArray;
    }

    public static void printArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.println("Element " + i + " contents " + array[i]);
        }
    }

    public static int[] sortIntegers(int[] array) {
        int holdNumber = 0;
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] < array[j]) {
                    holdNumber = array[i];
                    array[i] = array[j];
                    array[j] = holdNumber;
                }
            }
        }
        return array;
    }

}
