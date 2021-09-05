package lan.learn;

public class Main {

    public static void main(String[] args) {
        SortedArray.getIntegers(0);

        String pointA = "String";
        String pointB = pointA;
        modify(pointA);
        System.out.println(pointA+" "+pointB);
    }

    public static String modify(String aString){
        return aString += "ABC";
    }
}
