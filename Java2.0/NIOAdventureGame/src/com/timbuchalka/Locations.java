package com.timbuchalka;

import java.io.*;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;


public class Locations implements Map<Integer, Location> {
    private static Map<Integer, Location> locations = new LinkedHashMap<Integer, Location>();

    public static void main(String[] args) throws IOException {
        // Writing in by object
        Path locPath = FileSystems.getDefault().getPath("location.dat");
        try (ObjectOutputStream locFile = new ObjectOutputStream(new BufferedOutputStream(Files.newOutputStream(locPath)))) {
            for (Location location : locations.values()) {
                locFile.writeObject(location);
            }
        }

//        // Writing into the text file by NIO
//        Path locPath = FileSystems.getDefault().getPath("locations_big.txt");
//        Path dirPath = FileSystems.getDefault().getPath("directions_big.txt");
//        try (BufferedWriter locFile = Files.newBufferedWriter(locPath);
//             BufferedWriter dirFile = Files.newBufferedWriter(dirPath)) {
//
//            for (Location location : locations.values()) {
//                locFile.write(location.getLocationID() + "," + location.getDescription() + "\n");
//                for (String direction : location.getExits().keySet()) {
//                    if (!direction.equalsIgnoreCase("Q")) {
//                        dirFile.write(location.getLocationID() + "," + direction + " ," +
//                                location.getExits().get(direction) + "\n");
//                    }
//                }
//            }
//
//        } catch (IOException e) {
//            System.out.println("IOException: " + e.getMessage());
//        }
    }


    static {
        // read by NIO in object
        Path locPath = FileSystems.getDefault().getPath("location.dat");
        try (ObjectInputStream locFile = new ObjectInputStream(new BufferedInputStream(Files.newInputStream(locPath)))) {
            boolean eof = false;
            while (!eof) {
                try {
                    Location location = (Location) locFile.readObject();
                    locations.put(location.getLocationID(), location);
                } catch (EOFException e) {
                    eof = true;
                }
            }
        } catch(InvalidClassException e) {
            System.out.println("InvalidClassException " + e.getMessage());
        } catch(IOException e) {
            System.out.println("IOException " + e.getMessage());
        } catch(ClassNotFoundException e) {
            System.out.println("ClassNotFoundException " + e.getMessage());
        }


//        read by NIO in text
//        try(ObjectInputStream locFile = new ObjectInputStream(new BufferedInputStream(new FileInputStream("locations.dat")))) {
//            boolean eof = false;
//            while (!eof) {
//                try {
//                    Location location = (Location) locFile.readObject();
//                    System.out.println("Read location " + location.getLocationID() + " : " + location.getDescription());
//                    System.out.println("Found " + location.getExits().size() + " exits");
//
//                    locations.put(location.getLocationID(), location);
//                } catch (EOFException e) {
//                    eof = true;
//                }
//            }
//        } catch(InvalidClassException e) {
//            System.out.println("InvalidClassException " + e.getMessage());
//        } catch(IOException io) {
//            System.out.println("IO Exception " + io.getMessage());
//        } catch(ClassNotFoundException e) {
//            System.out.println("ClassNotFoundException " + e.getMessage());
//        }
    }

    @Override
    public int size() {
        return locations.size();
    }

    @Override
    public boolean isEmpty() {
        return locations.isEmpty();
    }

    @Override
    public boolean containsKey(Object key) {
        return locations.containsKey(key);
    }

    @Override
    public boolean containsValue(Object value) {
        return locations.containsValue(value);
    }

    @Override
    public Location get(Object key) {
        return locations.get(key);
    }

    @Override
    public Location put(Integer key, Location value) {
        return locations.put(key, value);
    }

    @Override
    public Location remove(Object key) {
        return locations.remove(key);
    }

    @Override
    public void putAll(Map<? extends Integer, ? extends Location> m) {

    }

    @Override
    public void clear() {
        locations.clear();

    }

    @Override
    public Set<Integer> keySet() {
        return locations.keySet();
    }

    @Override
    public Collection<Location> values() {
        return locations.values();
    }

    @Override
    public Set<Entry<Integer, Location>> entrySet() {
        return locations.entrySet();
    }
}
