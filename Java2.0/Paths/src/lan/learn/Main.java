package lan.learn;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.nio.file.*;

public class Main {

    public static void main(String[] args) {
        try {
            Path fileToDelete = FileSystems.getDefault().getPath("Examples", "Dir1", "file1copy.txt");
            Files.deleteIfExists(fileToDelete);

//            Path fileToMove = FileSystems.getDefault().getPath("Examples", "file2.txt");
//            Path destination = FileSystems.getDefault().getPath("Examples", "file1.txt");
//            Files.move(fileToMove, destination);

//            Path fileToMove = FileSystems.getDefault().getPath("Examples", "file1copy.txt");
//            Path destination = FileSystems.getDefault().getPath("Examples", "Dir1", "file1copy.txt");
//            Files.move(fileToMove, destination);

//            Path origin = FileSystems.getDefault().getPath("Examples", "file1.txt");
//            Path targetPath = FileSystems.getDefault().getPath("Examples", "file1copy.txt");
//            Files.copy(origin, targetPath, StandardCopyOption.REPLACE_EXISTING);
//
//            origin = FileSystems.getDefault().getPath("Examples", "dir1");
//            targetPath = FileSystems.getDefault().getPath("Examples", "dir4");
//            Files.copy(origin, targetPath, StandardCopyOption.REPLACE_EXISTING);


        } catch (IOException e){
            System.out.println(e.getMessage());

        }


    }
//        Path path = FileSystems.getDefault().getPath("WorkingDirectoryFile.txt");
//        printFile(path);
//        Path filePath = FileSystems.getDefault().getPath("File","SubDirectoryFile.txt");
//        printFile(filePath);
//        Path outPath = Paths.get("D:\\GAMERS\\outThere.txt");
//        printFile(outPath);
//
//        filePath = Paths.get(".");
//        System.out.println(filePath.toAbsolutePath());
//
//        Path path2 = Paths.get(".", "File","..","File","SubDirectoryFile.txt");
//        System.out.println(path2.toAbsolutePath());
//        // D:\CSC programs\Java2\Paths\.\File\..\File\SubDirectoryFile.txt
//        System.out.println(path2.normalize().toAbsolutePath());
//        // D:\CSC programs\Java2\Paths\File\SubDirectoryFile.txt
//        printFile(path2);
//        // this still works even it's not normalized
//    }
//
//    public static void printFile(Path path){
//        try(BufferedReader fileReader = Files.newBufferedReader(path)){
//            String line;
//            while ((line = fileReader.readLine()) != null){
//                System.out.println(line);
//            }
//        } catch (IOException e){
//            System.out.println(e.getMessage());
//            e.printStackTrace();
//        }
//    }
}
