import unittest
import response

class TestPrice(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_compare_same_currency(self):
        price1 = response.Price(**{
            "price": 1.00,
            "currency": "GBP"
        })
        price2 = response.Price(**{
            "price": 2.00,
            "currency": "GBP"
        })
        
        self.assertTrue(price1<price2)
        self.assertFalse(price1>price2)
        self.assertFalse(price1>price1)
        
    def test_compare_different_currency(self):
        price1 = response.Price(**{
            "price": 1.00,
            "currency": "USD"
        })
        price2 = response.Price(**{
            "price": 2.00,
            "currency": "GBP"
        })
        
        
        
        
if __name__ == "__main__":
    unittest.main()
