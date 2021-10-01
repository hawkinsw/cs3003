struct Book {
  title: String,
}

struct Internet {
  url: String,
}

trait Readable {
  fn read(&self);
}

impl Readable for Internet {
  fn read(&self) {
    println!("I am reading: {}", self.url);
  }
}

impl Readable for Book {
  fn read(&self) {
    println!("I am reading: {}", self.title);
  }
}

fn what_are_you_reading(r: &dyn Readable) {
  r.read();
}

fn main() {
    println!("Hello, world!");

    let internet = Internet{url: "http://www.google.com".to_string()};
    let book = Book{title: "Crying of Lot 49".to_string()};

    what_are_you_reading(&internet);
    what_are_you_reading(&book);
}
