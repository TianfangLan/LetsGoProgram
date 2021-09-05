package lan.learn;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.channels.Pipe;
import java.nio.charset.StandardCharsets;


public class Main {

    public static void main(String[] args) {

        try {
            Pipe pipe = Pipe.open();

            Runnable writer = new Runnable() {
                @Override
                public void run() {
                    try {
                        Pipe.SinkChannel sinkChannel = pipe.sink();
                        ByteBuffer buffer = ByteBuffer.allocate(56);

                        for (int i = 0; i < 10; i++) {
                            String currentTime = "The time is: " + System.currentTimeMillis();

                            buffer.put(currentTime.getBytes());
                            buffer.flip();

                            while (buffer.hasRemaining()) {
                                sinkChannel.write(buffer);
                            }
                            buffer.flip();
                            Thread.sleep(100);

                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            };

            Runnable reader = new Runnable() {
                @Override
                public void run() {

                    try{
                        Pipe.SourceChannel sourceChannel = pipe.source();
                        ByteBuffer buffer = ByteBuffer.allocate(56);

                        for (int i = 0; i < 10; i++) {
                            int bytesRead = sourceChannel.read(buffer);
                            byte[] timeString = new byte[bytesRead];
                            buffer.flip();
                            buffer.get(timeString);
                            System.out.println("Reader Thread: " + new String(timeString));
                            // System.out.println("Reader Thread: " + new String(buffer.array()));
                            buffer.flip();
                            Thread.sleep(100);
                        }
                    } catch (Exception e){
                        e.printStackTrace();
                    }
                }
            };

            new Thread(writer).start();
            new Thread(reader).start();

        } catch (IOException e) {
            e.printStackTrace();
        }


//        try (FileOutputStream binFile = new FileOutputStream("data.dat");
//             FileChannel binChannel = binFile.getChannel()) {
//            byte[] outputBytes = "Hello World!".getBytes();
//            byte[] outputBytes2 = "Nice to meet you".getBytes();
//            ByteBuffer buffer = ByteBuffer.allocate(100);
//            buffer.put(outputBytes);
//            int locInt1 = outputBytes.length;
//            buffer.putInt(245);
//            int locInt2 = locInt1 + Integer.BYTES;
//            buffer.putInt(-98765);
//            buffer.put(outputBytes2);
//            int locInt3 = locInt2 + Integer.BYTES + outputBytes2.length;
//            buffer.putInt(1000);
//            buffer.flip();
//            binChannel.write(buffer);
//
//
//            // writing file with position
//            byte[] newOutputBytes = "Hello World!".getBytes();
//            byte[] newOutputBytes2 = "Nice to meet you".getBytes();
//
//            long string1Loc = 0;
//            binChannel.write(ByteBuffer.wrap(newOutputBytes), string1Loc);
//
//            ByteBuffer intBuffer = ByteBuffer.allocate(Integer.BYTES);
//
//            intBuffer.putInt(245);
//            intBuffer.flip();
//            long intLoc1 = newOutputBytes.length;
//            binChannel.write(intBuffer, intLoc1);
//
//            intBuffer.flip();
//            intBuffer.putInt(-98765);
//            intBuffer.flip();
//            long intLoc2 = intLoc1 + Integer.BYTES;
//            binChannel.write(intBuffer, intLoc2);
//
//            long string2Loc = intLoc2 + Integer.BYTES;
//            binChannel.write(ByteBuffer.wrap(newOutputBytes2), string2Loc);
//
//            intBuffer.flip();
//            intBuffer.putInt(1000);
//            intBuffer.flip();
//            long intLoc3 = string2Loc + newOutputBytes2.length;
//            binChannel.write(intBuffer, intLoc3);
//
//
//            RandomAccessFile ra = new RandomAccessFile("data.dat", "rwd");
//            FileChannel channel = ra.getChannel();
//            ByteBuffer readBuffer = ByteBuffer.allocate(Integer.BYTES);
//
//
//            RandomAccessFile copyFile = new RandomAccessFile("dataCopy.dat","rw");
//            FileChannel copyChannel = copyFile.getChannel();
//            channel.position(0);
//            long numTransferred = copyChannel.transferFrom(channel, 0, channel.size());
//            System.out.println("The data has been transferd: " + numTransferred);
//
//            channel.close();
//            ra.close();
//            copyChannel.close();

//            channel.position(locInt3);
//            channel.read(readBuffer);
//            readBuffer.flip();
//            System.out.println(readBuffer.getInt());
//            readBuffer.flip();
//
//            channel.position(locInt2);
//            channel.read(readBuffer);
//            readBuffer.flip();
//            System.out.println(readBuffer.getInt());
//            readBuffer.flip();
//
//            channel.position(locInt1);
//            channel.read(readBuffer);
//            readBuffer.flip();
//            System.out.println(readBuffer.getInt());
//
//            channel.position(string1Loc);
//            byte[] string1 = new byte[newOutputBytes.length];
//            ByteBuffer string1Buffer = ByteBuffer.wrap(string1);
//            channel.read(string1Buffer);
//            string1Buffer.flip();
//            System.out.println(new String(string1));
//
//            channel.position(string2Loc);
//            byte[] string2 = new byte[newOutputBytes2.length];
//            ByteBuffer string2Buffer = ByteBuffer.wrap(string2);
//            channel.read(string2Buffer);
//            string2Buffer.flip();
//            System.out.println(new String(string2));

//            RandomAccessFile ra = new RandomAccessFile("data.dat", "rwd");
//            FileChannel channel = ra.getChannel();
//            ByteBuffer readBuffer = ByteBuffer.allocate(100);
//            channel.read(readBuffer);
//            System.out.println(readBuffer.getInt(locInt3));
//            byte[] inputByte2 = new byte[outputBytes2.length];
//            readBuffer.get(inputByte2, locInt2, inputByte2.length);
//            System.out.println(new String(inputByte2));
//            System.out.println(readBuffer.getInt(locInt2));
//            System.out.println(readBuffer.getInt(locInt1));
//            byte[] inputByte1 = new byte[outputBytes.length];
//            readBuffer.get(inputByte1, 0, outputBytes.length);
//            System.out.println(new String(inputByte1));


//            ByteBuffer readBuffer = ByteBuffer.allocate(100);
//            channel.read(readBuffer);
//            readBuffer.flip();
//            byte[] inputString = new byte[outputBytes.length];
//            readBuffer.get(inputString);
//            System.out.println(new String(inputString));
//            System.out.println(readBuffer.getInt());
//            System.out.println(readBuffer.getInt());
//            byte[] inputString2 = new byte[outputBytes2.length];
//            readBuffer.get(inputString2);
//            System.out.println(new String(inputString2));
//            System.out.println(readBuffer.getInt());

//        } catch (IOException e) {
//            e.printStackTrace();
//        }
    }
}
