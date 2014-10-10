import unittest

import wishlist
import model

def generate_game(**kwargs):
    default_params = {
        "machine_name": "foo",
        "human_name": "bar",
        "full_price": model.Price(**{
            "price": 12.00,
            "currency": "GBP"
        }),
        "current_price": model.Price(**{
            "price": 12.00,
            "currency": "GBP"
        }),
        "os": [
            "linux",
            "windows"
        ],
        "platform": [
            "download"
        ]
    }
    default_params.update(kwargs)
    return model.Game(**default_params)
    
def generate_wishlist_game(**kwargs):
    default_params = {
        "machine_name": "foo",
        "human_name": "bar",
        "price": model.Price(**{
            "price": 12.00,
            "currency": "GBP"
        }),
        "os": "linux",
        "platform": "download"
    }
    default_params.update(kwargs)
    return wishlist.WishlistGame(**default_params)

class TestWishlistGame(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_os_compare(self):
        # wishlist os exists in game
        wlgame_1 = generate_wishlist_game()
        game_1 = generate_game()
        
        self.assertTrue(wlgame_1.compare_os_to(game_1))
        
        # wishlist os does not exist in game
        wlgame_2 = generate_wishlist_game()
        game_2 = generate_game(os=['windows'])
        
        self.assertFalse(wlgame_2.compare_os_to(game_2))

if __name__ == "__main__":
    unittest.main()
