package lan.learn;

import java.util.Locale;

public class Main {

    public static void main(String[] args) {
	int code = 1;
	switch(code){
        case 1:
            System.out.println("The value is 1");
            break;

        case 2:
            System.out.println("The value is 2");
            break;

        case 3: case 4: case 5:
            System.out.println("The value is 3 or 4 or 5");
            break;

        default:
            System.out.println("The value is not 1 or 2");
            break;
    }
    String month = "january";
	switch(month.toLowerCase(Locale.ROOT)){
        case "january":
            System.out.println("Jan");
            break;
        case "june":
            System.out.println("Jun");
            break;
        default:
            System.out.println("unknown");
            break;
    }
    }
}
