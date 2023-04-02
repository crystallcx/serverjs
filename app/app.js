// define variables
const http = require('http'); // include http library inside hhtp variable
const fs = require('fs') // for file handling
const port = 3000;

const server = http.createServer(function(req, res) { // call createServer function of http library
// handle all activity on server

    // 200 = Status Code OK
    res.writeHead(200, { 'Content-Type': 'text/html'})
    fs.readFile('index.html', function(error, data) {
        if(error) {
            res.writeHead(404);
            res.write('Error: File not found')
        } else {
            res.write(data); // write data from index.html
        }
        res.end();
    });

    // // write plaintext Hello Node to every request sent
    // res.write('Hello Node');
    // res.end();
})

// setup server so that it listens on port 3000
server.listen(port, function(error) {
    if (error) {
        console.log('Something went wrong', error);
    } else {
        console.log('Server is listening on port ' + port);
    }
})

// const http = require('http');
// const hostname = '127.0.0.1';
// const port = 3000;
// const server = http.createServer((req, res) => {
// res.statusCode = 200;
// res.setHeader('Content-Type', 'text/plain');
// res.end('Hello World\n');
// });
// server.listen(port, hostname, () => {
// console.log(`Server running at http://${hostname}:${port}/`);
// })