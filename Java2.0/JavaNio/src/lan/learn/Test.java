package lan.learn;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.channels.ByteChannel;
import java.nio.channels.FileChannel;
import java.nio.charset.StandardCharsets;

public class Test {
    public static void main (String[] args) {
        try (FileOutputStream file = new FileOutputStream("data.dat1");
             FileChannel binChannel = file.getChannel()){
            long int1Pos = 0;
            ByteBuffer intBuffer = ByteBuffer.allocate(Integer.BYTES);
            intBuffer.putInt(38);
            intBuffer.flip();
            binChannel.write(intBuffer);
            intBuffer.flip();

            byte[] string1 = "hello?".getBytes(StandardCharsets.UTF_8);
            ByteBuffer stringBuffer = ByteBuffer.wrap(string1);
            long string1Pos = Integer.BYTES;
            binChannel.write(stringBuffer, string1Pos);
            string1[0] = 'a';

            RandomAccessFile ra = new RandomAccessFile("data.dat1", "rwd");
            FileChannel readChannel = ra.getChannel();

            // option 1
            stringBuffer.flip();
            readChannel.read(stringBuffer, Integer.BYTES);
            stringBuffer.flip();
            System.out.println(new String(string1));

            // option 2
            stringBuffer.flip();
            readChannel.position(string1Pos);
            readChannel.read(stringBuffer);
            stringBuffer.flip();
            System.out.println(new String(string1));

//            // do not do this!!!!!!!!!!!
//            ByteBuffer bigBuffer = ByteBuffer.allocate(100);
//            readChannel.read(bigBuffer, 0);
//            bigBuffer.get(string1, (int)string1Pos, string1.length);
//            System.out.println(new String(string1));


        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
