package lan.learn;

public class Main {

    public static void main(String[] args) {
        for (int i = 0; i <= 4; i++){
            System.out.println("Now at number: " + i);
        }
        // it will round the number
        for (int i = 9; i >= 4; i--){
            System.out.println("Now at number: " + i);
        }
        System.out.println(String.format("%.2f", 3.007));
    }

    public static boolean isPrime(int n){
        boolean aPrime = true;
        if (n != 1){
            for (int i = 2; i <= n/2; i++){
                if(n % i == 0){
                    aPrime = false;
                }
            }
        } else {
            aPrime = false;
        }
        return aPrime;
    }

}
