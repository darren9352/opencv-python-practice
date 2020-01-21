var net = require('net')

var server = net.createServer(function(socket){
    console.log(socket.address().address + " connected.");

    socket.on('data', function(data){
        console.log('rcv:'+data);
    });

    socket.on('close',function(){
        console.log('client disconnected');
    })

    socket.write('welcome to server');
});

server.on('error', function(err){
    console.log('err'+err);
});

server.listen(5000, function(){
    console.log('listening on 5000..');
})