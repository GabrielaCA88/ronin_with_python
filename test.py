import unittest
from tradedata import Tradedata
class TestStringMethods(unittest.TestCase):    

    def test_prices(self):
        mytd = Tradedata()
        mytd.get_crypto_price()
        self.assertEqual(mytd.slp_US>0, True)
        self.assertEqual(mytd.eth_US>0, True)
        self.assertEqual(mytd.axs_US>0, True)        

    def test_balances(self):
        mytd = Tradedata()
        addr="0xa8754b9fa15fc18bb59458815510e40a12cd2014"
        for ccy in ["slp", "axs","axies", "weth"] :
            balance = mytd.check_balance(addr,ccy)
            self.assertEqual(balance >= 0 , True)

    def test_sumbalance(self):
        mytd = Tradedata()
        mytd.get_crypto_price()
        addr="0xa8754b9fa15fc18bb59458815510e40a12cd2014"
        self.assertEqual(mytd.sum_balance(addr)>=0, True)

if __name__ == '__main__':
    unittest.main()