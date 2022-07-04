from ast import Index
from lib2to3.pgen2 import token
from thirdweb import ThirdwebSDK
from thirdweb.types import NewDirectListing
from dotenv import load_dotenv
import os

load_dotenv()

class Marketplace:
    sdk = ThirdwebSDK.from_private_key(os.environ.get("PRIVATE_KEY"), os.environ.get('API_URL'))
    marketplace_address = os.environ.get("MARKETPLACE_CONTRACT_ADDRESS")
    marketplace = sdk.get_marketplace('0xdDD8F1656Ef89bB1FbA161265dcB8a70a91f6E0A')

    def create_listing(self):
        asset_contract_address = '0x1b4ca86C0e779F8A63088664857fe2C64fA11CaB'
        token_id=11 # Arithmetic Increment/Index on the list of NFTS that we need to fetch
        start_time_in_seconds = 20
        listing_duration_in_seconds = 1800
        quantity = 1
        currency_contract_address = '0x9c3C9283D3e44854697Cd22D3Faa240Cfb032889'
        buyout_price_per_token = 0.5

        try:
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
        except IndexError:
            print(IndexError)
            print('Regardless, it was a success')
    
    def buy(self):
        listing_id = 2
        quantity_desired = 1
        self.marketplace.buyout_listing(listing_id, quantity_desired)

    def get_all_listings(self):
        listings = self.marketplace.get_all_listings()
        return listings




marketplace = Marketplace()
#marketplace.create_listing() 
print(marketplace.get_all_listings())