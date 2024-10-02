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

bool bid(double bid_price, int lot_no) {
    return true;
}

int main() {
    int won{bid(42.29, 49)};

    if (won) {
        // I know that I won, but how do I get
        // access to what I won?
        std::cout << "I won lot 49!\n";
    } else {
        std::cout << "I was outbid.\n";
    }
    return 1;
}
