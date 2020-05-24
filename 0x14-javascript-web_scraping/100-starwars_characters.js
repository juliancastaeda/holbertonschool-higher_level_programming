#!/usr/bin/node
// script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// You must use the Star wars API
// You must use the module request
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    for (const chars of JSON.parse(body).characters) {
      request.get(chars, function (error, response, body) {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
