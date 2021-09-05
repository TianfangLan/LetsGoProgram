package lan.learn;

import java.util.HashSet;
import java.util.Set;

public abstract class HeavenlyBody {
    private final Key key;
    private final double orbitalPeriod;
    private final Set<HeavenlyBody> satellites;

    public enum BodyTypes {
        PLANET,
        DWARF_PLANET,
        MOON
    }

    public static final class Key {
        private String name;
        private BodyTypes bodyType;

        private Key(String name, BodyTypes bodyType) {
            this.name = name;
            this.bodyType = bodyType;
        }

        public String getName() {
            return name;
        }

        public BodyTypes getBodyType() {
            return bodyType;
        }

        @Override
        public int hashCode() {
            return this.name.hashCode() + this.bodyType.hashCode() + 17;
        }

        @Override
        public boolean equals(Object obj) {
            // since this class is final there is no subclass
            if (this == obj) {
                // when comparing to itself
                return true;
            }
            if (obj instanceof Key) {
                // both name equal and bodyType will make the key to be equal
                boolean equalName = this.name.equals(((Key) obj).getName());
                boolean equalBodyType = this.bodyType.equals(((Key) obj).getBodyType());
                return equalName && equalBodyType;
            }
            return false;
        }

        @Override
        public String toString() {
            return this.name + ": " + this.bodyType.toString();
        }
    }

    public HeavenlyBody(String name, double orbitalPeriod, BodyTypes bodyType) {
        this.key = new Key(name, bodyType);
        this.orbitalPeriod = orbitalPeriod;
        this.satellites = new HashSet<HeavenlyBody>();
    }

    public Key getKey() {
        return key;
    }

    public boolean addSatellite(HeavenlyBody heavenlyBody) {
        return this.satellites.add(heavenlyBody);
    }

    public double getOrbitalPeriod() {
        return orbitalPeriod;
    }

    public Set<HeavenlyBody> getSatellites() {
        return new HashSet<>(this.satellites);
    }


    @Override
    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        // check if the input object's key is same as the current HeavenlyBody
        if(obj instanceof HeavenlyBody){
            return this.key.equals(((HeavenlyBody) obj).getKey());
        }
        return false;
    }

    @Override
    public final int hashCode() {
        // for not getting a 0 for the hashcode
        // also the number better to be prime
        // also the name of the class won't have the same hash as the String of it's name
        return this.key.hashCode();
    }

    public static Key makeKey(String name, BodyTypes bodyType){
        return new Key(name, bodyType);
    }

    @Override
    public String toString() {
        return this.key.getName() + ": " + this.key.getBodyType() +", " +this.orbitalPeriod;
    }
}
