public class SpeedConverter {

    public static long toMilesPerHour(double kilometersPerHour){
        long miles = -1L;
        if (kilometersPerHour >= 0){
            miles = Math.round((kilometersPerHour / 1.609));
        }
        return miles;
    }
    public static void printConversion (double kilometersPerHour){
        if (toMilesPerHour(kilometersPerHour) == -1){
            System.out.println("Invalid Value");
        } else {
            System.out.println(kilometersPerHour + " km/h = " + toMilesPerHour(kilometersPerHour) + " mi/h");
        }
    }
}
