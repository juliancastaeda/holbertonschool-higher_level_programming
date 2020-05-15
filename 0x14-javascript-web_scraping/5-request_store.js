#!/usr/bin/node
const quest = require('request');
const fs = require('fs');
const url = process.argv[2];
const output = process.argv[3];

function saveToFile (content, outputFile) {
  fs.writeFile(output, content, 'utf8', (err) => {
    if (err) { console.log(err); }
  });
}

quest
  .get(url, 'utf8', (err, res, body) => {
    if (err) { console.log(err); }
    saveToFile(body, output);
  });
