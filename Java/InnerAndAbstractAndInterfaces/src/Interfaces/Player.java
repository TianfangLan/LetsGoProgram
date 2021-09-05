package Interfaces;

import java.util.ArrayList;
import java.util.List;

public class Player implements ISaveable {
    private String name;
    private String weapon;
    private int hitPoints;
    private int strength;

    public Player(String name, int hitPoints, int strength) {
        this.name = name;
        this.hitPoints = hitPoints;
        this.strength = strength;
        this.weapon = "Sword";
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setWeapon(String weapon) {
        this.weapon = weapon;
    }

    public void setHitPoints(int hitPoints) {
        this.hitPoints = hitPoints;
    }

    public void setStrength(int strength) {
        this.strength = strength;
    }

    public String getName() {
        return name;
    }

    public String getWeapon() {
        return weapon;
    }

    public int getHitPoints() {
        return hitPoints;
    }

    public int getStrength() {
        return strength;
    }

    @Override
    public List<String> write() {
        List<String> saveData = new ArrayList<String>();
        saveData.add(0, this.name);
        saveData.add(1, "" + this.hitPoints);
        saveData.add(2, "" + this.strength);
        saveData.add(3, this.weapon);
        return saveData;
    }

    @Override
    public void read(List<String> saveData) {
        if (saveData != null && !saveData.isEmpty()) {
            this.name = saveData.get(0);
            this.hitPoints = Integer.parseInt(saveData.get(1));
            this.strength = Integer.parseInt(saveData.get(2));
            this.weapon = saveData.get(3);
        }
    }

    @Override
    public String toString() {
        return ("Player{name='" + this.name + "', hitPoints=" + this.hitPoints + ", strength=" +
                this.strength + ", weapon='" + this.weapon + "'}");
    }
}
