class Parent {
  Parent() {
    System.out.println("I am in the Parent constructor.");
  }

  Parent(int parameter) {
    System.out.println("This version of the constructor is not called.");
  }
}

class Child extends Parent {
  Child() {
    /*
     * No explicit call to super -- one is automatically
     * injected to the parent constructor with no parameters.
     */
    System.out.println("I am in the Child constructor.");
  }
}

public class DefaultConstructor {
  public static void main(String args[]) {
    Child c = new Child();
  }
}
