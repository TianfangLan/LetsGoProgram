package lan.learn;

public class EvenDigitSum {

    public static int getEvenDigitSum(int number){
        if(number < 0){
            return -1;
        }
        int sum = 0;
        boolean isEven = false;
        while (number > 0){
            if (isEven){
                sum += number % 10;
            }
            number = number / 10;
            isEven = !isEven;
        }
        return sum;
    }
}
