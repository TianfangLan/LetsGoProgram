package lan.learn;

import java.util.Arrays;

public class ReverseArray {

    private static void reverse(int[] array) {
        int halfLength = array.length / 2;
        for (int i = 0; i < halfLength; i++) {
            int temp = array[i];
            array[i] = array[array.length - 1 - i];
            array[array.length - 1 - i] = temp;
        }
    }

    public static void main(String[] args) {
        int[] a = {5,4,3,2,1};
        reverse(a);
        System.out.println(Arrays.toString(a));
    }
}
