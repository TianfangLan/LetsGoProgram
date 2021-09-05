package lan.learn;

public class Dog extends Animal{
    private int eyes;
    private int legs;
    private int tail;
    private int teeth;
    private String coat;

    public Dog(String name, int size, int weight,int eyes, int legs, int tail, int teeth, String coat) {
        super(name, 1, 1 , size, weight);
        this.coat = coat;
        this.eyes = eyes;
        this.tail = tail;
        this.legs = legs;
        this.teeth = teeth;
    }

    public void chew(){
        System.out.println("dog.chew() is called");
    }

    @Override
    public void eat() {
        System.out.println("dot.eat is called");
        chew();
        super.eat();
    }

    public void walk(){
        System.out.println("Dog.walk() is called");
        super.move(5);
    }

    public void run(){
        System.out.println("Dog.run() is called");
        move(10);
    }

    private void moveLegs(int speed){
        System.out.println("Dog,moveLegs() is called");
    }

    @Override
    public void move(int speed) {
        System.out.println("Dog.move() is called");
        moveLegs(speed);
        super.move(speed);
    }
}
