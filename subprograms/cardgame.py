import random

class Winner(BaseException):
    def __init__(self, winner_name):
        self.winner_name = winner_name

def deal(seed = None, shoe_size = 10):
    random.seed(seed)
    num_draws = 0
    while num_draws < shoe_size:
        yield random.randint(1, 10)
        num_draws += 1

def player(next_player, name, to_win, dealer):
    total = 0
    while True:
        try:
            total += next(dealer)

            if (total > to_win):
                raise Winner(f"{name}")

            # When there is no next player, simply
            # yield None. This will percolate back
            # to the top and signal that a new round
            # should start.
            if next_player == None:
                yield None
            else:
                yield next(next_player)

        except StopIteration as e:
            """ This will happen when we next(dealer) 
                and they are completely out of draws. 
                In other words, when we next() a coroutine
                that has finished, we get the StopIteration
                exception """
            break

if __name__=='__main__':
    to_win = 20
    rnd = 1
    dealer = deal(None, 3*5)
    # player_c does not have a next player -- None
    # indicates that the process returns to the loop (below)
    # that will start the next round!
    player_c = player(None, "C", to_win, dealer)
    player_b = player(player_c, "B", to_win, dealer)
    player_a = player(player_b, "A", to_win, dealer)

    while True:
        try:
            print(f"Starting round {rnd}.")
            next(player_a)
            rnd += 1
        except StopIteration as e:
            print(f"After {rnd} rounds, there was no winner!")
            break
        except Winner as w:
            print(f"Player {w.winner_name} won in round {rnd}!")
            break
