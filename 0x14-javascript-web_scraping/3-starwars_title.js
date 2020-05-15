#!/usr/bin/node
const quest = require('request');
const episode = process.argv[2];

quest('http://swapi.co/api/films/' + episode, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
