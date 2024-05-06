var http = require('http');

const creds = require('./creds.json');
let authCode;
let clientId = creds.clientId;
let clientSecret = creds.clientSecret;
let scopesList = ['chat:edit', 'chat:read'];
let scopes = scopesList.join('+')

// Serves URL for making ouath request
http.createServer(function (req, res) {
    res.write(`<a href="https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=${clientId}&redirect_uri=http://localhost:3000&scope=${scopes}&state=c3ab8aa609ea11e793ae92361f002671">Authorize</a>`);
    res.end();
}).listen(8080);

// Handles ouath redirect, regexes token from redirect URL
http.createServer(function (req, res) {
    res.write("wuh");
    res.end();
    authCode = req.url.match(/code=(.+?)&/)[1];
    getAuthToken();
}).listen(3000);


// Fetches access token
async function getAuthToken() {
    const url = "https://id.twitch.tv/oauth2/token";
    let data = `client_id=${clientId}&client_secret=${clientSecret}&code=${authCode}&grant_type=authorization_code&redirect_uri=http://localhost:3000`;
    await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        redirect: "follow",
        body: data
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        console.log(data);
    });
}