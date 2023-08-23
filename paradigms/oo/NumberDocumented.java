/**
 * A class for calculating the integer root of a given number.
 */
public class NumberDocumented {
  /**
   * Construct an instance of the NumberDocumented class.
   * 
   * @param num The number for which to calculate the integer root.
   */
  public NumberDocumented(int num) {
    this.m_num = num;
  }

  /**
   * Calculate the integer root of {@link NumberDocumented#m_num}.
   * Note the similarities between this implementation and the
   * imperative implementation. 
   * @return The integer root of {@link NumberDocumented#m_num}.
   */
  public boolean integerRoot() {
    // Step from 0 (i) until i^2 is bigger than NumberDocumented#m_num ...
    for (int i = 0; (i * i) <= this.m_num; i++) {
      if ((i * i) == this.m_num) {
        return true;
      }
    }
    // ... when the square of i is bigger than NumberDocumented#m_num,
    // our search is hopeless so we'll stop.
    return false;
  }

  /**
   * Demonstrate the NumberDocumented class.
   * 
   * @param args N/A.
   */
  public static void main(String args[]) {
    NumberDocumented rootable = new NumberDocumented(36);

    if (rootable.integerRoot()) {
      System.out.println("We have a root!\n");
    }
  }

  /**
   * The number for which this class calculates the integer root.
   */
  private int m_num;
}
