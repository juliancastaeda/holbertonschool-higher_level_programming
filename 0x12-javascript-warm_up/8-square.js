#!/usr/bin/node

const x = parseInt(process.argv[2]);
let X = '';
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= x; i++) {
    for (let j = 1; j <= x; j++) {
      X += 'X';
    }
    if (i < x) { X += '\n'; }
  }
  console.log(X);
}
