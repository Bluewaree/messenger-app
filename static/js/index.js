$(document).ready(function(){
    if ($('.messages_container').length > 0) {
        scroll_down();
    };
});

var ws_url = "ws://" + ws_url;
var ws = new ReconnectingWebSocket(ws_url);
var form = $("#message-form");
var input = $("#message");

ws.onmessage = e => {
    var message = JSON.parse(e.data)["data"];
    append_message(message["message"], message["username"]);
    scroll_down();
}

ws.onopen = e => {
    form.submit(e => {
        e.preventDefault();
        let message = input.val();
        let payload = {
            "message": message,
            "username": username 
        };
        ws.send(JSON.stringify(payload));
        input.val("");
    })
}

let append_message = (message, usrname) => {
    let messages_container = $(".messages-container");
    let date = new Date();
    date = moment(date).format("YYYY-MM-DD HH:mm");
    messages_container.append(`
        <div container message_container>
            <p class="message-headers">`+usrname+`: <label>`+date+`</label></p>    
            <p class="message">`+message+`</p>    
        </div>
    `);
}

let scroll_down = () => {
    $('.messages-container').scrollTop($('.messages-container')[0].scrollHeight);
}
