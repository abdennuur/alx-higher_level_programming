#!/usr/bin/node

const rqst = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
let defin = {};
rqst(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const abc = JSON.parse(body);
    abc.characters.forEach(function (item, index, array) {
      rqst(item, function (error, response, content) {
        if (error) {
          console.log(error);
        } else {
          defin = JSON.parse(content);
          console.log(defin.name);
        }
      });
    });
  }
});
