package lan.learn;

public class FirstLastDigitSum {

    public static int sumFirstAndLastDigit(int number){
        if (number < 0){
            return -1;
        }
        int lastDigit = number % 10, firstDigit = lastDigit;
        while (number != 0){
            firstDigit = number % 10;
            number = number / 10;
        }
        return firstDigit + lastDigit;
    }
}
