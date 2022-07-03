from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
from dotenv import load_dotenv
import os


load_dotenv()

class NFT:
    PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
    network = os.environ.get('API_URL')
    sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

    def create(self):
        NFT_COLLECTION_ADDRESS = '0x1b4ca86C0e779F8A63088664857fe2C64fA11CaB'
        nft_collection = self.sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)
        nft_collection.mint(NFTMetadataInput.from_json({
            "name": "test2",
            "description": "Path Test",
            "image": "https://cdn.jpegmini.com/user/images/slider_puffin_before_mobile.jpg" # Takes Weblinks
        }))
        print('Completed')
        #print(nft_collection.balance())


nft = NFT()

print(nft.create())