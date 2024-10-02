#include <iostream>

struct Matchbox {
    int manufacture_year{};
};


struct PokemonCard {
    double strength{};
};

union Lot {
    Matchbox car;
    PokemonCard card;
};

bool bid(double bid_price, int lot_no, Lot &lot) {
    lot.card = PokemonCard{};
    return true;
}

int main() {
    Lot lot{};
    int won{bid(42.29, 49, lot)};

    if (won) {
        // I know that I won, but how do I get
        // access to what I won?
        std::cout << "I won lot 49!\n";
    } else {
        std::cout << "I was outbid.\n";
    }
    return 1;
}
