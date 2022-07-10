import { ThirdwebSDK } from "@thirdweb-dev/sdk";


const sdk = new ThirdwebSDK("mumbai")
const contract = sdk.getNFTCollection("0x1b4ca86C0e779F8A63088664857fe2C64fA11CaB")


class NFT {
    constructor(walletAddress, name, description) {
        this._walletAddress = walletAddress
        this._name = name
        this._description = description
    }

    get walletAddress () {
        return this._walletAddress
    }

    get name () {
        return this._name 
    }

    get description () {
        return this._description
    }

    mint_one() {
        const metadata = {
            'name': this._name,
            'description': this._description,
            'image':'https://www.researchgate.net/profile/Pablo-Fernandez-10/publication/315458901/figure/fig12/AS:541071486996481@1506012903656/Tree-level-Feynman-diagrams-for-coherent-forward-scattering-of-neutrinos-on-any.png'
        }
        return metadata
    }

    async fetch_all_nfts () {
        const nfts = await contract.getAll();
        console.log(nfts)
    }
}





const test = new NFT('0x127a95027B5c7E1D807433837C9cDD7e6f336803', 'hi', 'test desc')

const metadata = test.mint_one()
const tx = await contract.mintTo('0x127a95027B5c7E1D807433837C9cDD7e6f336803', metadata)
const receipt = tx.receipt;
//const tokenId = tx.id
//const nft_data = await tx.data();
