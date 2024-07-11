#!/usr/bin/node
const request = require('util').promisify(require('request'));

async function starWarsCharacters () {
    let url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
    const response = await (await request(url)).body;
    const chars = JSON.parse(response).characters;
    for (let i = 0; i < chars.length; i++) {
        let character = await (await request(chars[i])).body;
        console.log(JSON.parse(character).name);
    }
}

starWarsCharacters();
