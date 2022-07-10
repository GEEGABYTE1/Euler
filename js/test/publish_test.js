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
}

const test = new NFT('0xec2a636B21E2935897DB0D779A66221A82B4fd02', 'hi', 'test desc')
console.log(test.description)