package lan.learn;

public class Main {

    public static void main(String[] args) {
        // char uses '' not ""
        char myChar = 'A';
        char myUnicodeChar = '\u0044';

        boolean myTrue = true;
        String lan = "lan";
        lan = lan + "tianfang";
        System.out.println(lan);
        int myInt = 50;
        String myString = "10" + myInt;
        System.out.println(myString);

        boolean isCar = false;
        boolean wasCar = isCar ? true : false;
        if (wasCar){
            System.out.println("this line is running!");
        }
        int aNumber = isCar ? 3 : 4;
        System.out.println("The final number is :" + aNumber);

        double firstNumber = 20.00;
        double secondNumber = 80.00;
        double reminder = ((firstNumber + secondNumber) * 100) % 40.00;
        boolean myBool = (reminder == 0) ? true : false;
        System.out.println("the answer is: " + myBool);
        if (!myBool){
           System.out.println("got some reminder");
        }


    }
}
