public class Main {

    public static void main(String[] args) {
        House houseA = new House("Green");
        House houseB = houseA;
        houseA = new House("black");

        houseA.printHouse();
        houseB.printHouse();

        House houseC = new House("Blue");
        houseA = houseC;
        houseA.printHouse();
        houseB.printHouse();
        houseC.printHouse();

        // different problems
        int[] a = {1,2,3,4,5};
        int[] b = a;
        int[] c = {0,0,0,0,0};
        a = c;
        printList(a);
        printList(b);
        printList(c);
    }

    public static void printList(int[] a){
        System.out.print("{");
        for(int i = 0; i < a.length; i++){
            System.out.print(a[i] + "");
            if (i + 1 != a.length){
                System.out.print(", ");
            }
        }
        System.out.print("}\n");
    }
}
