package lan.learn;

class Car {
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
        return ("Car -> starting.");
    }

    public String accelerate() {
        return ("Car is accelerating");
    }

    public String brake() {
        return ("Car is braking");
    }
}

class Mitsubishi extends Car {
    public Mitsubishi(int cylinders, String name) {
        super(cylinders, name);
    }

    @Override
    public String startEngine() {
        return ( "Mitsubishi's engine is starting.");
    }

    @Override
    public String accelerate() {
        return ("Mitsubishi is accelerating");
    }

    @Override
    public String brake() {
        return ("Mitsubishi is braking");
    }
}

class Holden extends Car {
    public Holden(int cylinders, String name) {
        super(cylinders, name);
    }

    @Override
    public String startEngine() {
        return ("Holden is starting.");
    }

    @Override
    public String accelerate() {
        return ("Holden is accelerating");
    }

    @Override
    public String brake() {
        return ("Holden is braking");
    }
}


class Ford extends Car {
    public Ford(int cylinders, String name) {
        super(cylinders, name);
    }

    @Override
    public String startEngine() {
        return ( "Ford's engine is starting.");
    }

    @Override
    public String accelerate() {
        return ("Ford is accelerating");
    }

    @Override
    public String brake() {
        return ("Ford is braking");
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car(8, "Base Car");
        System.out.println(car.startEngine());
        Mitsubishi mitsubishi =new Mitsubishi(6,"Outlander VRX 4WD");
        System.out.println(mitsubishi.startEngine());
    }
}