import requests

def request(value):
    request = Request()
    return request.search(value).json()

class Request(object):
    def __init__(self, api_url="https://www.humblebundle.com/store/api/humblebundle"):
        self.api_url = api_url
        self.default_querystrings = {
            "request": 3,
            "page_size": 20,
            "sort": "bestselling",
            "page": 0
        }
        
    def search(self, value):
        params = self.default_querystrings.copy()
        params['search'] = value
        return requests.get(self.api_url, params=params)
        
    def _get_raw_game(self, machine_name, game_name):
        """
        As the API stands you cannot request game details specifically.
        This function searches for the game and matches on the machine_name.
        """
        response = self.search(game_name).json()
        for result in response['results']:
            if result['machine_name'] == machine_name:
                return result
        raise RuntimeError("Game '{game_name}' not found.".format(game_name=game_name))
