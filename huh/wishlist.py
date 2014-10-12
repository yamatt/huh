from config import Config
import model

class WishlistConfig(Config):
    DEFAULT_FILE = "~/.huh-wishlist.yaml"
    
class WishlistGame(model.Game):
    @classmethod
    def from_config(cls, **kwargs):
        if kwargs.get("price"):
            kwargs['requested_price'] = model.Price(**kwargs)
        return cls(**kwargs)
        
    def __init__(self, **kwargs):
        self.id = kwargs['machine_name']
        self.name = kwargs['human_name']
        self.price = kwargs.get('requested_price')
        self.os = kwargs.get('os')
        self.platform = kwargs.get('platform')
        
    def compare_price_to(self, game):
        """
        Compares the price of this game to the one in the request_obj system (could be HIB, Steam etc.)
        """
        return game.current_price <= self.price
        
    def compare_os_to(self, game):
        return self.os in game.os
        
    def compare_platform_to(self, game):
        return self.platform in game.platforms
        
    def compare(self, game):
        if self.price and not self.compare_price_to(game):
            return False
            
        if self.os and not self.compare_os_to(game):
            return False
            
        if self.platform and not self.compare_platform_to(game):
            return False
            
        return True
        
    def get_matching_game(self, request_obj):
        raw_game = request_obj._get_raw_game(self.id, self.name)
        return model.Game.from_hib(**raw_game) # this line will be the first to go when the revolution comes
    
class Wishlist(object):
    @classmethod
    def get_games(cls):
        return cls.get_games_from_config(WishlistConfig.auto_load())
        
    @classmethod
    def get_games_from_config(cls, config):
        return cls(
            map(lambda game: WishlistGame.from_config(**game), config.games)
        )
    
    def __init__(self, games):
        self.games = games
