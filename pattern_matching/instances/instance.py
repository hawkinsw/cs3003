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
  if isinstance(vehicle, Wagon):
    model = vehicle.model
    year = vehicle.year
    print(f"This station wagon ({model}) is from {year}")
  elif isinstance(vehicle, SUV):
    model = vehicle.model
    year = vehicle.year
    print(f"This SUV ({model}) is from {year}")
  else:
    model = vehicle.model
    year = vehicle.year
    print(f"This generic vehicle ({model}) is from {year}")

def demo() -> None:
  v = Vehicle("Model S", 2019)
  s = SUV("GLE", 2022)
  w = SUV("V60", 2022)

  specific_printer(v)
  specific_printer(s)
  specific_printer(w)