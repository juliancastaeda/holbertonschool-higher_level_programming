#!/usr/bin/node
const myargv = process.argv.slice();

if (myargv.length === 2) {
  console.log('No argument');
}

if (myargv.length === 3) {
  console.log('Argument found');
}

if (myargv.length > 3) {
  console.log('Arguments found');
}
