document.addEventListener('DOMContentLoaded', () => {
    let ws;

    const handleWsClick = function (event) {
        appendMessage(event.data)
    }

    document.querySelector('#btn').addEventListener('click', function () {
        const input = document.querySelector("#name")
        const client_name = input.value

        const parent = this.parentNode
        parent.removeChild(this)
        input.disabled = true

        ws = new WebSocket(`${protocol}://${server}/ws/${client_name}`)
        ws.addEventListener('message', handleWsClick);
    });

    let messagesBlock = document.getElementById('messages')
    function appendMessage(msg) {
        let message = document.createElement('li')
        let content = document.createTextNode(msg)
        message.append(content)
        messagesBlock.append(message)
    }

    let input = document.getElementById("messageText")
    document.querySelector('#form').addEventListener('submit', function sendMessage(event) {
        event.preventDefault()

        ws.send(input.value)
        input.value = ''
    })
})