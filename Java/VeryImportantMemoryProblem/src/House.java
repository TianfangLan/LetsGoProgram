public class House {

    private String color;

    public House (String color){
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void printHouse(){
        System.out.println("The color of the house is: " + color);
    }
}
