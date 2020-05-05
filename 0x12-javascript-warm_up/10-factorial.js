#!/usr/bin/node

if (isNaN(parseInt(process.argv[2])) || parseInt(process.argv[2]) === 0 || parseInt(process.argv[2]) === undefined) {
  console.log('1');
} else {
  let fact = 1;
  for (let count = parseInt(process.argv[2]); count > 0; count--) {
    fact *= count;
  }
  console.log(fact);
}
