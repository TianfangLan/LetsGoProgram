package lan.learn;

public class judgePrime {

    public static boolean isPrime(int n){
        boolean aPrime = true;
        // since 1 is not a prime number
        if (n != 1){
            // test the number can exact divide int i until it reach half of itself
            for (int i = 2; i <= n/2; i++){
                if(n % i == 0){
                    aPrime = false;
                    // once the number is not prime, stop the looping
                    break;
                }
            }
        } else {
            aPrime = false;
        }
        return aPrime;
    }
}
