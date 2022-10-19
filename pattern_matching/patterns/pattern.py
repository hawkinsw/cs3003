class Vehicle():
  model: str
  year: int

  def __init__(self, model: str, year: int) -> None:
    self.model = model
    self.year = year

class SUV(Vehicle):
  def __init__(self, model: str, year: int) -> None:
    super().__init__(model, year)

class Wagon(Vehicle):
  def __init__(self, model: str, year: int) -> None:
    super().__init__(model, year)

def specific_printer(vehicle: Vehicle) -> None:
  match vehicle:
    case Wagon(model=model, year=year):
      print(f"(p) This station wagon ({model}) is from {year}")
    case SUV(model=model, year=year):
      print(f"(p) This station wagon ({model}) is from {year}")
    case Vehicle(model=model, year=year):
      print(f"(p) This generic vehicle ({model}) is from {year}")

def demo() -> None:
  v = Vehicle("Model S", 2019)
  s = SUV("GLE", 2022)
  w = SUV("V60", 2022)

  specific_printer(v)
  specific_printer(s)
  specific_printer(w)

