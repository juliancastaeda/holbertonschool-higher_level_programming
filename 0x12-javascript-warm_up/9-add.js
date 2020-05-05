#!/usr/bin/node

let suma = '';
if (isNaN(process.argv[2])) {
  console.log('NaN');
} else {
  suma = parseInt(process.argv[2]) + parseInt(process.argv[3]);
  console.log(suma);
}
