var express = require('express');
var socket = require('socket.io');
var axios = require('axios');

var app = express();


server = app.listen(5000, function () {
    console.log('server is running on port 5000')
});

io = socket(server);

postMessage = (message, author) => {
    var braggi_out;
    axios.post('http://127.0.0.1:8000/braggi/', {
        id: "",
        username: author,
        user_in: message,
        braggi_out: "-BLANK-",
        intent: "greetings",
        invoked_event: "greetings"
  })
  .then(function (response) {
    console.log("Response : ", response.data.braggi_out);
    data = {author : "Braggi", message : response.data.braggi_out}
    io.emit('RECEIVE_MESSAGE', data);
  })
}

io.on('connection', (socket) => {
    console.log(socket.id);
    var msg;

    socket.on('SEND_MESSAGE', function (data) {
        io.emit('RECEIVE_MESSAGE', data);
        console.log(data);
        //console.log(data.message)
        postMessage(data.message, data.author);
    })
});

/* 
axios.post('http://127.0.0.1:8000/braggi/', {
        id: "",
        username: "Batman",
        user_in: "Hi there!!",
        braggi_out: "See you later",
        intent: "greetings",
        invoked_event: "greetings"
  })
  .then(function (response) {
    console.log(response);
  })
*/