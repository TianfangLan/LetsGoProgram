import jdk.swing.interop.SwingInterOpUtils;

import java.io.*;
import java.util.*;


public class Locations implements Map<Integer, Location> {

    private static Map<Integer, Location> locations = new LinkedHashMap<Integer, Location>();
    private static Map<Integer, IndexRecord> index = new LinkedHashMap<>();
    private static RandomAccessFile ra;

    public static void main(String[] args) throws IOException {
        // write by RandomAccess File
        try (RandomAccessFile rao = new RandomAccessFile("locations_rand.dat", "rwd")) {
            rao.writeInt(locations.size());
            int indexSize = locations.size() * 3 * Integer.BYTES;
            int locationStart = (int) (indexSize + rao.getFilePointer() + Integer.BYTES);
            rao.writeInt(locationStart);

            long indexStart = rao.getFilePointer();

            int startPointer = locationStart;

            // point the offset to start of the data
            rao.seek(startPointer);

            // writing the data
            for (Location location : locations.values()) {
                // write location id
                rao.writeInt(location.getLocationID());
                // write description for the location
                rao.writeUTF(location.getDescription());
                // write all the exits for the current location
                // in the format of direction name, locationID
                StringBuilder builder = new StringBuilder();
                for (String direction : location.getExits().keySet()) {
                    if (!direction.equalsIgnoreCase("Q")) {
                        builder.append(direction);
                        builder.append(",");
                        builder.append(location.getExits().get(direction));
                        builder.append(",");
                    }
                }
                rao.writeUTF(builder.toString());

                // create the IndexRecord for the current location (startPointer, length)
                IndexRecord record = new IndexRecord(startPointer, (int) (rao.getFilePointer() - startPointer));

                // put it into the index map
                index.put(location.getLocationID(), record);

                // update the startPointer
                startPointer = (int) rao.getFilePointer();
            }

            rao.seek(indexStart);
            for (Map.Entry<Integer, IndexRecord> locationEntry : index.entrySet()) {
                rao.writeInt(locationEntry.getKey());
                rao.writeInt(locationEntry.getValue().getStartByte());
                rao.writeInt(locationEntry.getValue().getLength());
            }

        }

//        write by object
//        try (ObjectOutputStream locFile = new ObjectOutputStream(new BufferedOutputStream(new FileOutputStream("locations.dat")))) {
//            for(Location location : locations.values()) {
//                locFile.writeObject(location);
//            }
//        }


//========write by binary stream=================
//        try (DataOutputStream locFile = new DataOutputStream(new BufferedOutputStream(new FileOutputStream("locations.dat"))))
//        {
//            // when write the location file, write with the ID and the description
//            for(Location location: locations.values()){
//                locFile.writeInt(location.getLocationID());
//                locFile.writeUTF(location.getDescription());
//                System.out.println("Writing location " + location.getLocationID() + " : "+ location.getDescription());
//                System.out.println("Writing " + (location.getExits().size() - 1) + " exits.");
//                locFile.writeInt(location.getExits().size() - 1);
//                // when writing the direction file, write with the current location ID and the exits
//                // but Q and 0 are not in the list
//                for (Map.Entry<String, Integer> exit : location.getExits().entrySet()){
//                    if(!exit.getKey().equalsIgnoreCase("Q")){
//                        System.out.println("\t\t" + exit.getKey() + "," + exit.getValue());
//                        locFile.writeUTF(exit.getKey());
//                        locFile.writeInt(exit.getValue());
//                    }
//                }
//            }
//        }

//============write by txt=====================
//        try (BufferedWriter locFile = new BufferedWriter(new FileWriter("locations.txt"));
//             BufferedWriter dirFile = new BufferedWriter(new FileWriter("directions.txt"))
//        ) {
//            for (Location location : locations.values()) {
//                locFile.write(location.getLocationID() + "," + location.getDescription() + "\n");
//                for (String direction : location.getExits().keySet()) {
//                    if(!direction.equalsIgnoreCase("Q")){
//                    dirFile.write(location.getLocationID() + "," + direction + "," + location.getExits().get(direction)
//                            + "\n");
//                    }
//                }
//            }
//        }
    }

