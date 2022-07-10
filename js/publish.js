let data = []
const inputWalletAddress = document.getElementById("input-nft-address")
const inputNotificationMessage = document.getElementById("input-notification-message")
const sendBtn = document.getElementById("send-btn")
let savedData = document.getElementById("saved-data")
const note = "Published to Marketplace"

sendBtn.addEventListener("click", function() {
    data.push(inputWalletAddress.value)
    savedData.innerText = note
    console.log(data)
}) 