package lan.learn;

public class Main {

    public static void main(String[] args) {
        float myMaxFloat = Float.MAX_VALUE;
        float myMinFloat = Float.MIN_VALUE;
        System.out.println("the max float is :" + myMaxFloat);
        System.out.println("the min float is :" + myMinFloat);

        double myMaxDouble = Double.MAX_VALUE;
        double myMinDouble = Double.MIN_VALUE;
        System.out.println("the max double is :" + myMaxDouble);
        System.out.println("the min double is :" + myMinDouble);

        float fl = 5f / 3f;
        double d = 5.0 / 3.0;
        // will not work
        int myInt = 5/3;
        System.out.println(myInt);
        // casting will lose the decimals
        int myInt2 = (int)5.7;
        System.out.println(myInt2);
        System.out.println(poundsToKilograms(200));
    }
    public static double poundsToKilograms(float pound){
        //this function will transform pounds to kilograms
        float kilograms = pound * 0.45359237f;
        return kilograms;
    }
}
