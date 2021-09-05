package lan.learn;

public class Main {

    public static void main(String[] args) {
        int NewScore = calculateScore("lan" , 300);
        System.out.println("New score is: " + NewScore);
        calculateScore(30);
        calculateScore();
    }

    public static int calculateScore(String playerName, int score){
        System.out.println("Player " + playerName + " scored " + score + " points");
        return score *1000;
    }

    public static int calculateScore(int score){
        System.out.println("Unnamed Player scored " + score + " points");
        return score *1000;
    }

    public static int calculateScore(){
        return calculateScore(0);
    }
}
