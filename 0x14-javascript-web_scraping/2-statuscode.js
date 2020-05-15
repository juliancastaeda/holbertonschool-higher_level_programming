#!/usr/bin/node
const Argument = process.argv.slice(2);
const quest = require('request');
quest(Argument[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
