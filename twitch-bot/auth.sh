#/bin/bash

read -p "Code: " clientCo
read -p "ID: " clientID
read -p "Secret: " clientSe


curl -X POST 'https://id.twitch.tv/oauth2/token' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d "client_id=$clientID&client_secret=$clientSe&code=$clientCo&grant_type=authorization_code&redirect_uri=http://localhost:3000"
