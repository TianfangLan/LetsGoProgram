public class Car {
    private boolean engine;
    private int cylinders;
    private String name;
    private int wheels;

    public Car(int cylinders, String name) {
        this.cylinders = cylinders;
        this.name = name;
        this.wheels = 4;
        this.engine = true;
    }

    public String getName() {
        return name;
    }

    public int getCylinders() {
        return cylinders;
    }

    public String startEngine() {
        return (name + "'s engine is starting.");
    }

    public String accelerate() {
        return(name + " is accelerating");
    }

    public String brake() {
        return(name + " is braking");
    }
}