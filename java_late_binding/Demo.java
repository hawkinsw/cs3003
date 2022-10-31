class Sauce {
  int spiciness = 5;

  int getSpiciness() {
    return this.spiciness;
  }

  void speakSpicy() {
    // The spiciness here will *always* refer to the Sauce
    // spiciness because field access does not work with
    // late binding. 
    // https://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.11
    System.out.println("I am " + this.spiciness + " spicy (" + this.getClass() + ").");
  }

  void speakSpicySurreptitiously() {
    // In order to get late binding, we are going to have to use
    // a virtual method. That say, getSpiciness() will be the method
    // invoked on the *actual* type of the instance.
    System.out.println("I am " + this.getSpiciness() + " spicy (" + this.getClass() + ").");
  }
}

class SpicySauce extends Sauce {
  int spiciness = 10;

  int getSpiciness() {
    return this.spiciness;
  }
}

public class Demo {
  public static void main(String args[]) {
    Sauce s = new Sauce();
    SpicySauce ss = new SpicySauce();

    s.speakSpicy();
    s.speakSpicySurreptitiously();
    ss.speakSpicy();
    ss.speakSpicySurreptitiously();
  }
}
