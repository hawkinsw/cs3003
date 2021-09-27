abstract class Mammal {
  protected int legs = 0;
  Mammal() {
    legs = 0;
  }
  abstract void makeNoise();
}

class Dog extends Mammal {
  Dog() {
    super();
    legs = 4;
  }
  void makeNoise() {
    System.out.println("bark");
  }
}

class Cat extends Mammal {
  Cat() {
    super();
    legs = 4;
  }
  
  void makeNoise() {
    System.out.println("meow");
  }
}

public class MammalDemo {
  static void makeARuckus(Mammal m) {
    m.makeNoise();
  }
  public static void main(String args[]) {
    Dog fido = new Dog();
    Cat checkers = new Cat();
    
    makeARuckus(fido);
    makeARuckus(checkers);
  }
}
