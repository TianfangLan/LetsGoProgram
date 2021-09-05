package lan.learn;

public class NumberPalindrome {

    public static boolean isPalindrome(int number){
        int reverseNumber = 0;
        int originNumber = number;
        while (number != 0){
            reverseNumber = reverseNumber * 10 + (number % 10);
            number = number / 10;
        }
        return reverseNumber == originNumber;
    }
}