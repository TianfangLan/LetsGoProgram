package suitably;

public class Series {

    public static int nSum(int n){
        int result = 0;
        for (int i = 0; i <= n; i++){
            result += i;
        }
        return result;
    }

    public static int factorial(int n){
        if (n == 0){
            return 0;
        }
        int result = 1;
        for (int i = 1; i <= n; i++){
            result *= i;
        }
        return result;
    }

    public static int fibonacci(int n){
        int number1 = 0;
        int number2 = 1;
        if (n == 0){
            return 0;
        }
        for (int i = 1; i < n; i++){
            int saveNumber = number2;
            number2 += number1;
            number1 = saveNumber;
        }
        return number2;
    }
}
