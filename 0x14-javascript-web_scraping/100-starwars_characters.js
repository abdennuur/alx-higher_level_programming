#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
function makeRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function main() {
  try {
    const movieResponse = await makeRequest(baseUrl + argv[2]);
    const characters = JSON.parse(movieResponse).characters;

    const characterNames = await Promise.all(characters.map(async function (characterUrl) {
      const characterResponse = await makeRequest(characterUrl);
      return JSON.parse(characterResponse).name;
    }));

    characterNames.sort();
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(error);
  }
}

main();