    static {
        // when reading from Random Access File
        try {
            ra = new RandomAccessFile("locations_rand.dat", "rwd");
            int numLocations = ra.readInt();
            long locationStartPoint = ra.readInt();

            while (ra.getFilePointer() < locationStartPoint) {
                int locationId = ra.readInt();
                int locationStart = ra.readInt();
                int locationLength = ra.readInt();

                IndexRecord record = new IndexRecord(locationStart, locationLength);
                index.put(locationId, record);
            }
        } catch (IOException e) {
            System.out.println("IOException in static initializer" + e.getMessage());
        }


//        reading by object.
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
//        } catch (InvalidClassException e){
//            System.out.println("InvalidClassException "+ e.getMessage());
//        } catch (IOException io){
//            System.out.println("IO Exception " + io.getMessage());
//        } catch(ClassNotFoundException e){
//            System.out.println("ClassNotFoundException " + e.getMessage());
//        }

//========read by binary stream======================
//        try(DataInputStream locFile = new DataInputStream(new BufferedInputStream(new FileInputStream("locations.dat")))){
//            boolean eof = false;
//            while(!eof){
//                try{
//                    Map<String, Integer> exits = new LinkedHashMap<>();
//                    int locID = locFile.readInt();
//                    String description = locFile.readUTF();
//                    int numExits = locFile.readInt();
//                    System.out.println("Read location " + locID + ": " + description);
//                    System.out.println("Found " + numExits + "exits");
//                    for(int i=0; i<numExits;i++){
//                        String direction = locFile.readUTF();
//                        int destination = locFile.readInt();
//                        exits.put(direction, destination);
//                        System.out.println("\t\t" + direction +","+destination);
//                    }
//                    locations.put(locID, new Location(locID, description, exits));
//                } catch (EOFException e){
//                    eof =true;
//                }
//            }
//        } catch (IOException io){
//            System.out.println("IO Exception");
//        }


//========Read from txt by Scanner========================
//        try (Scanner scanner = new Scanner((new BufferedReader(new FileReader("locations_big.txt"))))) {
//            while (scanner.hasNextLine()) {
//                String input = scanner.nextLine();
//                String[] data = input.split(",");
//                int loc = Integer.parseInt(data[0]);
//                String description = data[1];
//                System.out.println("Imported loc: " + loc + ": " + description);
//                Map<String, Integer> tempExit = new HashMap<>();
//                locations.put(loc, new Location(loc, description, tempExit));
//            }
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//
//        // now read the exits
//        try (BufferedReader dirFile = new BufferedReader(new FileReader("directions_big.txt"))) {
//            String input;
//            while ((input = dirFile.readLine()) != null) {
//                // by using String split
//                String[] data = input.split(",");
//                int loc = Integer.parseInt(data[0]);
//                String direction = data[1];
//                int destination = Integer.parseInt(data[2]);
//
//                System.out.println(loc + ": " + direction + ": " + destination);
//                Location location = locations.get(loc);
//                location.addExit(direction, destination);
//            }
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
    }

    public Location getLocation(int locationId) throws IOException {
        IndexRecord record = index.get(locationId);
        ra.seek(record.getStartByte());
        int id = ra.readInt();
        String description = ra.readUTF();
        String exits = ra.readUTF();
        String[] exitPart = exits.split(",");

        Location location = new Location(locationId, description, null);

        if (locationId != 0) {
            for (int i = 0; i < exitPart.length; i++) {
                String direction = exitPart[i];
                int destination = Integer.parseInt(exitPart[++i]);
                location.addExit(direction, destination);
            }
        }

        return location;
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

    public void close() throws IOException {
        ra.close();
    }
}
