#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
let id = parseInt(process.argv[2], 10);
let characters = [];

request(url, function (err, response, body) {
  if (err == null) {
    const rsp = JSON.parse(body);
    const results = rsp.results;
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }
    for (let ix = 0; ix < results.length; i++) {
      if (results[ix].episode_id === id) {
        characters = results[ix].characters;
        break;
      }
    }
    for (let ji = 0; ji < characters.length; ji++) {
      request(characters[ji], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
