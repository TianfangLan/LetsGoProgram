package com.company;

public class Main {

    public static void main(String[] args) {
        int myValue = 10000;

        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntValue = Integer.MAX_VALUE;
        System.out.println("Integer Minimum Value = " + myMinIntValue);
        System.out.println("Integer Maximum Value = " + myMaxIntValue);

        byte  myMinByteValue = Byte.MIN_VALUE;
        byte  myMaxByteValue = Byte.MAX_VALUE;
        System.out.println("Byte Minimum Value = " + myMinByteValue);
        System.out.println("Byte Maximum Value = " + myMaxByteValue);

        long myLongValue = 100L;
        // this will eventually work, since after computation, the number is legal.
        short testing = 32_768 - 1;

        // casting problem'
        byte myByte = (byte)(myMinByteValue / 2);
        long myLong = myLongValue / 2;

    }
}
