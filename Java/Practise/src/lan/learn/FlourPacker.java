package lan.learn;

public class FlourPacker {

    public static boolean canPack(int bigCount, int smallCount, int goal){
        boolean packed = false;
        int bigPack = 0;
        while(bigPack <= bigCount && (bigPack * 5 <= goal)){
            if(((bigPack * 5) + smallCount) >= goal){
                packed = true;
                break;
            }
            bigPack ++;
        }
        return packed;
    }
}
