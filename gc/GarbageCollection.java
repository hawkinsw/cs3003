import java.lang.System;
import java.util.Vector;

class Counter {
  public static int counter = 0;
}

class O {
  O() {
    System.out.println("This is an O constructor!");
  }

  protected void finalize() {
    System.out.println("We are done with this object after " + Counter.counter + " iterations!");
  }
}

public class GarbageCollection {
  static void use_an_o() {
    new O();
    System.gc();
  }

  public static void main(String args[]) {
    use_an_o();
    for (int i = 0; true; i++) {
      int[] a = new int[100000];
      System.gc();
      Counter.counter++;
      try {
        Thread.sleep(400);
      } catch (Exception e) {}
    }
  }
}
