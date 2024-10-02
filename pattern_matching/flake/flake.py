from typing import Optional
from typing import Union
import random

class Matchbox:
    manufacture_year: int
    def __init__(self):
        self.manufacture_year = 0

class PokemonCard:
    strength: float
    def __init__(self):
        self.strength = 0

class Lot(object):
    lot: Union[PokemonCard, Matchbox]

    def __init__(self):
        self.lot = PokemonCard()

def bid(bid_price: float, lot_no: int) -> Optional[Lot]:
    randomizer = random.Random()
    won = randomizer.randint(1,100) % 2 == 0
    if won:
        pokemon_won = randomizer.randint(1,100) % 2 == 0
        lot: Lot = Lot()
        if pokemon_won:
            lot.lot = PokemonCard()
            lot.lot.strength = 5000
        else:
            lot.lot = Matchbox()
            lot.lot.manufacture_year = 1949
        return lot
    else:
        return None

if __name__=="__main__":
    maybe_won_lot = bid(42.29, 49)    
    if maybe_won_lot != None:
        match maybe_won_lot.lot:
            case PokemonCard(strength=s):
                print(f"I am a pokemon card with strength {s}.")
            case Matchbox(manufacture_year=my):
                print(f"I am a matchbox manufactured in {my}.")
    else:
        print("I got outbid!")
