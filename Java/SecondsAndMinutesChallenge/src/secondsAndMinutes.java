public class secondsAndMinutes {

    public static String getDurationString(int minutes, int seconds){
        String newFormat = "Invalid value";
        if (minutes >= 0 && seconds >= 0 && seconds <= 59){
            int hours = minutes / 60;
            minutes = minutes % 60;
            newFormat = hours + "h " + minutes + "m "+ seconds + "s";
        }
        return newFormat;
    }

    public static String getDurationString(int seconds){
        String newFormat = "Invalid value";
        if (seconds >= 0){
            int minutes = seconds / 60;
            seconds = seconds % 60;
            newFormat = getDurationString(minutes, seconds);
        }
        return newFormat;
    }
}
