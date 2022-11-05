class Vehicle {
    public int getWheelCount() {
        return 0;
    }
}

class Car extends Vehicle {
    public int getDoorCount() {
        return 2;
    }

    public int getWheelCount() {
        return 4;
    }
}

class Motorcyle extends Vehicle {
    public int getWheelCount() {
        return 2;
    }
}

class Rivian extends Car {
    public int getDoorCount() {
        return 4;
    }
} 

class Mercedes extends Car {
    public int getDoorCount() {
        return 2;
    }

    public int getWheelCount() {
        return 4;
    }
}

public class Vimple {
    public static void main(String args[]) {
        Rivian r = new Rivian();
        Mercedes m = new Mercedes();

        System.out.println("Mercedes have " + Integer.toString(m.getDoorCount()) + " doors.\n");
        System.out.println("Rivians have " + Integer.toString(m.getWheelCount()) + " wheels.\n");

    }
}