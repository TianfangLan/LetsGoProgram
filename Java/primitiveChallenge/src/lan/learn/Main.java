package lan.learn;

public class Main {
    // the long and short definition problem
    byte myByte = 25;
    short myShort = 33;
    int myInt = 56;
    long myLong = ((myByte + myInt + myShort) * 10L + 50000L);
    short myShort2 = (short)((myByte + myInt + myShort) + 30);

}
