from lib2to3.pgen2 import token
from thirdweb import ThirdwebSDK
from thirdweb.types import NewDirectListing
from dotenv import load_dotenv
import os

load_dotenv()

class Marketplace:
    sdk = ThirdwebSDK.from_private_key(os.environ.get("PRIVATE_KEY"), os.environ.get('API_URL'))
    marketplace_address = os.environ.get("MARKETPLACE_CONTRACT_ADDRESS")
    marketplace = sdk.get_marketplace(marketplace_address)

    def create_listing(self):
        asset_contract_address = '0x127a95027B5c7E1D807433837C9cDD7e6f336803'
        token_id=12 # Arithmetic Increment/Index on the list of NFTS that we need to fetch
        start_time_in_seconds = 10
        listing_duration_in_seconds = 180
        quantity = 1
        currency_contract_address = os.environ.get('TOKEN_ADDRESS')
        buyout_price_per_token = 0.5

        
        self.marketplace.direct.create_listing(NewDirectListing(
            asset_contract_address=asset_contract_address,
            token_id=token_id,
            start_time_in_seconds=start_time_in_seconds,
            listing_duration_in_seconds=listing_duration_in_seconds,
            quantity=quantity,
            currency_contract_address=currency_contract_address,
            buyout_price_per_token=buyout_price_per_token
        ))
        print('Success')

class Token:
    PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
    network = os.environ.get("API_URL")
    sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network) 
    token_module = sdk.get_currency_module(os.environ.get('TOKEN_ADDRESS')) 
    deployer_address = os.environ.get('DEPLOYER_ADDRESS')

    def mint_token(self):
        toAddress = '0xec2a636B21E2935897DB0D779A66221A82B4fd02'    # Any Address
        amount = 1
        self.token_module.transfer(toAddress, amount)

    def get_token_balance(self):  
        balance = self.token_module.balanceOf(self.deployer_address)  
        print('Balance of Deployer: {} Euler Tokens'.format(balance))

    def get_allowance(self, other_address):
        allowance = self.token_module.allowance_of(self.deployer_address, other_address)
        print('{otherAddress} Balance: {amount}'.format(otherAddress=other_address, amount=allowance))
    

