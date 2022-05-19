public class Number {
  public Number(int num) {
    this.m_num = num;
  }

  public boolean integerRoot() {
    for (int i = 0; (i * i) <= this.m_num; i++) {
      if ((i * i) == this.m_num) {
        return true;
      }
    }
    return false;
  }
  public static void main(String args[]) {
    Number rootable = new Number(36);

    if (rootable.integerRoot()) {
      System.out.println("We have a root!\n");
    }
  }

  private int m_num;
}
