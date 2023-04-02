## Launching
Run locally by navigating to inside app/ folder and running:
```sh
node app.js
```


To run it using docker:
```sh
docker build -t serverjs-demo .
docker run -d -p3000:3000 serverjs-demo
```

Access the server by navigating to
`localhost:3000` on your browser