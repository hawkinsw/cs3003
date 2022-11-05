class Readable {
  String isbn;

  public Readable(String isbn) {
    this.isbn = isbn;
  }

  public String getISBN() {
    return this.isbn;
  }

  public String getTesting() {
    return this.isbn;
  }
}

class Periodical extends Readable {
  String title;

  public Periodical(String isbn, String title) {
    super(isbn);
    this.title = title;
  }

  public String getAitle() {
    return this.title;
  }
}

enum Medium {
  Print,
  Electronic;

  public String toString() {
    if (this == Print) {
      return "Print";
    } else if (this == Electronic) {
      return "Electronic";
    }
    return "Unknown";
  }
}


class Newspaper extends Periodical {
  Medium medium;
  public Newspaper(String isbn, String title, Medium medium) {
    super(isbn, title);
    this.medium = medium;
  }

  @Override
  public String getAitle() {
    return this.title;
  }
}

public class Deep {
  public static void main(String args[]) {
    Newspaper wsj = new Newspaper("13", "Wall Street Journal", Medium.Print);
    System.out.println(wsj.getISBN());
    //System.out.println(wsj.getMedium());
    System.out.println(wsj.getAitle());
    System.out.println(wsj.getAitle());
    System.out.println(wsj.getAitle());
  }
}
