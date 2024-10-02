#include <iostream>

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

bool bid(double bid_price, int lot_no, Lot &lot) {
    lot.Lot.card = PokemonCard{};
    lot.type = Lot::Type::PokemonCard;
    return true;
}

int main() {
    Lot lot{};
    int won{bid(42.29, 49, lot)};

    if (won) {
        // I know that I won, but how do I get
        // access to what I won?
        std::cout << "I won lot 49!\n";

        switch (lot.type) {
            case Lot::Type::Matchbox: {
                std::cout << "It is a Matchbox car that was original produced in " << lot.Lot.car.manufacture_year << ".\n";
            }
            case Lot::Type::PokemonCard: {
                std::cout << "It is a Pokemon card whose character has strength " << lot.Lot.card.strength << ".\n";
            }
        }

    } else {
        std::cout << "I was outbid.\n";
    }
    return 1;
}
