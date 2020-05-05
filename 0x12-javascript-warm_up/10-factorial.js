#!/usr/bin/node

function fac (num) {
  if (isNaN(num) || num === undefined || num === 0) {
    return 1;
  } else {
    return num * (fac(num - 1));
  }
}
const num = parseInt(process.argv[2]);
console.log(fac(num));
