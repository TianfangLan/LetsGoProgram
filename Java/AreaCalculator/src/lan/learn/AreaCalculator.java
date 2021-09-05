package lan.learn;

public class AreaCalculator {
    public static double area(double radius){
        double areaOfCircle = -1.0;
        if (radius >= 0){
            areaOfCircle = radius * radius * Math.PI;
        }
        return areaOfCircle;
    }

    public static double area(double x, double y){
        double areaOfCircle = -1.0;
        if (x >= 0 && y >= 0){
            areaOfCircle = x * y;
        }
        return areaOfCircle;
    }
}
