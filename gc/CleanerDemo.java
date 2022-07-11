import java.lang.System;
import java.lang.ref.Cleaner;

class Counter {
  public static int counter = 0;
}

class Q {
  static class QCleaner implements Runnable {
    QCleaner(int creationGeneration) {
      mCreationGeneration = creationGeneration;
    }

    public void run() {
      System.out.println(String.format("A Q from generation %d is being cleaned after %d generations.", mCreationGeneration, Counter.counter));
    }
    private int mCreationGeneration;
  }

  Q() {
    int a[] = new int[100000000];
    cleaner = Cleaner.create();
    cleaner.register(this, new Q.QCleaner(Counter.counter));
  }

  private Cleaner cleaner;
}


public class CleanerDemo {
  static void use_a_q() {
    Q cue = new Q();
  }

  public static void main(String args[]) {
    for (int i = 0; true; i++) {
      use_a_q();
      int[] a = new int[10000];
      Counter.counter++;
      try {
        Thread.sleep(1);
      } catch (Exception e) {}
    }
  }
}
