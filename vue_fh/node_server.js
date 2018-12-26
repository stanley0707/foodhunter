var io = require('socket.io');
var http = require('http');

var app = http .createServer();
var io = io.listen(app);
app.listen(4000);

io.sockets.on('connection', function (socket) {
    
    socket.on('eventServer', function (data) {
        socket.emit('eventClient', { data: 'Hello Client' });
        console.log(data);
        
    });
    
    socket.on('eventClient', function () {
        socket.emit('eventClient', { data: 'Hello Client' });
    });
    
    socket.on('disconnect', function () {
        console.log('user disconnected');
    });
});