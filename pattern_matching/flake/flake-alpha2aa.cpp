#include <iostream>
#include <random>

bool get_random_bool() {
  std::random_device rd{};
  std::default_random_engine re{rd()};

  std::uniform_int_distribution<int> random_value(1, 100);

  return random_value(re) % 2 == 0;
}

struct Matchbox {
  int manufacture_year{1949};
};

struct PokemonCard {
  double strength{5000};
};

union Lot {
  Matchbox car;
  PokemonCard card;
};

bool bid(double bid_price, int lot_no, Lot &lot) {
  if (get_random_bool()) {
    lot.car = Matchbox{};
    return true;
  }
  return false;
}

int main() {
  Lot lot{};
  auto won{bid(42.29, 49, lot)};

  if (won) {
    std::cout << "I won lot 49!\n";
    std::cout << "The Pokemon has strength: " << lot.card.strength << ".\n";
  } else {
    std::cout << "I was outbid.\n";
  }
  return 1;
}
