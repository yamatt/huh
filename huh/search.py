#!/usr/bin/env python
import model
from request import Request
import sys

def get_args():
    return sys.argv[1]

if __name__ == "__main__":
    hib = Request()
    results = hib.search(get_args())
    for game in map(lambda result: model.Game.from_hib(**result), results.json()['results']):
        print("{game}: ({id}) at {price:.2f}{currency}".format(game=game.name, id=game.id, price=game.price.value, currency=game.price.currency))
