#!/usr/bin/node

let num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('1');
} else {
  let fact = 1;
  for (let count = num; count > 0; count--) {
      fact *= count;
  }
    console.log(fact);
}
