from bs4 import BeautifulSoup
import requests
from web3 import Web3


class Tradedata():
    def __init__(self):
        self.eth = 'ethereum'
        self.slp = 'smooth-love-potion'
        self.axs = 'axie-infinity'
        self.SLP_CONTRACT = "0xa8754b9fa15fc18bb59458815510e40a12cd2014"
        self.AXS_CONTRACT = "0x97a9107c1793bc407d6f527b77e7fff4d812bece"
        self.AXIE_CONTRACT = "0x32950db2a7164ae833121501c797d79e7b79d74c"
        self.WETH_CONTRACT = "0xc99a6a985ed2cac1ef41640596c5a5f9f4e19ef5"
        self.RONIN_PROVIDER = "https://api.roninchain.com/rpc"
        self.USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36"

    def get_crypto_price(self):
        # Ethereum price
        eth_url = 'https://coinmarketcap.com/es/currencies/' + self.eth + '/'
        HTML = requests.get(eth_url)
        soup = BeautifulSoup(HTML.text, 'html.parser')
        eth_price = (soup.find('div', attrs={'class': 'sc-16r8icm-0 kjciSH priceTitle'}).find('div', attrs={
            'class': 'priceValue'}).text).strip('$')

        # SLP price
        slp_url = 'https://coinmarketcap.com/es/currencies/' + self.slp + '/'
        HTML = requests.get(slp_url)
        soup = BeautifulSoup(HTML.text, 'html.parser')
        slp_price = (soup.find('div', attrs={'class': 'sc-16r8icm-0 kjciSH priceTitle'}).find('div', attrs={
            'class': 'priceValue'}).text).strip('$')

        # AXS price
        axs_url = 'https://coinmarketcap.com/es/currencies/' + self.axs + '/'
        HTML = requests.get(axs_url)
        soup = BeautifulSoup(HTML.text, 'html.parser')
        axs_price = (soup.find('div', attrs={'class': 'sc-16r8icm-0 kjciSH priceTitle'}).find('div', attrs={
            'class': 'priceValue'}).text).strip('$')

        # to_float
        self.eth_US = float(eth_price.replace(',', ''))
        self.slp_US = float(slp_price.replace(',', ''))
        self.axs_US = float(axs_price.replace(',', ''))

    def check_balance(self, account, token='slp'):
        if token == 'slp':
            contract = self.SLP_CONTRACT
        elif token == 'axs':
            contract = self.AXS_CONTRACT
        elif token == "axies":
            contract = self.AXIE_CONTRACT
        elif token == "weth":
            contract = self.WETH_CONTRACT
        else:
            return 0

        BALANCE_ABI = [{
            'constant': True,
            'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
            'name': 'balanceOf',
            'outputs': [{'internalType': 'uint256', 'name': '',
                         'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function',
        }]

        w3 = Web3(
            Web3.HTTPProvider(
                self.RONIN_PROVIDER,
                request_kwargs={
                    "headers": {"content-type": "application/json",
                                "user-agent": self.USER_AGENT}}))
        ctr = w3.eth.contract(
            address=Web3.toChecksumAddress(contract),
            abi=BALANCE_ABI
        )
        balance = ctr.functions.balanceOf(
            Web3.toChecksumAddress(account.replace("ronin:", "0x"))
        ).call()
        if token == 'weth':
            return float(balance / 1000000000000000000)
        return int(balance)

    def sum_balance(self, account):
        if self.check_balance(account, 'weth') != 0:
            self.sum_eth = self.eth_US * (self.check_balance(account, 'weth'))
        else:
            self.sum_eth = 0
        if self.check_balance(account, 'axs') != 0:
            self.sum_axs = self.axs_US * (self.check_balance(account, 'axs'))
        else:
            self.sum_axs = 0
        if self.check_balance(account, 'slp') != 0:
            self.sum_slp = self.slp_US * (self.check_balance(account, 'slp'))
        else:
            self.sum_slp = 0

        sum_all = (self.sum_eth + self.sum_axs + self.sum_slp)

        return sum_all

    def get_axies(self, account):
        if self.check_balance(account, 'axies') != 0:
            return (self.check_balance(account, 'axies'))
        else:
            return 'no axies'