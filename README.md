# ronin_with_python

Interacting with the Ronin blockchain using Python. 

Main Requirements.
*Python 3.0
*Web.py


Tradedata.get_crypto_price(): 
  runs webscraping of coinmarketcap for eth, slp, axs 
  
 Tradedata.check_balance():
  takes the ronin wallet address as input and reviews the balance of the wallet on each contract 
  
 Tradedata.sum_balance():
  multiplies the assets to the price retrieved from Coinmarketcap, sums all the tradable assets within a wallet and returns a single figure. 
  
 Tradedata.get_axies():
  takes the ronin wallet address as input and returns the amount of axies nfts in the account. 
