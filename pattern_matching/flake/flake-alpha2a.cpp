#include <iostream>
#include <random>

bool get_random_bool() {
    std::random_device rd{};
    std::default_random_engine re{rd()};

    std::uniform_int_distribution<int> random_value(1,100);

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
        return MaybeLot::SomeLot(Lot{.car = Matchbox{}});
    }
    return MaybeLot::NoneLot();
}

int main() {
    auto won{bid(42.29, 49)};

    if (won.has_some()) {
        Lot won_lot = won.some();
        std::cout << "I won lot 49!\n";
        std::cout << "The Pokemon has strength: " << won_lot.card.strength << ".\n";
    } else {
        std::cout << "I was outbid.\n";
    }
    return 1;
}
