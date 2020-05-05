#!/usr/bin/node
const myargv = process.argv.slice();

if (myargv.length === 2) {
  console.log('undefined is undefined');
}

if (myargv.length === 3) {
  console.log(myargv[2], 'is undefined');
}

if (myargv.length === 4) {
  console.log(myargv[2], 'is', myargv[3]);
}
