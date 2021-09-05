package lan.learn;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static Map<String, String> vocabulary = new HashMap();
    private static Map<Integer, Location> locations = new HashMap<Integer, Location>();

    public static void main(String[] args) {
        locations.put(0, new Location(0, "You are sitting in front of a computer learning Java"));
        locations.put(1, new Location(1, "You are standing at the end of a road before a small brick building"));
        locations.put(2, new Location(2, "You are at the top of a hill"));
        locations.put(3, new Location(3, "You are inside a building, a well house for a small spring"));
        locations.put(4, new Location(4, "You are in a valley beside a stream"));
        locations.put(5, new Location(5, "You are in the forest"));

        locations.get(1).addExit("W", 2);
        locations.get(1).addExit("E", 3);
        locations.get(1).addExit("S", 4);
        locations.get(1).addExit("N", 5);

        locations.get(2).addExit("N", 5);

        locations.get(3).addExit("W", 1);

        locations.get(4).addExit("N", 1);
        locations.get(4).addExit("W", 2);

        locations.get(5).addExit("S", 1);
        locations.get(5).addExit("W", 2);

        vocabulary.put("north", "N");
        vocabulary.put("n", "N");
        vocabulary.put("south", "S");
        vocabulary.put("s", "S");
        vocabulary.put("west", "W");
        vocabulary.put("w", "W");
        vocabulary.put("east", "E");
        vocabulary.put("e", "E");
        vocabulary.put("quit", "Q");
        vocabulary.put("q", "Q");
        command();
    }

    public static void command() {
        // initial a map for the different input
        int loc = 1;
        while (true) {
            // print the location description
            Location location = locations.get(loc);
            System.out.println(location.getDescription());
            // stop the program when loc is 0
            if (loc == 0){
                break;
            }
            // print out all the available exits of the current location
            System.out.print("Available exits are ");
            for (String exit : location.getExits().keySet()) {
                System.out.print(exit + ", ");
            }
            System.out.println();

            // user input the command
            Scanner scanner = new Scanner(System.in);
            String[] move = scanner.nextLine().toLowerCase().split(" ");
            Map<String, Integer> exits = location.getExits();
            boolean notMoved = true;
            for (String direction : move) {
                // change all the directions into N,S,W,E;
                // if the word is not in the vocabulary, it should return null and will not be executed
                String directionFormal = vocabulary.get(direction);
                if (exits.containsKey(directionFormal)) {
                    // reassign the location
                    loc = exits.get(directionFormal);
                    notMoved = false;
                    // stop the loop;
                    break;
                }
            }
            if (notMoved){
                System.out.println("You cannot go in that direction");
            }
        }
    }
}


