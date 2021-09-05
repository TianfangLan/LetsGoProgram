package lan.learn;

public class DiagonalStar {

    public static void printSquareStar(int number){
        if (number<5){
            System.out.println("Invalid Value");
            return;
        }
        for (int row = 1; row <= number; row++){
            for (int column = 1; column <= number; column++){
                if (column == number) {
                    System.out.println("*");
                } else if (column == 1 || row == 1 || row == number || row == column
                        || column + row == (number + 1)){
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
        }
    }
}
