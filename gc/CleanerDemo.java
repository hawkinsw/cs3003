import java.lang.System;
import java.lang.ref.Cleaner;

class Counter {
  public static int counter = 0;
}

class O {
  O() {
    System.out.println("This is an O constructor!");
  }
}

class OCleaner implements Runnable {
  public void run() {
    System.out.println("O is being cleaned after " + Counter.counter + " iterations.");
  }
}

public class CleanerDemo {
  static void use_an_o() {
    Cleaner cleaner = Cleaner.create();
    O ohh = new O();
    cleaner.register(ohh, new OCleaner());
    ohh = null;
  }

  public static void main(String args[]) {
    use_an_o();
    for (int i = 0; true; i++) {
      int[] a = new int[10000];
      Counter.counter++;
      try {
        Thread.sleep(1);
      } catch (Exception e) {}
    }
  }
}
