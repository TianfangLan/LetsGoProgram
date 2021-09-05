package Interfaces;

import java.util.ArrayList;
import java.util.List;

public class Monster implements ISaveable{
    private String name;
    private int hitPoints;
    private int strength;

    public Monster(String name, int hitPoints, int strength) {
        this.name = name;
        this.hitPoints = hitPoints;
        this.strength = strength;
    }

    public String getName() {
        return name;
    }

    public int getHitPoints() {
        return hitPoints;
    }

    public int getStrength() {
        return strength;
    }

    // write the current data in a list and then return it.
    @Override
    public List<String> write() {
        List<String> saveData = new ArrayList<String>();
        saveData.add(0, this.name);
        saveData.add(1, "" + this.hitPoints);
        saveData.add(2, "" + this.strength);
        return saveData;
    }

    // read data from input or outside the game
    @Override
    public void read(List<String> saveData) {
        if (saveData != null && !saveData.isEmpty()) {
            this.name = saveData.get(0);
            this.hitPoints = Integer.parseInt(saveData.get(1));
            this.strength = Integer.parseInt(saveData.get(2));
        }
    }

    @Override
    public String toString() {
        return ("Player{name='" + this.name + "', hitPoints=" + this.hitPoints + ", strength=" +
                this.strength + "}");
    }
}
