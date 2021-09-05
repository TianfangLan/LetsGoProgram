package LinkedList;

public class DeskPhone implements ITelephone{

    private int myNumber;
    private boolean isRinging;

    public DeskPhone(int myNumber) {
        this.myNumber = myNumber;
    }

    @Override
    public void powerOn() {
        System.out.println("No action taken, desk phone does not have a power button");
    }

    @Override
    public void dial(int phoneNumber) {
        System.out.println("Now calling: " + phoneNumber +" on desk phone");
    }

    @Override
    public void answer() {
        if(isRinging){
            System.out.println("Answering the desk phone");
            isRinging = false;
        }
    }

    @Override
    public boolean callPhone(int phoneNumber) {
        return false;
    }

    @Override
    public boolean isRinging() {
        return isRinging;
    }

    public void canIDoThis(){
    }
}
