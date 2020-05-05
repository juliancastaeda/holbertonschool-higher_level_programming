#!/usr/bin/node

function facR (fact) {
  if (isNaN(fact)) {
    return 1;
  } else {
    return fact * (facR(fact - 1));
  }
}
const fact = parseInt(process.argv[2]);
console.log(facR(fact));
