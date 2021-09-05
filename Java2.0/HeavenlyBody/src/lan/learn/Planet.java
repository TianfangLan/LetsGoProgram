package lan.learn;

public class Planet extends HeavenlyBody{

    public Planet(String name, double orbitalPeriod) {
        super(name, orbitalPeriod, BodyTypes.PLANET);
    }

    @Override
    public boolean addSatellite(HeavenlyBody heavenlyBody) {
        if (heavenlyBody.getKey().getBodyType() == BodyTypes.MOON){
            return super.addSatellite(heavenlyBody);
        }
        return false;
    }
}
