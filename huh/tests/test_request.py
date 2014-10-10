import unittest
import request

class TestPrice(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_request(self):
        r = request.Request()
        r.search("ftl")
        
if __name__ == "__main__":
    unittest.main()
