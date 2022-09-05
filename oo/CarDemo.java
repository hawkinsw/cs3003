class Car {
  protected boolean electric = false;
  protected int wheels = 4;

  Car() {
  }

  void start() {
    System.out.println("Starting a car ...");
    if (this.ignite()) {
      System.out.println("Ignited the engine!");
    } else {
      System.out.println("Did NOT ignite the engine!");
    }
  }

  public boolean ignite() {
      System.out.println("Igniting a generic car's engine!");
      return true;
  }
}

class Tesla extends Car {
  Tesla() {
    super();
    electric = true;
  }

  @Override
  public boolean ignite() {
    super.ignite();
    System.out.println("Igniting a Tesla's engine!");
    return true;
  }
}

class Chevrolet extends Car {
  Chevrolet() {
    super();
  }

  @Override
  public boolean ignite() {
    super.ignite();
    System.out.println("Igniting a Chevrolet's engine!");
    return false;
  }
}

class Volt extends Chevrolet {
  @Override
  public boolean ignite() {
    System.out.println("Volt!");
    return true;
  }
}

public class CarDemo {
  public static void main(String args[]) {
    Car c = new Car();
    Car t = new Tesla();
    Car v = new Chevrolet();
    Car vv = new Volt();

    c.ignite();
    t.ignite();
    v.ignite();
    vv.ignite();
  }
}
