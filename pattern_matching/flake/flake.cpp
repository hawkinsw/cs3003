#include <iostream>
#include <random>

bool get_random_bool() {
  std::random_device rd{};
  std::default_random_engine re{rd()};

  std::uniform_int_distribution<int> random_value(1, 100);

  return random_value(re) % 2 == 0;
}

struct Matchbox {
  int manufacture_year{};
};

struct PokemonCard {
  double strength{};
};

struct Lot {
  enum class Type {
    Matchbox,
    PokemonCard,
  };

  Type type;
  union {
    Matchbox car;
    PokemonCard card;
  } Lot;
};

struct MaybeLot {
  Lot lot;
  bool _some{false};

  void set(Lot lot) {
    _some = true;
    this->lot = lot;
  }

  void reset() {
    // More would be required here.
    _some = false;
  }

  Lot some() { return lot; }
  bool has_some() { return _some; }

  static MaybeLot SomeLot(Lot lot) {
    MaybeLot ml{};
    ml._some = true;
    ml.lot = lot;

    return ml;
  }

  static MaybeLot NoneLot() { return MaybeLot{}; }
};

MaybeLot bid(double bid_price, int lot_no) {
  if (get_random_bool()) {
    Lot lot{};
    if (get_random_bool()) {
      lot.Lot.card = PokemonCard{.strength = 5000};
      lot.type = Lot::Type::PokemonCard;
    } else {
      lot.Lot.car = Matchbox{.manufacture_year = 1949};
      lot.type = Lot::Type::Matchbox;
    }
    return MaybeLot::SomeLot(lot);
  } else {
    return MaybeLot::NoneLot();
  }
}

int main() {
  auto maybe_won_lot{bid(42.29, 49)};

  if (maybe_won_lot.has_some()) {
    auto lot = maybe_won_lot.some();
    std::cout << "I won lot 49!\n";

    switch (lot.type) {
    case Lot::Type::Matchbox: {
      std::cout << "It is a Matchbox car that was originally produced in "
                << lot.Lot.car.manufacture_year << ".\n";
      break;
    }
    case Lot::Type::PokemonCard: {
      std::cout << "It is a Pokemon card whose character has strength "
                << lot.Lot.card.strength << ".\n";
      break;
    }
    }

  } else {
    std::cout << "I was outbid.\n";
  }
  return 1;
}


