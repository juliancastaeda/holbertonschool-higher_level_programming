#!/usr/bin/node

const fs = require('fs');
const doc = process.argv[2];
const input = process.argv[3];

fs.writeFile(doc, input, 'utf-8', (err) => {
  if (err) { console.log(err); }
});
