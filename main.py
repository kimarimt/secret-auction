import os
import time


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print('Welcome to the secret auction program.')
    bids = {}
    again = ''

    while again != 'no':
        bidder = input('Enter your name: ')
        bid = int(input('Enter your bid: $'))
        bids[bidder] = bid
        again = input('\nAre there any other bidders(\'yes\' or \'no\'): ')
        clear()

    winner = ''
    max_bid = 0

    for name, amount in bids.items():
        if amount > max_bid:
            winner = name
            max_bid = amount

    print(f'The winner is {winner} with a bid of ${max_bid:.2f}')


if __name__ == '__main__':
    main()
