from request import request

def responses(value):
    return map(lambda response: Response(**response), request(value))

class Game(object):
    @classmethod
    def from_hib(cls, **kwargs):
        kwargs['current_price'] = Price.from_hib(kwargs['current_price'])
        kwargs['full_price'] = Price.from_hib(kwargs['full_price'])
        kwargs['os'] = kwargs['platforms']
        kwargs['platforms'] = kwargs['delivery_methods']
        
        return cls(**kwargs)
        
    def __init__(self, **kwargs):
        self.id = kwargs['machine_name']
        self.name = kwargs['human_name']
        self.current_price = kwargs['current_price']
        self.full_price = kwargs['full_price']
        self.os = kwargs['os']
        self.platforms = kwargs['platforms']
        
class Price(object):
    @classmethod
    def from_hib(cls, array):
        return cls(**{
            "price": array[0],
            "currency": array[1],
        })
        
    def __init__(self, *args, **kwargs):
        self.value = kwargs['price']
        self.currency = kwargs['currency']
        
    def __cmp__(self, other):
        if other.currency == self.currency:
            if self.value < other.value:
                return -1
            elif self.value > other.value:
                return 1
            else:
                return 0
        else:
            raise NotImplemented("Mixed currencies cannot be compared")
