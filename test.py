import unittest
from tradedata import Tradedata
class TestStringMethods(unittest.TestCase):    

    def test_prices(self):
        mytd = Tradedata()
        mytd.get_crypto_price()
        self.assertEqual(mytd.slp_US>0, True)
        self.assertEqual(mytd.eth_US>0, True)
        self.assertEqual(mytd.axs_US>0, True)        


if __name__ == '__main__':
    unittest.main()