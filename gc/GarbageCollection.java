import java.lang.System;
import java.util.Vector;
import java.util.List;

class Counter {
  public static int counter = 0;
}

class O {
  O() {
    int[] a = new int[OSIZE];
    generation = Counter.counter;
  }

  private int generation;
  static public final int OSIZE = 10000000;

  protected void finalize() {
    System.out.println(String.format("We are done with %d after %d iterations.", generation, Counter.counter));
  }
}


public class GarbageCollection {
  static public final int ASIZE = 100000;
  
  public static void main(String args[]) {
    List<int[]> larray = new Vector<int[]>();
    for (int i = 0; true; i++) {
      O no = new O();
      int[] a = new int[ASIZE];
      larray.add(a);
      //System.gc();
      Counter.counter++;
      try {
        java.lang.Thread.sleep(400);
      } catch (InterruptedException iex) {
        // Don't need to do anything.
      }
    }
  }
}
